/* M3, the method loop (copy-review-007, Phase 3; ruled "A" 2026-09-30).

   On /method, the first time the working-loop diagram is half in view, it
   traces itself once: each step and the arrow after it light up in the loop's
   order, brief to next session, then the dashed arrow runs back to the brief.
   style.css does the motion (the .is-tracing block); this file only says when.

   Nothing is hidden before it runs: without this file the diagram is as it
   always was. Under Motion Reduced and Off it never runs (style.css also
   multiplies every time by --move, and Off stops all animation). */
(function () {
  var fig = document.querySelector('.loop--files');
  if (!fig || !window.tcvMotion || !('IntersectionObserver' in window)) return;
  if (window.tcvMotion() !== 'full') return;
  var io = new IntersectionObserver(function (entries) {
    if (!entries.some(function (e) { return e.isIntersecting; })) return;
    io.disconnect();
    if (window.tcvMotion() === 'full') fig.classList.add('is-tracing');
  }, { threshold: 0.5 });
  io.observe(fig);
})();
