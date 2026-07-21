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

  // Announcement bar: rotate messages. Frozen (shows first only) if reduced-motion.
  function initAnnounce() {
    var bar = document.querySelector(".bw-announce");
    if (!bar) return;
    var msgs = bar.querySelectorAll(".bw-announce__msg");
    if (msgs.length < 2 || reduce) return;
    var speed = (parseInt(bar.getAttribute("data-speed"), 10) || 4) * 1000;
    var i = 0;
    setInterval(function () {
      msgs[i].classList.remove("is-active");
      i = (i + 1) % msgs.length;
      msgs[i].classList.add("is-active");
    }, speed);
  }

  function init() { initReveal(); initAnnounce(); }
  if (document.readyState !== "loading") init();
  else document.addEventListener("DOMContentLoaded", init);
})();
