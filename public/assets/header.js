/* The header that collapses (Thomas, 2026-10-03; rulings in copy-review-012).

   Without this file the top bar is the plain bar every page carries in its HTML,
   and every link works. With it the header is only the name, the nav and the
   Display button, floating over the page with no fill and no rule:
   - Behind it, once the page scrolls, the page's name shows faintly (with the
     section being read, on a case study or /method). No label words.
   - Wide, at the top: the name, then Projects, Method, Background and Contact
     as smoked-glass pills, then Display (the accessibility symbol).
   - As the page scrolls through its first 160px: "Thomas Cheesman" folds into a
     TC monogram (the other letters fall away, each word's last letters first)
     and the pills fold into one Menu pill, left of Display. Scrolling back plays
     it in reverse. Hovering or focusing the monogram unfolds the name.
   - On a phone, or wherever the pills don't fit beside the name, Menu is always
     there; the name becomes the monogram once the page scrolls, or from the
     start where the full name wouldn't fit beside the buttons.
   - Menu opens the nav as a panel: Esc, a click outside, or Tab past it closes
     it. Menu leans like a gimbal: toward the pointer on a computer, with the
     phone's tilt on a phone (an iPhone asks first, on the first tap of Menu).
     It doesn't wobble (Thomas dropped that, 2026-10-03).
   - Folded, the header sits on a slab: a 3D bar that faces the pointer (or
     tilts with a phone), its surface lit like sunshine on the light theme and
     moonlight on the dark, the light sliding as it turns.
   - A glass "Back to top" button waits at the bottom left once the page has
     scrolled a screen.
   Motion: under Full everything eases (each frame closes 16% of the gap to the
   scroll position, so a stepped wheel glides). Reduced and Off: the header
   switches between its two forms at once, with no lean. */
(function () {
  var root = document.documentElement;
  var bar = document.querySelector('.topbar');
  var inner = bar && bar.querySelector('.topbar__inner');
  var word = bar && bar.querySelector('.wordmark');
  var nav = bar && bar.querySelector('nav');
  var disp = bar && bar.querySelector('.display__toggle');
  if (!bar || !inner || !word || !nav || !window.requestAnimationFrame) return;

  var RANGE = 160;                                  // px of scroll over which the sequence plays
  var phone = window.matchMedia('(max-width: 45em)');
  function full() { return window.tcvMotion && window.tcvMotion() === 'full'; }
  function clamp(x) { return x < 0 ? 0 : x > 1 ? 1 : x; }
  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html) e.innerHTML = html;
    return e;
  }

  /* ---- the name, letter by letter -------------------------------------------
     At rest the letters flow as ordinary text (inline), so the name keeps the
     font's own spacing; only while the name folds are they boxes that can
     narrow (data-folding). Widths are measured once the fonts have loaded. */
  var name = word.textContent;
  word.setAttribute('aria-label', name);
  word.textContent = '';
  var letters = [], keepT = 0, keepC = name.indexOf('C');
  for (var i = 0; i < name.length; i++) {
    var s = el('span', 'hc-l');
    s.textContent = name.charAt(i) === ' ' ? ' ' : name.charAt(i);
    s.setAttribute('aria-hidden', 'true');
    if (i === keepT || i === keepC) s.classList.add('hc-l--keep');
    word.appendChild(s);
    letters.push(s);
  }
  var fall = [];                                    // the last letter of each word first, working in
  letters.forEach(function (s, j) {
    if (j === keepT || j === keepC) return;
    var end = j < keepC ? keepC - 1 : name.length - 1;
    fall.push({ s: s, rank: end - j });
  });
  var maxRank = Math.max.apply(null, fall.map(function (f) { return f.rank; }));
  var widths = [], fullW = 0, navW = 0;

  /* ---- the buttons ---------------------------------------------------------- */
  if (disp) {
    disp.classList.add('glassbtn', 'glassbtn--icon');
    disp.innerHTML = '<span class="hc-icon hc-icon--a11y" aria-hidden="true"></span><span class="sr-only">Display</span>';
  }
  // the nav's own links become pills: their words in the metal lettering
  Array.prototype.forEach.call(nav.querySelectorAll(':scope > a, :scope > .navsub > a'), function (a) {
    a.innerHTML = '<span class="hc-ink">' + a.innerHTML + '</span>';
  });
  nav.id = nav.id || 'site-nav';
  var menu = el('button', 'glassbtn hc-menu', '<span class="hc-ink">Menu</span>');
  menu.type = 'button';
  menu.setAttribute('aria-expanded', 'false');
  menu.setAttribute('aria-controls', nav.id);
  inner.insertBefore(menu, disp || null);           // Menu, then Display at the far right

  /* the page's name, faint, behind the header; with the section being read */
  var ghost = el('div', 'hc-ghost');
  ghost.setAttribute('aria-hidden', 'true');
  inner.insertBefore(ghost, inner.firstChild);
  var here = nav.querySelector('.navsub__list a[aria-current="page"]') ||
             nav.querySelector('a[aria-current="page"]') || nav.querySelector('a[aria-current="true"]');
  var ghostPage = el('span', 'hc-ghost__page'); ghostPage.textContent = here ? here.textContent.trim() : '';
  var ghostSec = el('span', 'hc-ghost__sec');
  ghost.appendChild(ghostPage); ghost.appendChild(ghostSec);
  var sections = Array.prototype.slice.call(document.querySelectorAll('main .cs-section[id]'));
  function sectionLabel(k) {
    var num = sections[k].querySelector('.cs-section__num');
    return (k < 9 ? '0' : '') + (k + 1) + ' ' + (num ? num.textContent.trim() : '');
  }

  var top = el('button', 'glassbtn glassbtn--icon hc-top',
    '<span class="hc-icon hc-icon--up" aria-hidden="true"></span><span class="sr-only">Back to top</span>');
  top.type = 'button';
  document.body.appendChild(top);

  function measure() {
    word.removeAttribute('data-folding');
    fall.forEach(function (f) { f.s.style.maxWidth = ''; f.s.style.opacity = ''; });
    word.setAttribute('data-folding', '');          // measure each letter as the box it will be
    widths = fall.map(function (f) { return f.s.getBoundingClientRect().width; });
    word.removeAttribute('data-folding');
    fullW = word.getBoundingClientRect().width;
    if (!bar.hasAttribute('data-compact')) navW = nav.getBoundingClientRect().width;
  }
  /* Where the full name doesn't fit beside the buttons it would cover them: the monogram shows from
     the start, and doesn't peek (found 2026-10-03 by site_check at 375px with 200% text). */
  function tight() {
    if (!compact) return false;
    return fullW > menu.getBoundingClientRect().left - word.getBoundingClientRect().left - 16;
  }
  /* Where the four pills don't fit beside the full name and Display, the bar is compact from the start. */
  function narrow() {
    var room = inner.clientWidth - parseFloat(getComputedStyle(inner).paddingLeft) * 2;
    return fullW + navW + (disp ? disp.offsetWidth : 0) + 48 > room;
  }

  /* While the name folds, each letter paints its own slice of the teal gradient, placed where the whole
     name's would be (style.css says why). Layout positions, not screen ones: the slab under the name turns. */
  function slices() {
    var w = word.clientWidth + 'px', h = word.clientHeight + 'px';
    var at = letters.map(function (s) { return [-s.offsetLeft + 'px', -s.offsetTop + 'px']; });
    if (word.style.getPropertyValue('--wm-w') !== w) word.style.setProperty('--wm-w', w);
    if (word.style.getPropertyValue('--wm-h') !== h) word.style.setProperty('--wm-h', h);
    letters.forEach(function (s, k) {
      if (s.style.getPropertyValue('--l-x') !== at[k][0]) s.style.setProperty('--l-x', at[k][0]);
      if (s.style.getPropertyValue('--l-y') !== at[k][1]) s.style.setProperty('--l-y', at[k][1]);
    });
  }

  /* ---- state ---------------------------------------------------------------- */
  var p = 0, q = 0, raf = 0, peek = false, compact = null, menuOpen = false;   // p: the bar; q: the name
  root.setAttribute('data-hc', '');
  bar.setAttribute('data-hc', '');

  function setCompact(on) {
    if (on === compact) return;
    compact = on;
    if (on) bar.setAttribute('data-compact', ''); else { bar.removeAttribute('data-compact'); closeMenu(); }
    if (slab) face(slab.tx, slab.ty);              // level the slab when it goes (set up further down)
    menu.tabIndex = on ? 0 : -1;
    menu.setAttribute('aria-hidden', on ? 'false' : 'true');
  }
  function paint() {
    var always = phone.matches || narrow();
    var folding = q > 0.001;
    word.toggleAttribute('data-folding', folding);
    fall.forEach(function (f, k) {
      if (!folding) { f.s.style.maxWidth = ''; f.s.style.opacity = ''; return; }
      var t = clamp((q - (1 - f.rank / maxRank) * 0.5) / 0.5);   // the end letters go first
      f.s.style.maxWidth = (widths[k] * (1 - t)).toFixed(2) + 'px';
      f.s.style.opacity = (1 - t).toFixed(3);
    });
    word.toggleAttribute('data-mono', q > 0.85);
    var grow = 1 + 0.45 * clamp((q - 0.5) / 0.5);  // the T and C grow into the monogram
    letters[keepT].style.fontSize = letters[keepC].style.fontSize = grow === 1 ? '' : grow.toFixed(3) + 'em';
    if (folding) slices();
    var b = always ? 1 : p;
    bar.style.setProperty('--hc', b.toFixed(4));
    bar.style.setProperty('--hc-name', p.toFixed(4));
    var cur = -1;
    sections.forEach(function (sec, k) { if (sec.getBoundingClientRect().top <= bar.offsetHeight + 48) cur = k; });
    ghostSec.textContent = cur >= 0 ? sectionLabel(cur) : '';
    setCompact(always || p >= 0.5);
    top.toggleAttribute('data-show', window.scrollY > window.innerHeight * 0.9);
  }
  function target() { return clamp(window.scrollY / RANGE); }
  function ease(from, to, k) { var v = from + (to - from) * k; return Math.abs(to - v) < 0.002 ? to : v; }
  function nameTo() { return tight() ? 1 : peek ? 0 : p; }
  function tick() {
    raf = 0;
    var t = target();
    if (full()) { p = ease(p, t, 0.16); q = ease(q, nameTo(), 0.2); }
    else { p = t >= 0.5 ? 1 : 0; q = nameTo(); }   // Reduced, Off: switch at once
    paint();
    if (full() && (p !== t || q !== nameTo())) raf = requestAnimationFrame(tick);
  }
  function kick() { if (!raf) raf = requestAnimationFrame(tick); }
  function remeasure() { measure(); paint(); kick(); }

  /* ---- the menu ------------------------------------------------------------- */
  function openMenu() {
    menuOpen = true; menu.setAttribute('aria-expanded', 'true'); bar.setAttribute('data-menu-open', '');
    askTilt();
  }
  function closeMenu() {
    if (!menuOpen) return;
    menuOpen = false; menu.setAttribute('aria-expanded', 'false'); bar.removeAttribute('data-menu-open');
  }
  menu.addEventListener('click', function () { face(slab.tx, slab.ty); });   // hold still while the menu is open
  menu.addEventListener('click', function () { if (menuOpen) closeMenu(); else openMenu(); });
  bar.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && menuOpen && !(e.target.closest && e.target.closest('.navsub[data-open]'))) {
      closeMenu(); menu.focus();
    }
  });
  document.addEventListener('click', function (e) {
    if (menuOpen && !nav.contains(e.target) && !menu.contains(e.target)) closeMenu();
  });
  document.addEventListener('focusin', function (e) {
    if (menuOpen && !nav.contains(e.target) && !menu.contains(e.target)) closeMenu();
  });

  /* ---- back to top ---------------------------------------------------------- */
  top.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: full() ? 'smooth' : 'auto' });
    word.focus({ preventScroll: true });
  });

  /* ---- the peek ------------------------------------------------------------- */
  ['mouseenter', 'focus'].forEach(function (ev) { word.addEventListener(ev, function () { peek = true; kick(); }); });
  ['mouseleave', 'blur'].forEach(function (ev) { word.addEventListener(ev, function () { peek = false; kick(); }); });

  /* ---- the gimbal ----------------------------------------------------------- */
  var tilt = { x: 0, y: 0, vx: 0, vy: 0, tx: 0, ty: 0 }, graf = 0, base = null, asked = false;
  function gimbal() {
    graf = 0;
    if (!full()) { menu.style.removeProperty('--rx'); menu.style.removeProperty('--ry'); return; }
    var k = 0.09, d = 0.78;                         // a spring that follows, then settles with a little overshoot
    tilt.vx = (tilt.vx + (tilt.tx - tilt.x) * k) * d; tilt.x += tilt.vx;
    tilt.vy = (tilt.vy + (tilt.ty - tilt.y) * k) * d; tilt.y += tilt.vy;
    menu.style.setProperty('--rx', tilt.x.toFixed(2) + 'deg');
    menu.style.setProperty('--ry', tilt.y.toFixed(2) + 'deg');
    if (Math.abs(tilt.vx) + Math.abs(tilt.vy) + Math.abs(tilt.tx - tilt.x) + Math.abs(tilt.ty - tilt.y) > 0.02)
      graf = requestAnimationFrame(gimbal);
  }
  function lean(tx, ty) { tilt.tx = tx; tilt.ty = ty; if (!graf) graf = requestAnimationFrame(gimbal); }

  /* the slab: it turns to face the pointer, a few degrees, on its own spring; still while the menu is open */
  var slab = { x: 0, y: 0, vx: 0, vy: 0, tx: 0, ty: 0 }, sraf = 0;
  function slabTurn() {
    sraf = 0;
    if (!full()) { ['--bx', '--by', '--lx', '--ly'].forEach(function (v) { inner.style.removeProperty(v); }); return; }
    var on = compact && !menuOpen ? 1 : 0, k = 0.06, d = 0.82;
    slab.vx = (slab.vx + (slab.tx * on - slab.x) * k) * d; slab.x += slab.vx;
    slab.vy = (slab.vy + (slab.ty * on - slab.y) * k) * d; slab.y += slab.vy;
    inner.style.setProperty('--bx', slab.x.toFixed(3) + 'deg');
    inner.style.setProperty('--by', slab.y.toFixed(3) + 'deg');
    inner.style.setProperty('--lx', (35 - slab.y * 9).toFixed(2) + '%');   // the light slides as it turns
    inner.style.setProperty('--ly', (-20 + slab.x * 7).toFixed(2) + '%');
    if (Math.abs(slab.vx) + Math.abs(slab.vy) + Math.abs(slab.tx * on - slab.x) + Math.abs(slab.ty * on - slab.y) > 0.005)
      sraf = requestAnimationFrame(slabTurn);
  }
  function face(tx, ty) { slab.tx = tx; slab.ty = ty; if (!sraf) sraf = requestAnimationFrame(slabTurn); }
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  if (fine) {
    window.addEventListener('pointermove', function (e) {
      if (!compact || !full()) return;
      var br = inner.getBoundingClientRect();     // the slab faces the pointer: below it, it tips down; to a side, it turns
      face(Math.max(-6, Math.min(6, (e.clientY - (br.top + br.height / 2)) / 500 * 6)),
           Math.max(-2.5, Math.min(2.5, -(e.clientX - (br.left + br.width / 2)) / 700 * 2.5)));
      var r = menu.getBoundingClientRect(), dx = e.clientX - (r.left + r.width / 2), dy = e.clientY - (r.top + r.height / 2);
      var reach = Math.max(0, 1 - Math.hypot(dx, dy) / 360);       // only within 360px of the button
      lean(-dy / 360 * 22 * reach, dx / 360 * 22 * reach);
    }, { passive: true });
  }
  function onTilt(e) {
    if (e.beta == null || !full()) return;
    if (!base) base = { b: e.beta, g: e.gamma };                   // the way the phone was held at first
    var lim = function (v) { return Math.max(-18, Math.min(18, v)); };
    lean(lim((e.beta - base.b) * 0.6), lim((e.gamma - base.g) * 0.6));
    face(Math.max(-6, Math.min(6, (e.beta - base.b) * 0.25)), Math.max(-4, Math.min(4, -(e.gamma - base.g) * 0.2)));
  }
  function listenTilt() { window.addEventListener('deviceorientation', onTilt); }
  function askTilt() {          // an iPhone asks the reader once, from a tap; others just send it
    if (asked || fine) return;
    asked = true;
    var D = window.DeviceOrientationEvent;
    if (D && typeof D.requestPermission === 'function') {
      D.requestPermission().then(function (s) { if (s === 'granted') listenTilt(); }, function () {});
    }
  }
  if (!fine && window.DeviceOrientationEvent && typeof window.DeviceOrientationEvent.requestPermission !== 'function') listenTilt();

  /* ---- go ------------------------------------------------------------------- */
  measure();
  p = full() ? target() : (target() >= 0.5 ? 1 : 0);   // a reload part-way down starts where the page is
  q = p;
  paint();                                        // sets compact, so tight() can be asked
  if (tight()) { q = 1; paint(); }
  window.addEventListener('scroll', kick, { passive: true });
  window.addEventListener('resize', remeasure);
  window.addEventListener('load', remeasure);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(remeasure);
  phone.addEventListener && phone.addEventListener('change', remeasure);
  new MutationObserver(remeasure).observe(root, { attributes: true, attributeFilter: ['data-motion', 'data-text'] });
})();
