/* The build ledger as a 3D scene behind the home hero (copy-review-010, H-0 ruled 2026-10-02).

   The same ledger as the two SVG pictures, from assets/ledger-data.json (written by
   scripts/export-ledger.py). Time runs into depth: each handoff is a gate across the
   floor, the newest nearest. The bands are lanes side by side; each item is a filament
   from the gate where it opened to the gate where it closed. Carried items run to the
   front edge in teal; closed ones stop with a square cap; parked ones are dotted. The
   traps are a second layer under a translucent floor.

   It follows ledger.js: every step of the slider and of M2's draw-in arrives as an
   'lg:show' event on the figure. Dragging the scene moves the slider. The page
   scrolls as normal; under Motion Full the camera rises as the hero leaves (Q-H2 A).
   No words of its own (Q-H3 A): the gate numbers and band names are on the page already.

   The journey (TP-A, copy-review-013, ruled 2026-10-03): under Motion Full on a wide
   screen, this file adds an empty runway after the ledger's list, and the scene holds
   its place (sticky) while the reader scrolls it. The camera dives back to 001 as the
   ledger rewinds, travels gate by gate to the newest as it builds again, each gate's
   ruled line shown beside it (aria-hidden: the list carries every line), then rises to
   the whole ledger, and the page carries on. Native scroll drives it, so the reader
   sets the pace. The slider follows. Reduced, Off, 45em and under: no runway, as before.

   prefs.js marks <html> data-lg-scene on the home page when WebGL2 and modules exist,
   and CSS hides the SVG pictures while it's there. This file sets it to "on" once the
   scene has drawn, and takes it off if anything fails, so the SVGs come back. Three.js
   is imported inside start(), so a failed load gives up at once instead of leaving the
   page to prefs.js's 5 s fallback. */
let THREE;

const root = document.documentElement;
const hero = document.querySelector('.hero--home');
const fig = document.querySelector('.ledger');
const input = document.getElementById('ledger-scrub');
const scrub = fig && fig.querySelector('.ledger__scrub');
let canvas = null, renderer = null;

function giveUp(err) {
  if (err) console.warn('ledger scene off:', err);
  root.removeAttribute('data-lg-scene');
  if (renderer) renderer.dispose();
  if (canvas) canvas.remove();
}

if (!hero || !fig || !input || !scrub || !root.hasAttribute('data-lg-scene')) giveUp();
else start().catch(giveUp);

async function start() {
  const [lib, res] = await Promise.all([import('./vendor/three/three.module.min.js'), fetch('/assets/ledger-data.json')]);
  THREE = lib;
  if (!res.ok) throw new Error('ledger-data.json ' + res.status);
  const data = await res.json();
  if (!root.hasAttribute('data-lg-scene')) return;          // prefs.js gave up waiting: the SVGs show
  await document.fonts.load('10px "IBM Plex Mono"').catch(() => {});

  canvas = document.createElement('canvas');
  canvas.className = 'lg-scene';
  canvas.setAttribute('aria-hidden', 'true');
  renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' });

  const n = data.cols.length;
  const mqNarrow = matchMedia('(max-width: 45em)');
  const mqMore = matchMedia('(prefers-contrast: more)');
  const mqDark = matchMedia('(prefers-color-scheme: dark)');
  const motion = () => (window.tcvMotion ? window.tcvMotion() : 'full');
  const more = () => (root.getAttribute('data-contrast') || (mqMore.matches ? 'more' : 'standard')) === 'more';
  const dark = () => (root.getAttribute('data-theme') || (mqDark.matches ? 'dark' : 'light')) === 'dark';

  /* ---- layout, in world units ---- */
  const DZ = 0.55, LW = 0.085, BG = 0.34, TY = -0.46, FRONT = 0.42;
  const zOf = j => j * DZ;
  let W = 0;
  data.bands.forEach((b, i) => { b.x0 = W; W += b.lanes * LW + (i < data.bands.length - 1 ? BG : 0); });
  const X0 = -W / 2;
  const items = [];
  data.bands.forEach(b => b.t.forEach(([lane, s, e, state]) => {
    items.push({ x: X0 + b.x0 + (lane + 0.5) * LW, y: 0.012, s, e, state });
  }));
  const traps = [];
  if (data.traps) {
    const tl = W / data.traps.lanes;
    data.traps.t.forEach(([lane, s, e, state, how, helped, inf]) => {
      traps.push({ x: X0 + (lane + 0.5) * tl, y: TY, s, e, state, how, helped, inf, trap: true });
    });
  }
  const threads = items.concat(traps);
  const depth = zOf(n - 1);

  /* ---- scene ---- */
  const scene = new THREE.Scene();
  scene.fog = new THREE.Fog(0x000000, 6, 30);
  const camera = new THREE.PerspectiveCamera(42, 1, 0.05, 80);
  const box = new THREE.BoxGeometry(1, 1, 1);
  const ball = new THREE.SphereGeometry(1, 12, 8);
  const ring = new THREE.TorusGeometry(1, 0.24, 6, 18);
  const solid = () => new THREE.MeshBasicMaterial({ color: 0xffffff, fog: true });
  function inst(geo, mat, count) {
    const m = new THREE.InstancedMesh(geo, mat, Math.max(count, 1));
    m.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
    m.setColorAt(0, new THREE.Color());
    m.frustumCulled = false;
    scene.add(m);
    return m;
  }
  const glowMat = new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.2, depthWrite: false, fog: true });
  const rods = inst(box, solid(), threads.length * 2);            // a thread, and a trap's inferred stretch
  const glow = inst(box, glowMat, threads.length);
  const dots = inst(ball, solid(), threads.length);
  const caps = inst(box, solid(), threads.length);
  const rings = inst(ring, solid(), traps.reduce((a, t) => a + t.helped.length, 0));
  // Parked items and the traps' inferred starts are drawn as dots 0.11 apart: room for every one of them.
  const DOT = 0.11;
  const dotCap = threads.reduce((a, t) => a
    + (t.state === 'parked' ? Math.ceil((zOf(n - 1) + FRONT - zOf(t.s)) / DOT) + 1 : 0)
    + (t.trap && t.inf !== null && t.s < t.inf ? Math.ceil((zOf(t.inf) - zOf(t.s)) / DOT) + 1 : 0), 0);
  const parkedDots = inst(ball, solid(), dotCap);
  const gates = inst(box, solid(), n * 3);
  const floorMat = new THREE.MeshBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.8, depthWrite: false, fog: true });
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(W + 1.4, depth + 30), floorMat);
  floor.rotation.x = -Math.PI / 2;
  floor.position.set(0, -0.02, depth / 2);
  floor.renderOrder = 1;
  scene.add(floor);

  /* ---- labels: gate numbers and band names, drawn into textures ---- */
  const labels = new THREE.Group();
  scene.add(labels);
  function texture(text, color, px) {
    const c = document.createElement('canvas');
    const g = c.getContext('2d');
    const font = `${px}px "IBM Plex Mono", ui-monospace, monospace`;
    g.font = font;
    c.width = Math.ceil(g.measureText(text).width) + 8;
    c.height = Math.ceil(px * 1.4);
    g.font = font;
    g.fillStyle = color;
    g.textBaseline = 'middle';
    g.fillText(text, 4, c.height / 2);
    const t = new THREE.CanvasTexture(c);
    t.colorSpace = THREE.SRGBColorSpace;
    t.anisotropy = 4;
    return { t, aspect: c.width / c.height };
  }
  let gateLabels = [], bandLabels = [];
  function buildLabels(pal) {
    labels.children.slice().forEach(o => { o.material.map.dispose(); o.material.dispose(); labels.remove(o); });
    const scale = parseFloat(getComputedStyle(root).fontSize) / 16;
    gateLabels = data.cols.map(([num], k) => {
      const { t, aspect } = texture(num, pal.muted, 40);
      const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: t, transparent: true, depthWrite: false, fog: true }));
      const h = 0.11 * scale;
      s.scale.set(h * aspect, h, 1);
      s.position.set(X0 - 0.42, 0.06, zOf(k));
      s.userData.k = k;
      labels.add(s);
      return s;
    });
    const flat = (text, x, y) => {
      const { t, aspect } = texture(text, pal.muted, 40);
      const m = new THREE.Mesh(new THREE.PlaneGeometry(1, 1),
        new THREE.MeshBasicMaterial({ map: t, transparent: true, depthWrite: false, fog: true }));
      const h = 0.1 * scale;
      m.scale.set(h * aspect, h, 1);
      m.rotation.x = -Math.PI / 2;
      m.position.set(x, y + 0.004, 0);
      m.renderOrder = 2;
      labels.add(m);
      return m;
    };
    bandLabels = data.bands.map(b => flat(b.name, X0 + b.x0 + (b.lanes * LW) / 2, 0));
    if (data.traps) bandLabels.push(flat(data.traps.name, 0, TY));
  }

  /* ---- colours from the page's own tokens ---- */
  let pal;
  function readPalette() {
    const cs = getComputedStyle(root);
    const v = k => cs.getPropertyValue(k).trim();
    pal = { paper: v('--paper'), ink: v('--ink'), muted: v('--muted'), rule: v('--rule'), accent: v('--accent'),
            dark: dark(), more: more() };
    pal.c = {
      paper: new THREE.Color(pal.paper), muted: new THREE.Color(pal.muted), accent: new THREE.Color(pal.accent),
      rule: new THREE.Color(pal.rule), ink: new THREE.Color(pal.ink),
    };
    renderer.setClearColor(pal.c.paper, 1);
    scene.fog.color.copy(pal.c.paper);
    floorMat.color.copy(pal.c.paper);
    floorMat.opacity = pal.more ? 0.9 : 0.8;
    glowMat.blending = pal.dark ? THREE.AdditiveBlending : THREE.NormalBlending;
    glowMat.opacity = pal.dark ? 0.22 : 0.1;
    glowMat.needsUpdate = true;
    buildLabels(pal);
  }

  /* ---- drawing the ledger as it stood at handoff jf (0 .. n-1, fractions between) ---- */
  const M = new THREE.Matrix4(), Q = new THREE.Quaternion(), P = new THREE.Vector3(), S = new THREE.Vector3();
  const C = new THREE.Color();
  const flatRing = new THREE.Quaternion().setFromEuler(new THREE.Euler(-Math.PI / 2, 0, 0));
  const NONE = new THREE.Matrix4().makeScale(0, 0, 0);
  let hovered = null;
  let short = false;
  function put(mesh, i, x, y, z, sx, sy, sz, color, q) {
    if (i >= mesh.count) {                                      // a mark with no room: say so once (site_check's console check)
      if (!short) { short = true; console.error('ledger scene: more marks than room for them; some are not drawn'); }
      return;
    }
    P.set(x, y, z); S.set(sx, sy, sz);
    M.compose(P, q || Q.identity(), S);
    mesh.setMatrixAt(i, M);
    if (color) mesh.setColorAt(i, color);
  }
  function tone(base, t) {
    if (hovered === null) return base;
    return t === hovered ? (pal.dark ? pal.c.ink : pal.c.accent) : C.copy(base).lerp(pal.c.paper, 0.72);
  }
  function draw(jf) {
    const wide = pal.more ? 1.6 : 1;
    let r = 0, g = 0, d = 0, c = 0, h = 0, p = 0;
    const edge = zOf(jf) + (jf >= n - 1 ? FRONT : 0.06);
    for (const t of threads) {
      if (t.s > jf) continue;
      const closedNow = t.state === 'closed' && t.e <= jf;
      const zA = zOf(t.s), zB = closedNow ? zOf(t.e) : edge;
      const base = closedNow ? pal.c.muted : pal.c.accent;
      const col = tone(base, t);
      const w = (closedNow ? 0.016 : 0.024) * wide, hh = closedNow ? 0.008 : 0.014;
      let from = zA;
      if (t.trap && t.inf !== null && t.s < t.inf) {            // the inferred start, before 019: dotted, as the caption says
        const zI = Math.min(zOf(t.inf), zB);
        for (let z = zA; z < zI; z += DOT) {
          put(parkedDots, p++, t.x, t.y, z, 0.012 * wide, 0.012 * wide, 0.012 * wide, col);
        }
        from = zI;
      }
      if (t.state === 'parked' && !closedNow) {
        for (let z = from; z < zB; z += DOT) {
          put(parkedDots, p++, t.x, t.y, z, 0.016 * wide, 0.016 * wide, 0.016 * wide, col);
        }
      } else if (zB > from) {
        put(rods, r++, t.x, t.y, (from + zB) / 2, w, hh, zB - from, col);
      }
      if (!closedNow && !pal.more && t.state !== 'parked') {
        put(glow, g++, t.x, t.y, (from + zB) / 2, 0.16, 0.05, zB - from, col);
      }
      put(dots, d++, t.x, t.y, zA, 0.022 * wide, 0.022 * wide, 0.022 * wide, col);
      if (closedNow) {
        if (t.trap && t.how === 'into code') put(caps, c++, t.x, t.y, zB, 0.05, 0.05, 0.05, col);
        else put(caps, c++, t.x, t.y, zB, 0.06, 0.035, 0.01, col);
      }
      if (t.trap) {
        for (const k of t.helped) {
          if (k > jf) continue;
          put(rings, h++, t.x, t.y, zOf(k), 0.03, 0.03, 0.03, col, flatRing);
        }
      }
    }
    const on = Math.min(Math.round(jf), n - 1);
    let q = 0;
    for (let k = 0; k < n; k++) {
      if (k > jf + 0.001) continue;
      const lit = k === on || (hovered && (k === hovered.s || k === hovered.e));
      const gc = lit ? pal.c.accent : pal.c.rule;
      const z = zOf(k);
      put(gates, q++, 0, -0.005, z, W + 0.5, 0.006, 0.01, gc);
      put(gates, q++, X0 - 0.25, 0.11, z, 0.008, 0.24, 0.008, gc);
      put(gates, q++, -X0 + 0.25, 0.11, z, 0.008, 0.24, 0.008, gc);
    }
    for (const [mesh, used] of [[rods, r], [glow, g], [dots, d], [caps, c], [rings, h], [parkedDots, p], [gates, q]]) {
      for (let i = used; i < mesh.count; i++) mesh.setMatrixAt(i, NONE);
      mesh.instanceMatrix.needsUpdate = true;
      if (mesh.instanceColor) mesh.instanceColor.needsUpdate = true;
    }
    for (const s of gateLabels) {
      const k = s.userData.k;
      s.visible = k <= jf + 0.001 && (k % 5 === 0 || k === n - 1 || k === on);
      s.material.opacity = k === on ? 1 : 0.7;
    }
    const zf = zOf(Math.max(jf, 0)) + FRONT + 0.22;
    for (const m of bandLabels) m.position.z = zf;
  }

  /* ---- the camera ---- */
  const pointer = { x: 0, y: 0, tx: 0, ty: 0 };
  const cam = { pos: new THREE.Vector3(), look: new THREE.Vector3(), ready: false };
  let rise = 0;
  /* The journey's state: J is how far through the runway the page has scrolled (0 to 1), Js eases after it. */
  const DIVE = 0.15, TRAVEL = 0.85;                             // where the dive ends, and where the travel ends
  let journey = false, J = 0, Js = 0, runway = null, say = null, sayK = -1;
  const lines = Array.prototype.slice.call(document.querySelectorAll('.ledger__at'));
  function aim(jf, out) {
    const narrow = mqNarrow.matches;
    const front = zOf(jf) + FRONT;
    const prog = n > 1 ? jf / (n - 1) : 1;
    const ease = 1 - Math.pow(1 - prog, 2);
    let px, py, pz, lx, ly, lz;
    if (narrow) {                                               // portrait: time runs down the screen
      px = 0; py = 7.6 - 1.6 * ease; pz = front + 2.6; lx = 0; ly = 0; lz = front - 4.4;
    } else {
      px = -1.2; py = 5.6 - 1.4 * ease; pz = front + 3.2; lx = 0.3; ly = 0; lz = front - 4.6;
    }
    px += pointer.x * 0.5; py += pointer.y * 0.25;
    if (rise > 0) {                                             // the hero leaving: up to the whole ledger
      const mid = depth / 2;
      px += (0 - px) * rise; py += (Math.max(9, depth * 0.75) - py) * rise; pz += (mid + 3 - pz) * rise;
      lx += (0 - lx) * rise; lz += (mid - lz) * rise;
    }
    out.pos.set(px, py, pz); out.look.set(lx, ly, lz);
  }
  /* The journey's poses: low over the floor just ahead of the build front, looking back down the years, swaying
     side to side; then up over the whole ledger. */
  function travelPose(jf, out) {
    const front = zOf(jf) + 0.4, sway = Math.sin(jf * 0.35) * 0.9;
    out.pos.set(sway + pointer.x * 0.3, 0.95 + pointer.y * 0.15, front + 2.3);
    out.look.set(sway * 0.3, 0.1, front - 2.6);
  }
  function risePose(out) {
    const mid = depth / 2;
    out.pos.set(0, Math.max(9, depth * 0.75), mid + 3); out.look.set(0, 0, mid);
  }
  const PA = { pos: new THREE.Vector3(), look: new THREE.Vector3() }, PB = { pos: new THREE.Vector3(), look: new THREE.Vector3() };
  const smooth = t => t * t * (3 - 2 * t);
  function journeyAt(j, out) {                                  // sets the camera's goal; returns the handoff drawn
    if (j <= DIVE) {
      const e = smooth(j / DIVE);
      aim(n - 1, PA); travelPose(0, PB);
      out.pos.lerpVectors(PA.pos, PB.pos, e); out.look.lerpVectors(PA.look, PB.look, e);
      return (n - 1) * (1 - e);
    }
    if (j <= TRAVEL) {
      const jf = (n - 1) * (j - DIVE) / (TRAVEL - DIVE);
      travelPose(jf, out);
      return jf;
    }
    const e = smooth((j - TRAVEL) / (1 - TRAVEL));
    travelPose(n - 1, PA); risePose(PB);
    out.pos.lerpVectors(PA.pos, PB.pos, e); out.look.lerpVectors(PA.look, PB.look, e);
    return n - 1;
  }
  /* Each gate's ruled line, beside its right post, while the camera travels. */
  function sayAt(jf, j) {
    if (!say) return;
    if (j <= DIVE || j >= TRAVEL + 0.02) { say.removeAttribute('data-on'); return; }
    const on = Math.min(Math.round(jf), n - 1);
    if (on !== sayK && lines[on]) {
      sayK = on;
      const at = lines[on], b = document.createElement('b'), tm = document.createElement('time'), sp = document.createElement('span');
      b.textContent = 'handoff-' + at.querySelector('b').textContent;
      tm.textContent = at.querySelector('time').textContent;
      sp.textContent = at.querySelector('span').textContent;
      say.replaceChildren(b, tm, sp);
    }
    P.set(-X0 + 0.32, 0.24, zOf(on)).project(camera);
    if (P.z > 1) { say.removeAttribute('data-on'); return; }
    const r = canvas.getBoundingClientRect();
    const x = Math.min(r.left + (P.x + 1) / 2 * r.width + 14, innerWidth - say.offsetWidth - 24);
    const y = Math.max(96, Math.min(r.top + (1 - P.y) / 2 * r.height, innerHeight - say.offsetHeight / 2 - 24));
    say.style.setProperty('--x', Math.round(Math.max(24, x)) + 'px');     // whole pixels: the text stays crisp
    say.style.setProperty('--y', Math.round(y) + 'px');
    say.setAttribute('data-on', '');
  }

  /* ---- placing the canvas ---- */
  function place() {
    if (mqNarrow.matches) {
      if (canvas.parentNode !== fig) fig.insertBefore(canvas, scrub);
      hero.style.removeProperty('--lg-scene-h');
      fig.style.removeProperty('--lg-cap-gap');
    } else if (journey) {                                       // the journey: the scene fills the screen (CSS);
      if (canvas.parentNode !== hero) hero.insertBefore(canvas, hero.firstChild);
      const top = hero.getBoundingClientRect().top;            // the scrim covers the words, down to the runway
      hero.style.setProperty('--lg-scene-h', (runway.getBoundingClientRect().top - top) + 'px');
      fig.style.removeProperty('--lg-cap-gap');
    } else {
      if (canvas.parentNode !== hero) hero.insertBefore(canvas, hero.firstChild);
      const top = hero.getBoundingClientRect().top;
      const below = scrub.getBoundingClientRect().bottom - top;
      const h = Math.max(window.innerHeight - Math.max(top + window.scrollY, 0), below + 56);
      hero.style.setProperty('--lg-scene-h', h + 'px');
      fig.style.setProperty('--lg-cap-gap', Math.max(h - below + 12, 12) + 'px');
    }
    const w = canvas.clientWidth, h = canvas.clientHeight;
    if (!w || !h) return;
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, mqNarrow.matches ? 1.5 : 2));
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    offset(1 - (journey ? smooth(Math.min(Js / DIVE, 1)) : 0));
    kick();
  }
  function offset(o) {                                          // the ledger right of and under the headline; o = 0: centred
    const w = canvas.clientWidth, h = canvas.clientHeight;
    if (mqNarrow.matches || !w || !h) camera.clearViewOffset();
    else camera.setViewOffset(w, h, -w * 0.35 * o, h * 0.04 * o, w, h);
    camera.updateProjectionMatrix();
  }

  /* ---- state, and the loop ---- */
  let target = +input.value - 1, shown = target, raf = 0, last = 0, idleSince = 0, visible = true;
  const goal = { pos: new THREE.Vector3(), look: new THREE.Vector3() };
  function frame(t) {
    raf = 0;
    const dt = last ? Math.min((t - last) / 1000, 0.1) : 0.016;
    last = t;
    const full = motion() === 'full';
    const k = full ? 1 - Math.exp(-dt * 7) : 1;
    pointer.x += (pointer.tx - pointer.x) * (full ? k : 1);
    pointer.y += (pointer.ty - pointer.y) * (full ? k : 1);
    if (!full) { pointer.x = pointer.y = 0; }
    let jf = null;
    if (journey) {
      Js += (J - Js) * k;
      if (Math.abs(J - Js) < 0.0005) Js = J;
      if (Js > 0) {
        jf = journeyAt(Js, goal);
        target = shown = jf;                                    // so the page picks up here when the journey ends
        offset(1 - smooth(Math.min(Js / DIVE, 1)));
        const v = Math.min(n, Math.round(jf) + 1);              // the slider follows
        if (v !== +input.value) { input.value = v; input.dispatchEvent(new Event('input', { bubbles: true })); }
      }
    }
    if (jf === null) {
      shown += (target - shown) * k;
      if (Math.abs(target - shown) < 0.002) shown = target;
      aim(shown, goal);
    }
    if (!cam.ready || !full) { cam.pos.copy(goal.pos); cam.look.copy(goal.look); cam.ready = true; }
    else { cam.pos.lerp(goal.pos, k); cam.look.lerp(goal.look, k); }
    camera.position.copy(cam.pos);
    camera.lookAt(cam.look);
    draw(shown);
    renderer.render(scene, camera);
    if (journey) sayAt(shown, Js);
    if (root.getAttribute('data-lg-scene') !== 'on') {
      root.setAttribute('data-lg-scene', 'on');
      requestAnimationFrame(() => canvas.classList.add('is-on'));
      setJourney();
      place();
    }
    const settled = shown === target && Js === J && cam.pos.distanceTo(goal.pos) < 0.001
      && Math.abs(pointer.tx - pointer.x) < 0.001 && Math.abs(pointer.ty - pointer.y) < 0.001;
    if (!settled) idleSince = t;
    if (visible && t - idleSince < 300) raf = requestAnimationFrame(frame);
    else last = 0;
  }
  function kick() { if (!raf && visible) { idleSince = performance.now(); raf = requestAnimationFrame(frame); } }

  const travelling = () => journey && J > 0 && J < 1;
  fig.addEventListener('lg:show', e => {
    if (travelling()) return;                                   // the journey sends these itself, through the slider
    target = Math.max(0, Math.min(e.detail - 1, n - 1)); kick();
  });

  /* Drag along the scene moves the slider; ledger.js does the rest, as for the slider itself. */
  let drag = null;
  canvas.addEventListener('pointerdown', e => {
    if (travelling()) return;
    drag = { x: e.clientX, v: +input.value, id: e.pointerId };
    canvas.setPointerCapture(e.pointerId);
  });
  canvas.addEventListener('pointerup', () => { drag = null; });
  canvas.addEventListener('pointercancel', () => { drag = null; });
  canvas.addEventListener('pointermove', e => {
    const r = canvas.getBoundingClientRect();
    pointer.tx = ((e.clientX - r.left) / r.width - 0.5) * 2;
    pointer.ty = -((e.clientY - r.top) / r.height - 0.5) * 2;
    if (drag) {
      const v = Math.max(1, Math.min(n, Math.round(drag.v + (e.clientX - drag.x) / (r.width * 0.7) * n)));
      if (v !== +input.value) { input.value = v; input.dispatchEvent(new Event('input', { bubbles: true })); }
    }
    hover(e.clientX - r.left, e.clientY - r.top, r);
    kick();
  });
  canvas.addEventListener('pointerleave', () => { pointer.tx = pointer.ty = 0; if (hovered) { hovered = null; } kick(); });

  /* Hover: the thread nearest the pointer on screen, within 10px, lights; the rest dim. */
  const A = new THREE.Vector3(), B = new THREE.Vector3();
  function hover(mx, my, r) {
    let best = null, bd = 10;
    const edge = zOf(shown) + (shown >= n - 1 ? FRONT : 0.06);
    for (const t of threads) {
      if (t.s > shown) continue;
      const zB = t.state === 'closed' && t.e <= shown ? zOf(t.e) : edge;
      A.set(t.x, t.y, zOf(t.s)).project(camera); B.set(t.x, t.y, zB).project(camera);
      const ax = (A.x + 1) / 2 * r.width, ay = (1 - A.y) / 2 * r.height;
      const bx = (B.x + 1) / 2 * r.width, by = (1 - B.y) / 2 * r.height;
      const dx = bx - ax, dy = by - ay, L = dx * dx + dy * dy || 1;
      const u = Math.max(0, Math.min(1, ((mx - ax) * dx + (my - ay) * dy) / L));
      const dd = Math.hypot(mx - ax - u * dx, my - ay - u * dy);
      if (dd < bd) { bd = dd; best = t; }
    }
    if (best !== hovered) { hovered = best; canvas.style.cursor = best ? 'pointer' : ''; }
  }

  /* The journey: on under Full on a wide screen, once the scene draws; off otherwise. */
  function setJourney() {
    const want = motion() === 'full' && !mqNarrow.matches && root.getAttribute('data-lg-scene') === 'on';
    if (want === journey) return;
    journey = want;
    if (want) {
      runway = document.createElement('div');
      runway.className = 'lg-runway';
      runway.setAttribute('aria-hidden', 'true');
      hero.querySelector('.wrap').appendChild(runway);
      say = document.createElement('div');
      say.className = 'lg-say';
      say.setAttribute('aria-hidden', 'true');
      document.body.appendChild(say);
      root.setAttribute('data-lg-journey', '');
    } else {
      if (runway) runway.remove();
      if (say) say.remove();
      runway = say = null; sayK = -1; J = Js = 0;
      root.removeAttribute('data-lg-journey');
    }
    rise = 0;
    onScroll();
  }

  /* The hero leaving lifts the camera (Full only). With the journey on, the runway's scroll drives it instead. */
  function onScroll() {
    if (journey) {
      const r = runway.getBoundingClientRect(), vh = innerHeight;
      const j = Math.max(0, Math.min(1, (vh * 0.5 - r.top) / Math.max(1, r.height - vh * 0.5)));
      if (j !== J) { J = j; kick(); }
      return;
    }
    const h = canvas.clientHeight || 1;
    const r = motion() === 'full' && !mqNarrow.matches ? Math.max(0, Math.min(1, -hero.getBoundingClientRect().top / (h * 0.85))) : 0;
    if (r !== rise) { rise = r; kick(); }
  }
  addEventListener('scroll', onScroll, { passive: true });

  /* Drawing stops off-screen and in a hidden tab. */
  new IntersectionObserver(es => { visible = es.some(e => e.isIntersecting) && !document.hidden; if (visible) kick(); })
    .observe(canvas);
  document.addEventListener('visibilitychange', () => { visible = !document.hidden; if (visible) kick(); });

  /* The Display panel and the OS: theme, contrast, text size, motion. */
  const restyle = () => { readPalette(); setJourney(); place(); kick(); };
  new MutationObserver(restyle).observe(root, { attributes: true, attributeFilter: ['data-theme', 'data-contrast', 'data-text', 'data-motion'] });
  [mqDark, mqMore].forEach(m => m.addEventListener('change', restyle));
  mqNarrow.addEventListener('change', () => { cam.ready = false; setJourney(); place(); });
  addEventListener('resize', place);
  canvas.addEventListener('webglcontextlost', e => { e.preventDefault(); giveUp('context lost'); });

  readPalette();
  place();
  kick();
}
