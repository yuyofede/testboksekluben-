/* Grimstad Bokseklubb – felles skript */
(function () {
  "use strict";

  /* Header: solid background after scrolling ------------------------------- */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-scrolled", window.scrollY > 40);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* Mobile navigation ------------------------------------------------------ */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    var setNav = function (open) {
      toggle.setAttribute("aria-expanded", String(open));
      nav.classList.toggle("is-open", open);
      document.documentElement.style.overflow = open ? "hidden" : "";
    };

    toggle.addEventListener("click", function () {
      setNav(toggle.getAttribute("aria-expanded") !== "true");
    });

    nav.addEventListener("click", function (event) {
      if (event.target.closest("a")) setNav(false);
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && nav.classList.contains("is-open")) {
        setNav(false);
        toggle.focus();
      }
    });
  }

  /* Current year ----------------------------------------------------------- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* Reveal on scroll ------------------------------------------------------- */
  var revealItems = document.querySelectorAll("[data-reveal]");
  if (revealItems.length) {
    if ("IntersectionObserver" in window) {
      var observer = new IntersectionObserver(
        function (entries) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add("is-visible");
              observer.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.12, rootMargin: "0px 0px -50px 0px" }
      );
      revealItems.forEach(function (el) {
        observer.observe(el);
      });
    } else {
      revealItems.forEach(function (el) {
        el.classList.add("is-visible");
      });
    }
  }

  /* Lightbox --------------------------------------------------------------- */
  var dialog = document.getElementById("lightbox");
  var triggers = Array.prototype.slice.call(
    document.querySelectorAll("[data-lightbox]")
  );

  if (dialog && triggers.length) {
    var lbImage = dialog.querySelector("[data-lightbox-image]");
    var lbCaption = dialog.querySelector("[data-lightbox-caption]");
    var prevBtn = dialog.querySelector("[data-lightbox-prev]");
    var nextBtn = dialog.querySelector("[data-lightbox-next]");
    var current = 0;

    var render = function (index) {
      current = (index + triggers.length) % triggers.length;
      var trigger = triggers[current];
      var src = trigger.getAttribute("data-full");
      var caption = trigger.getAttribute("data-caption") || "";
      if (src) lbImage.src = src;
      lbImage.alt = trigger.getAttribute("data-alt") || caption;
      lbCaption.textContent = caption;
      var counter = dialog.querySelector("[data-lightbox-count]");
      if (counter) {
        counter.textContent =
          current + 1 + " / " + triggers.length;
      }
    };

    var open = function (index) {
      render(index);
      if (typeof dialog.showModal === "function") {
        dialog.showModal();
      } else {
        dialog.setAttribute("open", "");
      }
      document.documentElement.style.overflow = "hidden";
    };

    var close = function () {
      if (typeof dialog.close === "function") {
        dialog.close();
      } else {
        dialog.removeAttribute("open");
      }
      document.documentElement.style.overflow = "";
    };

    triggers.forEach(function (trigger, index) {
      trigger.addEventListener("click", function () {
        open(index);
      });
    });

    dialog.addEventListener("close", function () {
      document.documentElement.style.overflow = "";
    });

    dialog.addEventListener("click", function (event) {
      if (event.target === dialog) close();
    });

    dialog.querySelectorAll("[data-lightbox-close]").forEach(function (btn) {
      btn.addEventListener("click", close);
    });

    if (prevBtn) {
      prevBtn.addEventListener("click", function () {
        render(current - 1);
      });
    }
    if (nextBtn) {
      nextBtn.addEventListener("click", function () {
        render(current + 1);
      });
    }

    dialog.addEventListener("keydown", function (event) {
      if (event.key === "ArrowLeft") {
        event.preventDefault();
        render(current - 1);
      }
      if (event.key === "ArrowRight") {
        event.preventDefault();
        render(current + 1);
      }
    });
  }

  /* Contact form: opens the visitor's e-mail client ------------------------ */
  var form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      if (!form.reportValidity()) return;

      var data = new FormData(form);
      var lang = form.getAttribute("data-lang") || "no";
      var labels =
        lang === "en"
          ? { subject: "Website enquiry", name: "Name", email: "E-mail", phone: "Phone", topic: "Topic", message: "Message" }
          : { subject: "Henvendelse fra nettsiden", name: "Navn", email: "E-post", phone: "Telefon", topic: "Gjelder", message: "Melding" };

      var lines = [];
      ["name", "email", "phone", "topic", "message"].forEach(function (key) {
        var value = (data.get(key) || "").toString().trim();
        if (value) lines.push(labels[key] + ": " + value);
      });

      var subject =
        (data.get("topic") || labels.subject).toString() + " – " + (data.get("name") || "");
      var href =
        "mailto:grimstadbk@gmail.com?subject=" +
        encodeURIComponent(subject) +
        "&body=" +
        encodeURIComponent(lines.join("\n"));

      window.location.href = href;

      var status = form.querySelector("[data-form-status]");
      if (status) {
        status.textContent =
          lang === "en"
            ? "Your e-mail app should open now. You can also write to grimstadbk@gmail.com."
            : "E-postprogrammet ditt åpnes nå. Du kan også skrive til grimstadbk@gmail.com.";
      }
    });
  }
})();
