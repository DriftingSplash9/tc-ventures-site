/* The build ledger's scrubber and draw-in (copy-review-007, Phase 3 step 5).

   The ledger is written by scripts/export-ledger.py, and it is whole without
   this file: two pictures, and the list below them. The export also writes the
   scrubber: a native slider, one step per handoff, and every handoff's line
   stacked in one place. CSS shows it only when scripts run.

   Moving the slider to a handoff clips both pictures' threads at that
   handoff's column, marks the column, and shows its line: the ledger as it
   stood then. A thread that closed later is drawn open (teal) there, as it
   was that day (Q-S5-1 B); the export writes each closed thread's column as
   data-e. The slider starts at the newest handoff, which is the whole ledger.

   The draw-in (M2): under Motion Full, the first time the ledger scrolls into
   view, the same slider runs from 001 to the newest, in about three seconds.
   Until then the threads are clipped to 001. Under Reduced and Off it never
   runs, and the ledger is whole from the start. Touching the slider stops it.

   DESIGN-6: this file is deferred, so prefs.js marks <html> (data-lg-wait)
   before the first paint and style.css hides the threads meanwhile. This file
   lifts the mark on every path, and on the draw-in path only once the threads
   are clipped. The draw-in runs only if the mark is still on: if prefs.js's 3 s
   fallback lifted it first, the ledger has been shown whole, so it stays so. */
(function () {
  var root = document.documentElement;
  var waiting = root.hasAttribute('data-lg-wait');
  function release() { root.removeAttribute('data-lg-wait'); }
  var fig = document.querySelector('.ledger');
  var input = document.getElementById('ledger-scrub');
  if (!fig || !input) { release(); return; }

  var n = +input.max;
  var lines = Array.prototype.slice.call(document.querySelectorAll('.ledger__at'));
  var STEP_MS = 110;            // one handoff; 26 handoffs take about 2.9 s
  var NS = 'http://www.w3.org/2000/svg';

  /* Per picture: its columns (along time), and a clip over its threads. */
  var pics = Array.prototype.map.call(fig.querySelectorAll('.ledger__pic'), function (svg, k) {
    var land = svg.classList.contains('ledger__pic--land');
    var vb = svg.viewBox.baseVal;
    var cols = Array.prototype.slice.call(svg.querySelectorAll('.lg__col'));
    var closed = Array.prototype.map.call(svg.querySelectorAll('[data-e]'), function (el) {
      return { el: el, e: +el.getAttribute('data-e') };
    });
    var at = cols.map(function (c) { return +c.getAttribute(land ? 'x1' : 'y1'); });
    var clip = document.createElementNS(NS, 'clipPath');
    clip.id = 'lg-clip-' + k;
    var rect = document.createElementNS(NS, 'rect');
    rect.setAttribute('x', 0); rect.setAttribute('y', 0);
    rect.setAttribute('width', vb.width); rect.setAttribute('height', vb.height);
    clip.appendChild(rect);
    svg.insertBefore(clip, svg.firstChild);
    svg.querySelector('.lg__threads').setAttribute('clip-path', 'url(#' + clip.id + ')');
    return { land: land, vb: vb, cols: cols, at: at, rect: rect, closed: closed };
  });

  /* Show the ledger as it stood at handoff v (1 to n); a fraction draws part of
     the way to the next column. */
  var shown = n;
  function show(v) {
    var j = Math.min(Math.floor(v), n) - 1;
    pics.forEach(function (p) {
      var reach;
      if (v >= n) reach = p.land ? p.vb.width : p.vb.height;
      else {
        var f = v - Math.floor(v);
        reach = p.at[j] + (p.at[j + 1] - p.at[j]) * f + 4;
      }
      p.rect.setAttribute(p.land ? 'width' : 'height', reach);
      p.cols.forEach(function (c, i) { c.classList.toggle('lg__col--on', i === j); });
      p.closed.forEach(function (c) { c.el.classList.toggle('lg__then-open', c.e > j); });
    });
    if (j + 1 !== shown) {
      shown = j + 1;
      input.value = shown;
      lines.forEach(function (l, i) { l.classList.toggle('is-on', i === j); });
      var at = lines[j];
      input.setAttribute('aria-valuetext', 'handoff-' + at.querySelector('b').textContent + ', '
        + at.querySelector('time').textContent + ': ' + at.querySelector('span').textContent);
    }
  }
  shown = 0;
  show(n);

  var raf = 0;
  function stop() { if (raf) { cancelAnimationFrame(raf); raf = 0; } }
  input.addEventListener('input', function () { stop(); show(+input.value); });

  var full = window.tcvMotion ? window.tcvMotion() === 'full' : true;
  if (!full || !waiting || !('IntersectionObserver' in window) || n < 2) { release(); return; }

  show(1);
  release();                            // clipped and revealed in one step (DESIGN-6)
  var io = new IntersectionObserver(function (entries) {
    if (!entries.some(function (e) { return e.isIntersecting; })) return;
    io.disconnect();
    if (+input.value !== 1 || window.tcvMotion() !== 'full') { stop(); show(+input.value === 1 ? n : +input.value); return; }
    var t0 = 0;
    raf = requestAnimationFrame(function tick(t) {
      if (!t0) t0 = t;
      var v = window.tcvMotion() === 'full' ? 1 + (t - t0) / STEP_MS : n;   // Off or Reduced chosen mid-way
      show(Math.min(v, n));
      raf = v < n ? requestAnimationFrame(tick) : 0;
    });
  }, { threshold: 0.35 });
  io.observe(fig);
})();
