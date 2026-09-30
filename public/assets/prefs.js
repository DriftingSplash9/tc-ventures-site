/* Display settings, applied before the first paint (copy-review-007, Phase 3).

   Loaded without defer in every page's <head>, so it runs before the page is
   drawn. It reads the reader's choices from this browser's localStorage and
   marks <html> with them; the CSS reads the marks. No choice means System: no
   mark, and the OS settings decide through plain CSS, as they do with
   JavaScript off. Nothing is sent anywhere.

     data-motion    full | reduced | off
     data-theme     light | dark
     data-contrast  standard | more
     data-text      large | larger

   display.js (the panel) writes the same key. If storage is blocked, every
   page falls back to the OS settings. */
(function () {
  var KEY = 'tcv-display';
  var ALLOWED = {
    motion: ['full', 'reduced', 'off'],
    theme: ['light', 'dark'],
    contrast: ['standard', 'more'],
    text: ['large', 'larger']
  };
  var root = document.documentElement;
  var saved = {};
  try { saved = JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { saved = {}; }
  for (var k in ALLOWED) {
    if (ALLOWED[k].indexOf(saved[k]) !== -1) root.setAttribute('data-' + k, saved[k]);
  }

  /* The motion level in effect, for scripts that animate (the 3D graph).
     Under System, the OS's "reduce motion" means Reduced (Q-P3-2 A). */
  window.tcvMotion = function () {
    var m = root.getAttribute('data-motion');
    if (m) return m;
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'reduced' : 'full';
  };
})();
