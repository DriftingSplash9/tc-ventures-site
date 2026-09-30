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
   under the key prefs.js reads before the next page is drawn. */
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
        if (o[0]) { prefs[g.key] = o[0]; root.setAttribute('data-' + g.key, o[0]); }
        else { delete prefs[g.key]; root.removeAttribute('data-' + g.key); }
        save(prefs);
      });
      row.appendChild(input);
      row.appendChild(label);
    });
    set.appendChild(row);
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
