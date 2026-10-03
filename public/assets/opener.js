/* The opener's settle (SP-A; made visible 2026-10-03, Thomas: "1-4 yes").
   On a case study, under Full, as the page scrolls through the first 70% of a
   screen, the opening picture settles from 1.2 times its size (the Bare Your
   Rare excerpt from 1.08) with a parallax drift, and the meta strip rises in
   behind it. It follows the scroll with easing (each frame closes 14% of the
   gap), so a mouse wheel that scrolls in steps still moves it smoothly, and it
   stops drawing once settled. Reduced, Off, and no script: the picture in
   place, still. prefs.js sets the starting pose before the first paint
   (data-opener on <html>), so the picture never jumps when this arrives. */
(function () {
  var root = document.documentElement;
  var frame = document.querySelector('.cs-opener__frame');
  if (!frame || !frame.firstElementChild || !window.requestAnimationFrame) {
    root.removeAttribute('data-opener');
    return;
  }
  var pic = frame.firstElementChild;
  var meta = document.querySelector('.cs-opener ~ .cs-head__meta');
  var grow = frame.parentNode.classList.contains('excerpt') ? 0.08 : 0.2;
  var cur = 0, raf = 0;

  function full() { return window.tcvMotion && window.tcvMotion() === 'full'; }
  function target() { return Math.min(1, Math.max(0, window.scrollY / (window.innerHeight * 0.7))); }
  function paint(c) {
    var e = 1 - c;
    pic.style.transform = 'translateY(' + (-30 * grow * e).toFixed(3) + '%) scale(' + (1 + grow * e).toFixed(4) + ')';
    if (meta) meta.style.transform = 'translateY(' + (32 * e).toFixed(2) + 'px)';
  }
  function clear() {
    pic.style.transform = '';
    if (meta) meta.style.transform = '';
  }
  function tick() {
    raf = 0;
    if (!full()) { clear(); return; }
    var t = target();
    cur += (t - cur) * 0.14;
    if (Math.abs(t - cur) < 0.0005) cur = t;
    paint(cur);
    if (cur !== t) raf = requestAnimationFrame(tick);
  }
  function kick() { if (!raf) raf = requestAnimationFrame(tick); }

  cur = target();                 // a reload part-way down starts where the page is
  if (full()) paint(cur); else clear();
  root.setAttribute('data-opener', 'on');   // the inline pose has taken over from prefs.js's
  window.addEventListener('scroll', kick, { passive: true });
  window.addEventListener('resize', kick);
  // the Display panel changes data-motion on <html>: follow it at once
  new MutationObserver(kick).observe(root, { attributes: true, attributeFilter: ['data-motion'] });
})();
