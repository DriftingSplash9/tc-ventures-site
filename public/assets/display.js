/* The Display panel (copy-review-007, Phase 3): motion, theme, contrast and
   text size. Each starts at System, the reader's own OS setting.

   The button is in every page's top bar, and CSS shows it only when scripts
   run: without JavaScript the panel couldn't do anything, and the OS settings
   still apply through CSS. This file builds the panel once, right after the
   button, as a disclosure like the Projects sub-menu: the button opens and
   closes it, Esc closes it and puts focus back on the button, and it closes
   when focus or a click goes somewhere else. It overlays the page; nothing
   below it moves.

   A choice takes effect at once (the mark on <html> changes) and is saved
   under the key prefs.js reads before the next page is drawn.

   TP-B (copy-review-013, ruled 2026-10-03): each change shows itself. Under Motion
   Full, a new theme sweeps out from the Display button as a growing circle, More
   or Standard contrast wipes across, and a new text size zooms through: one
   same-document view transition each, with <html> marked data-vt while it runs
   (CSS stands the bar's own transition names down, so the page changes as one).
   Under Reduced, a cross-fade. Under Off, or without view transitions, at once.
   The Motion row carries a small sample (aria-hidden) that moves as the setting
   says: it runs under Full, breathes under Reduced, and is still under Off. */
(function () {
  var KEY = 'tcv-display';
  /* The words: copy-review-007, DP1 to DP3. '' is System (no mark). */
  var GROUPS = [
    { key: 'motion', legend: 'Motion', options: [['', 'System'], ['full', 'Full'], ['reduced', 'Reduced'], ['off', 'Off']] },
    { key: 'theme', legend: 'Theme', options: [['', 'System'], ['light', 'Light'], ['dark', 'Dark']] },
    { key: 'contrast', legend: 'Contrast', options: [['', 'System'], ['standard', 'Standard'], ['more', 'More']] },
    { key: 'text', legend: 'Text size', options: [['', 'Standard'], ['large', 'Large'], ['larger', 'Larger']] }
  ];
  var NOTE = 'Saved in this browser only.';

  var root = document.documentElement;
  var btn = document.querySelector('.display__toggle');
  if (!btn) return;

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; }
  }
  function save(prefs) {
    try { localStorage.setItem(KEY, JSON.stringify(prefs)); } catch (e) { /* this page still changes */ }
  }

  var SHOW = { theme: 'sweep', contrast: 'wipe', text: 'zoom' };
  function motion() { return window.tcvMotion ? window.tcvMotion() : 'full'; }
  function clear() { root.removeAttribute('data-vt'); }
  /* Make a change inside a view transition that shows it (or at once). */
  function show(key, done) {
    var kind = SHOW[key], m = motion();
    if (!kind || m === 'off' || !document.startViewTransition) { done(); return; }
    if (m !== 'full') kind = 'fade';
    root.setAttribute('data-vt', kind);
    var t;
    try { t = document.startViewTransition(done); } catch (e) { clear(); done(); return; }
    t.ready.then(function () { animate(kind); }, function () {});
    t.finished.then(clear, clear);
  }
  function animate(kind) {
    var r = btn.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
    var R = Math.hypot(Math.max(x, innerWidth - x), Math.max(y, innerHeight - y));
    var NEW = '::view-transition-new(root)', OLD = '::view-transition-old(root)';
    if (kind === 'sweep') {
      root.animate({ clipPath: ['circle(0px at ' + x + 'px ' + y + 'px)', 'circle(' + R + 'px at ' + x + 'px ' + y + 'px)'] },
        { duration: 750, easing: 'cubic-bezier(0.65, 0, 0.25, 1)', fill: 'both', pseudoElement: NEW });
    } else if (kind === 'wipe') {
      root.animate({ clipPath: ['inset(0 0 0 100%)', 'inset(0 0 0 0)'] },
        { duration: 600, easing: 'cubic-bezier(0.65, 0, 0.25, 1)', fill: 'both', pseudoElement: NEW });
    } else if (kind === 'zoom') {
      root.animate({ opacity: [1, 0], transform: ['scale(1)', 'scale(1.035)'] },
        { duration: 420, easing: 'ease-in', fill: 'both', pseudoElement: OLD });
      root.animate({ opacity: [0, 1], transform: ['scale(0.97)', 'scale(1)'] },
        { duration: 560, easing: 'cubic-bezier(0.2, 0.8, 0.2, 1)', fill: 'both', pseudoElement: NEW });
    }
  }

  var prefs = load();
  var panel = document.createElement('div');
  panel.className = 'display__panel';
  panel.id = btn.getAttribute('aria-controls');
  panel.hidden = true;

  GROUPS.forEach(function (g) {
    var set = document.createElement('fieldset');
    var legend = document.createElement('legend');
    legend.textContent = g.legend;
    set.appendChild(legend);
    var row = document.createElement('div');
    row.className = 'display__options';
    g.options.forEach(function (o) {
      var input = document.createElement('input');
      input.type = 'radio';
      input.name = 'display-' + g.key;
      input.value = o[0];
      input.id = 'display-' + g.key + '-' + (o[0] || 'system');
      input.checked = (prefs[g.key] || '') === o[0];
      var label = document.createElement('label');
      label.htmlFor = input.id;
      label.textContent = o[1];
      input.addEventListener('change', function () {
        show(g.key, function () {
          if (o[0]) { prefs[g.key] = o[0]; root.setAttribute('data-' + g.key, o[0]); }
          else { delete prefs[g.key]; root.removeAttribute('data-' + g.key); }
          save(prefs);                              // inside: a view transition makes the change a frame later
        });
      });
      row.appendChild(input);
      row.appendChild(label);
    });
    set.appendChild(row);
    if (g.key === 'motion') {                     // the sample: it moves as the setting says
      var sample = document.createElement('span');
      sample.className = 'display__sample';
      sample.setAttribute('aria-hidden', 'true');
      sample.appendChild(document.createElement('i'));
      set.appendChild(sample);
    }
    panel.appendChild(set);
  });
  var note = document.createElement('p');
  note.className = 'display__note';
  note.textContent = NOTE;
  panel.appendChild(note);
  btn.parentNode.insertBefore(panel, btn.nextSibling);
  btn.setAttribute('data-enhanced', '');

  function isOpen() { return btn.getAttribute('aria-expanded') === 'true'; }
  function open() { btn.setAttribute('aria-expanded', 'true'); panel.hidden = false; }
  function close() { btn.setAttribute('aria-expanded', 'false'); panel.hidden = true; }

  btn.addEventListener('click', function () { if (isOpen()) close(); else open(); });
  [btn, panel].forEach(function (el) {
    el.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isOpen()) { close(); btn.focus(); }
    });
  });
  document.addEventListener('focusin', function (e) {
    if (isOpen() && !btn.contains(e.target) && !panel.contains(e.target)) close();
  });
  document.addEventListener('click', function (e) {
    if (isOpen() && !btn.contains(e.target) && !panel.contains(e.target)) close();
  });
})();
