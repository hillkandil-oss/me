/* BeepWear — front-end behaviors. Progressive enhancement only. */
(function () {
  "use strict";

  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Reveal-on-scroll: fade + rise, once, for elements marked .bw-reveal.
  function initReveal() {
    var items = document.querySelectorAll(".bw-reveal");
    if (!items.length) return;
    if (reduce || !("IntersectionObserver" in window)) {
      items.forEach(function (el) { el.classList.add("is-in"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.1 });
    items.forEach(function (el) { io.observe(el); });
  }

  if (document.readyState !== "loading") initReveal();
  else document.addEventListener("DOMContentLoaded", initReveal);
})();
