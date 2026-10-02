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
     data-lg-wait   on the home page under Full, until ledger.js takes over the
                    draw-in (DESIGN-6; below)
     data-lg-scene  on the home page while the 3D hero loads, "on" once it draws
                    (copy-review-010; below)

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

  /* M2's draw-in (DESIGN-6). ledger.js is deferred, so on a slow load the page
     could paint the whole ledger before ledger.js clips it to 001. On the home
     page under Full, this marks <html> before the first paint, and style.css
     hides the threads while the mark is on. ledger.js clips them and lifts the
     mark in one step. If ledger.js hasn't run after 3 s, the mark lifts here and
     the ledger shows whole, with no draw-in. */
  if (window.tcvMotion() === 'full' && /^\/(index(\.html)?)?$/.test(location.pathname) && 'IntersectionObserver' in window) {
    root.setAttribute('data-lg-wait', '');
    setTimeout(function () { root.removeAttribute('data-lg-wait'); }, 3000);
  }

  /* The 3D hero (copy-review-010). On the home page, where WebGL2 and modules
     exist, this marks <html> before the first paint, and style.css hides the SVG
     pictures so they don't show and then vanish. ledger-scene.js sets the mark to
     "on" once it draws, and removes it if it can't. If it hasn't drawn after 5 s,
     the mark lifts here and the SVGs show. */
  if (/^\/(index(\.html)?)?$/.test(location.pathname) && window.WebGL2RenderingContext
      && 'noModule' in document.createElement('script')) {
    root.setAttribute('data-lg-scene', '');
    setTimeout(function () {
      if (root.getAttribute('data-lg-scene') !== 'on') root.removeAttribute('data-lg-scene');
    }, 5000);
  }

  /* M1, page to page (copy-review-007 §4, Phase 3 step 5). Each page's <head>
     turns on cross-document view transitions (@view-transition, inline since
     DESIGN-5), and style.css names the top bar
     so it holds still while the content cross-fades. Under Full, a case study's
     sub-menu label, clicked, grows into the H1 of the page it opens (the label
     is the H1, a standing rule). Reduced: the cross-fade only. Off: none.
     Browsers without the feature change pages as before. The hooks live here
     because the new page's must be registered before its first paint. */
  var clicked = null;
  function unname() {
    var named = document.querySelectorAll('[style*="view-transition-name"]');
    for (var i = 0; i < named.length; i++) named[i].style.viewTransitionName = '';
  }
  document.addEventListener('click', function (e) {
    clicked = e.target.closest ? e.target.closest('#navsub-work a') : null;
  }, true);
  window.addEventListener('pageshow', function () { clicked = null; unname(); });
  /* A skipped transition (Off, or any other skip once this page has it) rejects
     its promises. Handled here, so such a skip is quiet, not a console error.
     (The live skips of DESIGN-5 happened on the new page before this ran; their
     fix is the inline @view-transition opt-in in each page's head.) */
  function quiet(vt) {
    function none() {}
    vt.ready.catch(none); vt.finished.catch(none); vt.updateCallbackDone.catch(none);
  }
  window.addEventListener('pageswap', function (e) {
    if (!e.viewTransition) return;
    quiet(e.viewTransition);
    var m = window.tcvMotion();
    if (m === 'off') { e.viewTransition.skipTransition(); return; }
    unname();
    if (m === 'full' && clicked && clicked.getClientRects().length) clicked.style.viewTransitionName = 'cs-title';
  });
  window.addEventListener('pagereveal', function (e) {
    if (!e.viewTransition) return;
    quiet(e.viewTransition);
    var m = window.tcvMotion();
    if (m === 'off') { e.viewTransition.skipTransition(); return; }
    var h1 = m === 'full' && /^\/work\//.test(location.pathname) && document.querySelector('main h1');
    if (!h1) return;
    h1.style.viewTransitionName = 'cs-title';
    e.viewTransition.finished.then(unname, unname);
  });
})();
