/* ==========================================================================
   graph-demo.js  —  tc-ventures.ca

   The Grande Prairie budget slice of the Economic Report Influence Graph,
   drawn live in 3D on demand.

   Rules this file obeys:
   - Nothing runs, and nothing downloads, until the button is pressed. The
     1.3MB renderer is fetched on click, never on load.
   - The button does not exist without JavaScript. It is `hidden` in the
     markup and unhidden here, so a reader with JS off sees the still and the
     written chain underneath it and misses nothing.
   - prefers-reduced-motion means the layout is solved before the first frame
     and then sits still. It is not "the same thing, faster".
   ========================================================================== */
(function () {
  'use strict';

  var mount = document.getElementById('graph-demo');
  if (!mount) return;

  var btn = mount.querySelector('.gd__load');
  var stage = mount.querySelector('.gd__stage');
  var panel = mount.querySelector('.gd__panel');
  var still = mount.querySelector('.gd__still');
  if (!btn || !stage || !panel || !still) return;

  /* WebGL is the one hard requirement. Ask before promising anything. */
  var webgl = (function () {
    try {
      var c = document.createElement('canvas');
      return !!(window.WebGLRenderingContext &&
        (c.getContext('webgl') || c.getContext('experimental-webgl')));
    } catch (e) { return false; }
  })();
  if (!webgl) return;

  btn.hidden = false;

  var TIER = {
    municipal:     '#F0A64E',
    provincial:    '#5CC7D1',
    federal:       '#7FA8F0',
    institutional: '#C08FE0',
    international: '#78C98D'
  };
  var GRADE = { A: '#BFE3E8', B: '#7E8C9C', C: '#4E5866' };
  var ROOT = '#FFFFFF';

  var reduce = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  var REL = {
    uses_data_from: 'uses data from',
    calculated_from: 'is calculated from',
    methodology_depends_on: 'follows the methodology of',
    cites: 'cites',
    legal_basis: 'has its legal basis in'
  };

  function say(html) { panel.innerHTML = html; }

  function sayIdle() {
    say('<p class="gd__hint">Drag to turn it. Click a line, or use the arrow ' +
        'keys, to read the document the dependency was drawn from and the ' +
        'grade it earned.</p>');
  }

  function sayNode(n) {
    say(
      '<p class="gd__kicker">' + esc(n.tier) + '</p>' +
      '<p class="gd__title">' + esc(n.title) + '</p>' +
      '<p class="gd__meta">' + esc(n.publisher) + '</p>' +
      (n.rests > 0
        ? '<p class="gd__meta">Depended on ' +
          (n.rests === 1 ? 'once' : 'by ' + n.rests + ' reports') +
          ' across the whole corpus.</p>'
        : '<p class="gd__meta">Nothing in the corpus rests on this one yet.</p>') +
      (n.url ? '<p class="gd__src"><a href="' + esc(n.url) +
        '" rel="noopener">The report itself</a></p>' : '')
    );
  }

  function sayLink(l) {
    var s = l.source, t = l.target;
    say(
      '<p class="gd__kicker">Evidence <span class="gd__grade gd__grade--' +
        esc(l.grade) + '">' + esc(l.grade) + '</span></p>' +
      '<p class="gd__title">' + esc(s.title) + ' <span class="gd__rel">' +
        esc(REL[l.rel] || l.rel) + '</span> ' + esc(t.title) + '</p>' +
      '<blockquote class="gd__basis">' + esc(l.basis) + '</blockquote>' +
      (l.url ? '<p class="gd__src"><a href="' + esc(l.url) +
        '" rel="noopener">The document this was read out of</a></p>' : '')
    );
  }

  function load(src) {
    return new Promise(function (res, rej) {
      var s = document.createElement('script');
      s.src = src;
      s.onload = res;
      s.onerror = function () { rej(new Error('script')); };
      document.head.appendChild(s);
    });
  }

  function fail() {
    btn.hidden = true;
    panel.focus({ preventScroll: true });
    say('<p class="gd__hint">The live graph did not load. The still above and ' +
        'the chain below are the same data; the ' +
        '<a href="https://github.com/DriftingSplash9/Reports-Clustering">' +
        'repository</a> has all of it.</p>');
  }

  btn.addEventListener('click', function () {
    btn.disabled = true;
    btn.textContent = 'Loading…';

    Promise.all([
      fetch('/assets/gp-budget-graph.json').then(function (r) {
        if (!r.ok) throw new Error('data');
        return r.json();
      }),
      load('/assets/3d-force-graph.min.js')
    ]).then(function (out) {
      var data = out[0];
      if (!window.ForceGraph3D) throw new Error('lib');

      still.hidden = true;
      btn.hidden = true;
      stage.hidden = false;
      sayIdle();

      /* Keyboard path: the stage takes focus, and the arrow keys walk the
         dependencies in the order the data lists them. Each one is read into
         the panel (a live region) and drawn thicker in the scene. The camera
         never moves for it. */
      var current = null, idx = -1, g;
      function mark(l) {
        current = l;
        idx = l ? data.links.indexOf(l) : -1;
        if (g) g.linkColor(g.linkColor()).linkWidth(g.linkWidth());
      }
      stage.addEventListener('keydown', function (e) {
        var n = data.links.length;
        if (!n) return;
        if (e.key === 'ArrowRight' || e.key === 'ArrowDown') idx = (idx + 1) % n;
        else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') idx = (idx - 1 + n) % n;
        else if (e.key === 'Escape') { mark(null); sayIdle(); return; }
        else return;
        e.preventDefault();
        mark(data.links[idx]);
        sayLink(data.links[idx]);
      });

      var maxRests = data.nodes.reduce(function (m, n) {
        return Math.max(m, n.rests || 0);
      }, 1);

      g = window.ForceGraph3D({ controlType: 'orbit' })(stage)
        .backgroundColor('#060913')
        .showNavInfo(false)
        .graphData(data)
        .nodeId('id')
        .nodeRelSize(5)
        /* Size is authority: how much of the whole corpus rests on that one
           release. Square-rooted, because the eye reads area, not radius. */
        .nodeVal(function (n) {
          if (n.id === data.root) return 3.2;
          return 0.6 + 7 * Math.sqrt((n.rests || 0) / maxRests);
        })
        .nodeColor(function (n) {
          return n.id === data.root ? ROOT : (TIER[n.tier] || '#8A99A8');
        })
        .nodeOpacity(0.92)
        .nodeLabel(function (n) {
          return '<div class="gd__tip"><strong>' + esc(n.title) +
            '</strong><br>' + esc(n.publisher) + '</div>';
        })
        .linkColor(function (l) {
          return l === current ? '#FFFFFF' : (GRADE[l.grade] || '#7E8C9C');
        })
        .linkOpacity(0.55)
        .linkWidth(function (l) {
          if (l === current) return 2.4;
          return l.grade === 'A' ? 0.9 : 0.5;
        })
        .linkHoverPrecision(5)
        .linkDirectionalArrowLength(3.2)
        .linkDirectionalArrowRelPos(1)
        .linkDirectionalArrowColor(function (l) { return GRADE[l.grade] || '#7E8C9C'; })
        .linkLabel(function (l) {
          return '<div class="gd__tip">' + esc(l.grade) + ' · ' +
            esc(REL[l.rel] || l.rel) + '</div>';
        })
        .onNodeClick(sayNode)
        .onLinkClick(function (l) { mark(l); sayLink(l); })
        .onBackgroundClick(function () { mark(null); sayIdle(); })
        .enableNodeDrag(false);

      g.d3Force('charge').strength(-170);

      /* Reduced motion: solve the layout before the first frame, then stop
         dead. Same picture; it simply never moves on its own. */
      if (reduce) {
        g.warmupTicks(500).cooldownTicks(0);
      } else {
        g.cooldownTime(9000);
      }
      g.graphData(data);

      var W = 0, H = 0;
      function size() {
        W = stage.clientWidth || 800;
        H = Math.round(Math.min(680, Math.max(340, W * 0.62)));
        g.width(W).height(H);
      }
      size();
      window.addEventListener('resize', function () { size(); frame(); });

      /* zoomToFit fits a bounding sphere, which on a graph this elongated
         leaves it swimming in a third of the frame. Fit the actual box. */
      function frame() {
        var ns = g.graphData().nodes, i, k;
        if (!ns.length) return;
        var lo = [1e9, 1e9, 1e9], hi = [-1e9, -1e9, -1e9];
        for (i = 0; i < ns.length; i++) {
          var p = [ns[i].x, ns[i].y, ns[i].z];
          for (k = 0; k < 3; k++) {
            if (!isFinite(p[k])) return;
            if (p[k] < lo[k]) lo[k] = p[k];
            if (p[k] > hi[k]) hi[k] = p[k];
          }
        }
        var c = { x: (lo[0] + hi[0]) / 2, y: (lo[1] + hi[1]) / 2, z: (lo[2] + hi[2]) / 2 };
        var fov = 50 * Math.PI / 180, aspect = W / H;
        var dist = Math.max(
          ((hi[1] - lo[1]) / 2) / Math.tan(fov / 2),
          ((hi[0] - lo[0]) / 2) / (Math.tan(fov / 2) * aspect)
        ) * 1.08 + (hi[2] - lo[2]) / 2;
        g.cameraPosition({ x: c.x, y: c.y, z: c.z + dist }, c, 0);
      }

      /* One framing move, then the camera is the reader's. */
      setTimeout(frame, reduce ? 0 : 1400);

      /* The button that had focus is gone; hand focus to what replaced it. */
      stage.focus({ preventScroll: true });
    }).catch(fail);
  });
})();
