/* The header that collapses (Thomas, 2026-10-03; rulings in copy-review-012).

   Without this file the top bar is the plain bar every page carries in its HTML,
   and every link works. With it:
   - The bar sticks to the top. On a wide screen, as the page scrolls through its
     first 160px, "Thomas Cheesman" folds into a TC monogram (the other letters
     fall away, the last ones first), the nav folds into one glass Menu button,
     the bar slims and turns to frosted glass, and the page's name shows faintly
     behind it (with the section being read, on a case study or /method). A
     progress line runs along its foot, notched at each section. Scrolling back
     plays it in reverse. On a phone the Menu button is always there, and the
     name becomes the monogram once the page scrolls.
   - Display is a glass button with the accessibility symbol.
   - Menu opens the nav as a glass panel: Esc, a click outside, or Tab past it
     closes it.
   - The Menu button wobbles now and then, and leans like a gimbal: toward the
     pointer on a computer, with the phone's tilt on a phone (an iPhone asks
     first, on the first tap of Menu).
   - A glass "Back to top" button waits at the bottom left once the page has
     scrolled a screen.
   Motion: under Full everything eases (each frame closes 16% of the gap to the
   scroll position, so a stepped wheel glides). Reduced and Off: the bar switches
   between full and slim at once, with no wobble, lean, glide or progress line. */
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

  /* ---- the name, letter by letter ------------------------------------------ */
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
  // the order they fall away in: the last letter of each word first, working in
  var fall = [];
  letters.forEach(function (s, j) {
    if (j === keepT || j === keepC) return;
    var end = j < keepC ? keepC - 1 : name.length - 1;   // the word's last letter (the space counts with Thomas)
    fall.push({ s: s, rank: end - j });
  });
  var maxRank = Math.max.apply(null, fall.map(function (f) { return f.rank; }));
  var widths = [], fullW = 0;
  function measure() {
    fall.forEach(function (f) { f.s.style.maxWidth = ''; });
    widths = fall.map(function (f) { return f.s.getBoundingClientRect().width; });
    fullW = word.getBoundingClientRect().width;
    bar.style.setProperty('--hc-menu-w', menu.offsetWidth + 'px');   // the room Display leaves for Menu
  }
  /* Where the full name doesn't fit beside the buttons (a phone with large text, a very narrow
     screen), it would cover Menu: the bar shows the monogram from the start, and doesn't peek.
     Found 2026-10-03 by site_check at 375px with 200% text. */
  function tight() {
    if (!compact) return false;
    var stop = Math.min(menu.getBoundingClientRect().left, disp ? disp.getBoundingClientRect().left : Infinity);
    return fullW > stop - word.getBoundingClientRect().left - 16;
  }

  /* ---- the buttons ---------------------------------------------------------- */
  var A11Y = '<span class="hc-icon hc-icon--a11y" aria-hidden="true"></span><span class="sr-only">Display</span>';
  if (disp) {
    disp.classList.add('glassbtn', 'glassbtn--icon');
    disp.innerHTML = A11Y;
  }
  nav.id = nav.id || 'site-nav';
  var menu = el('button', 'glassbtn hc-menu',
    '<span class="hc-menu__face"><span class="hc-ink">Menu</span></span>');
  menu.type = 'button';
  menu.setAttribute('aria-expanded', 'false');
  menu.setAttribute('aria-controls', nav.id);
  inner.appendChild(menu);

  var ghost = el('div', 'hc-ghost');
  ghost.setAttribute('aria-hidden', 'true');
  inner.insertBefore(ghost, inner.firstChild);

  var prog = el('div', 'hc-progress', '<span class="hc-progress__bar"></span>');
  prog.setAttribute('aria-hidden', 'true');
  bar.appendChild(prog);
  var progBar = prog.firstChild;

  var top = el('button', 'glassbtn glassbtn--icon hc-top',
    '<span class="hc-icon hc-icon--up" aria-hidden="true"></span><span class="sr-only">Back to top</span>');
  top.type = 'button';
  document.body.appendChild(top);

  /* ---- the page's name, and the section being read -------------------------- */
  var here = nav.querySelector('.navsub__list a[aria-current="page"]') ||
             nav.querySelector('a[aria-current="page"]') || nav.querySelector('a[aria-current="true"]');
  var pageName = here ? here.textContent.trim() : '';
  var sections = Array.prototype.slice.call(document.querySelectorAll('main .cs-section[id]'));
  var notches = sections.map(function () { var n = el('span', 'hc-notch'); prog.appendChild(n); return n; });
  var ghostPage = el('span', 'hc-ghost__page'); ghostPage.textContent = pageName;
  var ghostSec = el('span', 'hc-ghost__sec');
  ghost.appendChild(ghostPage); ghost.appendChild(ghostSec);
  function sectionLabel(k) {
    var num = sections[k].querySelector('.cs-section__num');
    return (k < 9 ? '0' : '') + (k + 1) + ' ' + (num ? num.textContent.trim() : '');
  }
  function placeNotches() {
    var span = document.documentElement.scrollHeight - window.innerHeight;
    sections.forEach(function (sec, k) {
      var y = sec.getBoundingClientRect().top + window.scrollY - bar.offsetHeight;
      notches[k].style.left = (span > 0 ? clamp(y / span) * 100 : 0) + '%';
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
    menu.tabIndex = on ? 0 : -1;
  }
  function paint() {
    var mob = phone.matches;
    fall.forEach(function (f, k) {
      var start = (1 - f.rank / maxRank) * 0.5;   // the end letters go first
      var t = clamp((q - start) / 0.5);
      f.s.style.maxWidth = (widths[k] * (1 - t)).toFixed(2) + 'px';
      f.s.style.opacity = (1 - t).toFixed(3);
    });
    word.toggleAttribute('data-mono', q > 0.85);
    var grow = 1 + 0.45 * clamp((q - 0.5) / 0.5);  // the T and C grow into the monogram
    letters[keepT].style.fontSize = letters[keepC].style.fontSize = grow === 1 ? '' : grow.toFixed(3) + 'em';
    var b = mob ? 1 : p;                          // the bar: a phone is always in its compact form
    bar.style.setProperty('--hc', b.toFixed(4));
    bar.style.setProperty('--hc-name', p.toFixed(4));
    setCompact(mob || p >= 0.5);
    // the reading progress, the notches, the section
    var span = document.documentElement.scrollHeight - window.innerHeight;
    var r = span > 0 ? clamp(window.scrollY / span) : 0;
    progBar.style.transform = 'scaleX(' + r.toFixed(4) + ')';
    var cur = -1;
    sections.forEach(function (sec, k) {
      var on = sec.getBoundingClientRect().top <= bar.offsetHeight + 48;
      notches[k].toggleAttribute('data-on', on);
      if (on) cur = k;
    });
    ghostSec.textContent = cur >= 0 ? sectionLabel(cur) : '';
    top.toggleAttribute('data-show', window.scrollY > window.innerHeight * 0.9);
  }
  function target() { return clamp(window.scrollY / RANGE); }
  function ease(from, to, k) { var v = from + (to - from) * k; return Math.abs(to - v) < 0.002 ? to : v; }
  function tick() {
    raf = 0;
    var t = target();
    var nameTo = function () { return tight() ? 1 : peek ? 0 : p; };
    if (full()) {
      p = ease(p, t, 0.16);
      q = ease(q, nameTo(), 0.2);                 // the name follows the bar, or unfolds for a peek
    } else {
      p = t >= 0.5 ? 1 : 0;                       // Reduced, Off: switch at once
      q = nameTo();
    }
    paint();
    if (full() && (p !== t || q !== nameTo())) raf = requestAnimationFrame(tick);
  }
  function kick() { if (!raf) raf = requestAnimationFrame(tick); }

  /* ---- the menu ------------------------------------------------------------- */
  function openMenu() {
    menuOpen = true; menu.setAttribute('aria-expanded', 'true'); bar.setAttribute('data-menu-open', '');
    askTilt();
  }
  function closeMenu() {
    if (!menuOpen) return;
    menuOpen = false; menu.setAttribute('aria-expanded', 'false'); bar.removeAttribute('data-menu-open');
  }
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

  /* ---- the gimbal and the wobble ------------------------------------------- */
  var tilt = { x: 0, y: 0, vx: 0, vy: 0, tx: 0, ty: 0 }, graf = 0, base = null, asked = false;
  function gimbal() {
    graf = 0;
    if (!full()) { menu.style.removeProperty('--rx'); menu.style.removeProperty('--ry'); return; }
    // a spring: stiff enough to follow, damped enough to settle with a little overshoot
    var k = 0.09, d = 0.78;
    tilt.vx = (tilt.vx + (tilt.tx - tilt.x) * k) * d; tilt.x += tilt.vx;
    tilt.vy = (tilt.vy + (tilt.ty - tilt.y) * k) * d; tilt.y += tilt.vy;
    menu.style.setProperty('--rx', tilt.x.toFixed(2) + 'deg');
    menu.style.setProperty('--ry', tilt.y.toFixed(2) + 'deg');
    if (Math.abs(tilt.vx) + Math.abs(tilt.vy) + Math.abs(tilt.tx - tilt.x) + Math.abs(tilt.ty - tilt.y) > 0.02)
      graf = requestAnimationFrame(gimbal);
  }
  function lean(tx, ty) { tilt.tx = tx; tilt.ty = ty; if (!graf) graf = requestAnimationFrame(gimbal); }
  var fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  if (fine) {
    window.addEventListener('pointermove', function (e) {
      if (!compact || !full()) return;
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
  placeNotches();
  p = full() ? target() : (target() >= 0.5 ? 1 : 0);   // a reload part-way down starts where the page is
  q = p;
  paint();                                        // sets compact, so tight() can be asked
  if (tight()) { q = 1; paint(); }
  window.addEventListener('scroll', kick, { passive: true });
  window.addEventListener('resize', function () { measure(); placeNotches(); kick(); });
  window.addEventListener('load', function () { measure(); placeNotches(); kick(); });
  phone.addEventListener && phone.addEventListener('change', kick);
  new MutationObserver(function () { measure(); placeNotches(); kick(); })
    .observe(root, { attributes: true, attributeFilter: ['data-motion', 'data-text'] });
})();
