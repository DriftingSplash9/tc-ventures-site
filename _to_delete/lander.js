/* ==========================================================================
   lander.js  —  tc-ventures.ca

   Loads the Godot web build into /lander.html on demand.

   Why an iframe and not the engine's own loader wired into this page:
   the Godot export ships its own index.html, loader JS, .wasm and .pck as a
   set that expects to own the document. Dropping the exported folder in
   untouched and pointing an iframe at it means an engine upgrade is a folder
   swap, not a re-integration — and it keeps the game's canvas from fighting
   this page for the window.

   Same rule as the graph demo: nothing downloads until the button is
   pressed. The build is tens of megabytes and nobody should get it by
   scrolling past.
   ========================================================================== */
(function () {
  'use strict';

  var BUILD = '/lander/index.html';

  var mount = document.getElementById('lander-demo');
  if (!mount) return;

  var btn = mount.querySelector('.gd__load');
  var stage = mount.querySelector('.gd__stage');
  var panel = mount.querySelector('.gd__panel');
  /* The still is optional: until there is a screenshot of the build worth
     showing, the frame is just dark ground with the button on it. */
  var still = mount.querySelector('.gd__still');
  if (!btn || !stage || !panel) return;

  /* WebGL is the hard requirement — the build is GL Compatibility, which is
     WebGL 2 in a browser. Without it there is nothing to offer, so say so
     rather than handing over a button that cannot work. */
  var webgl = (function () {
    try {
      var c = document.createElement('canvas');
      return !!(window.WebGL2RenderingContext && c.getContext('webgl2'));
    } catch (e) { return false; }
  })();

  function say(html) { panel.innerHTML = '<p class="gd__hint">' + html + '</p>'; }

  if (!webgl) {
    say('This browser does not have WebGL 2, which the build needs to draw ' +
        'anything. The writing below is the part worth reading anyway.');
    return;
  }

  /* The page ships before the build does. Rather than showing a button that
     404s, ask the server whether the export is actually there — a HEAD on one
     small HTML file, not the thirty-megabyte part — and only offer the button
     if it is. The day the folder is uploaded, the button appears on its own. */
  fetch(BUILD, { method: 'HEAD' }).then(function (r) {
    if (r.ok) {
      btn.hidden = false;
    } else {
      say('The build is not uploaded yet. The writing below is the part worth ' +
          'reading in the meantime, and this page will offer the game the ' +
          'moment there is one to offer.');
    }
  }).catch(function () {
    say('The build is not uploaded yet. The writing below is the part worth ' +
        'reading in the meantime.');
  });

  btn.addEventListener('click', function () {
    btn.disabled = true;
    btn.textContent = 'Loading…';

    var frame = document.createElement('iframe');
    frame.src = BUILD;
    frame.title = 'Rocket Lander';
    /* allow-same-origin is required: the engine needs storage for its own
       state, and the build is first-party anyway. No allow-top-navigation,
       no allow-popups — a game has no business moving the page. */
    frame.setAttribute('sandbox', 'allow-scripts allow-same-origin allow-pointer-lock');
    frame.setAttribute('allow', 'fullscreen; autoplay');
    frame.loading = 'eager';

    frame.addEventListener('load', function () {
      if (still) still.hidden = true;
      btn.hidden = true;
      stage.hidden = false;
      say('Click inside once to give it the keyboard. <kbd>R</kbd> restarts, ' +
          '<kbd>&#96;</kbd> opens the 38 knobs. If you land it, I would like ' +
          'to hear how.');
      /* Hand it the keyboard straight away; the click that loaded it was on
         the button, so focus is still out here. */
      try { frame.contentWindow.focus(); } catch (e) { /* cross-origin, ignore */ }
    });

    frame.addEventListener('error', function () {
      btn.hidden = true;
      say('The build did not load. It is a large file and a slow connection ' +
          'can time out; a reload usually fixes it.');
    });

    stage.appendChild(frame);
  });
})();
