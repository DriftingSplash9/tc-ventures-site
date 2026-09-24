/* Primary nav: the Projects sub-menu (the case studies).

   The list works without this file: CSS shows it on hover and while keyboard
   focus is inside it, and /projects links to every case study. This file turns
   it into a disclosure (the WAI-ARIA disclosure navigation pattern): the
   button opens and closes it, Esc closes it and puts focus back on the button,
   and it closes when focus or a click goes somewhere else. With a mouse,
   hovering opens it too, and a click on the button then keeps it open. */
(function () {
  var hover = window.matchMedia && window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  Array.prototype.forEach.call(document.querySelectorAll('.navsub'), function (sub) {
    var btn = sub.querySelector('.navsub__toggle');
    var list = sub.querySelector('.navsub__list');
    if (!btn || !list) return;

    var pinned = false;   // opened by a click or a key, not only by hover
    var timer = 0;

    function isOpen() { return btn.getAttribute('aria-expanded') === 'true'; }
    function open(pin) {
      clearTimeout(timer);
      btn.setAttribute('aria-expanded', 'true');
      sub.setAttribute('data-open', '');
      if (pin) pinned = true;
    }
    function close() {
      clearTimeout(timer);
      btn.setAttribute('aria-expanded', 'false');
      sub.removeAttribute('data-open');
      pinned = false;
    }

    sub.setAttribute('data-enhanced', '');

    btn.addEventListener('click', function () {
      if (isOpen() && pinned) close();
      else open(true);
    });

    sub.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isOpen()) { close(); btn.focus(); }
    });

    sub.addEventListener('focusout', function (e) {
      if (!sub.contains(e.relatedTarget)) close();
    });

    document.addEventListener('click', function (e) {
      if (isOpen() && !sub.contains(e.target)) close();
    });

    if (hover) {
      sub.addEventListener('mouseenter', function () {
        if (isOpen()) clearTimeout(timer); else open(false);
      });
      sub.addEventListener('mouseleave', function () {
        if (!pinned) timer = setTimeout(close, 250);
      });
    }
  });
})();
