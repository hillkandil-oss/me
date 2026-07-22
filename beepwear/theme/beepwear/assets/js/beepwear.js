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

  // Mobile navigation drawer: toggle, a11y, ESC, overlay + link close, scroll lock.
  function initMobileNav() {
    var btn = document.getElementById("bw-burger");
    var nav = document.getElementById("bw-mobile-nav");
    if (!btn || !nav) return;
    var panel = nav.querySelector(".bw-mobile-nav__panel");
    var lastFocus = null;

    function open() {
      lastFocus = document.activeElement;
      nav.hidden = false;
      // next frame so the transition runs from the hidden state
      requestAnimationFrame(function () {
        nav.classList.add("is-open");
        document.body.classList.add("bw-nav-open");
      });
      btn.setAttribute("aria-expanded", "true");
      btn.setAttribute("aria-label", "Close menu");
      var first = panel && panel.querySelector("a");
      if (first) first.focus();
      document.addEventListener("keydown", onKey);
    }
    function close() {
      nav.classList.remove("is-open");
      document.body.classList.remove("bw-nav-open");
      btn.setAttribute("aria-expanded", "false");
      btn.setAttribute("aria-label", "Open menu");
      document.removeEventListener("keydown", onKey);
      var done = function () { nav.hidden = true; nav.removeEventListener("transitionend", done); };
      if (reduce) { nav.hidden = true; } else { nav.addEventListener("transitionend", done); }
      if (lastFocus && lastFocus.focus) lastFocus.focus();
    }
    function onKey(e) { if (e.key === "Escape" || e.keyCode === 27) close(); }

    btn.addEventListener("click", function () {
      if (nav.classList.contains("is-open")) close(); else open();
    });
    // Close when clicking the dimmed overlay (outside the panel).
    nav.addEventListener("click", function (e) { if (e.target === nav) close(); });
    // Close after choosing a destination.
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") close();
    });
  }

  // Add a subtle shadow/background to the sticky header once scrolled.
  function initHeaderScroll() {
    var header = document.querySelector(".bw-site-header");
    if (!header) return;
    var ticking = false;
    function update() {
      header.classList.toggle("is-scrolled", window.scrollY > 8);
      ticking = false;
    }
    window.addEventListener("scroll", function () {
      if (!ticking) { window.requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  }

  function init() { initReveal(); initAnnounce(); initMobileNav(); initHeaderScroll(); }
  if (document.readyState !== "loading") init();
  else document.addEventListener("DOMContentLoaded", init);
})();
