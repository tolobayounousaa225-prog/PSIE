// Animations et lecture des données publiques de la PSIE.
// Règle de sécurité : aucune donnée venant du serveur n'est insérée comme HTML (uniquement textContent).
(function () {
  "use strict";
  var root = document.documentElement;
  root.classList.add("js");
  var body = document.body;
  var api = body.dataset.api;
  var lang = body.dataset.lang === "ar" ? "ar" : "fr";
  var page = body.dataset.page;
  var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var LABELS = {
    fr: { fondateur: "Membre fondateur", ordinaire: "Membre ordinaire", honneur: "Membre d'honneur", none: "Aucune actualité pour le moment.", read: "Lire la suite" },
    ar: { fondateur: "عضو مؤسس", ordinaire: "عضو عادي", honneur: "عضو شرف", none: "لا توجد أخبار حاليا.", read: "اقرأ المزيد" }
  }[lang];

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined && text !== null) node.textContent = text;
    return node;
  }
  function pick(obj) { if (!obj) return ""; return obj[lang] || obj[lang === "ar" ? "fr" : "ar"] || ""; }
  function clear(node) { while (node.firstChild) node.removeChild(node.firstChild); }
  function clamp(v, a, b) { return Math.min(b, Math.max(a, v)); }

  // ---------- Animations d'interface ----------
  var header = document.querySelector(".topbar");
  var bar = document.querySelector(".progress");
  var toTop = document.querySelector(".to-top");
  var art = document.querySelector(".hero-art-wrap");
  var timeline = document.querySelector(".timeline");
  var ticking = false;

  function onScroll() {
    ticking = false;
    var y = window.scrollY || window.pageYOffset;
    var max = Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
    if (header) header.classList.toggle("scrolled", y > 24);
    if (bar) root.style.setProperty("--scroll", String(clamp(y / max, 0, 1)));
    if (toTop) toTop.classList.toggle("show", y > 700);
    if (art && !reduced && y < 900) art.style.setProperty("--py", String(Math.round(y * 0.1)));
    if (timeline) {
      var r = timeline.getBoundingClientRect();
      var p = clamp((window.innerHeight * 0.62 - r.top) / Math.max(1, r.height), 0, 1);
      timeline.style.setProperty("--progress", p.toFixed(3));
      var steps = timeline.querySelectorAll(".step");
      steps.forEach(function (s, i) { s.classList.toggle("on", p >= (i + 0.35) / steps.length); });
    }
  }
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  window.addEventListener("resize", onScroll);
  onScroll();

  if (toTop) toTop.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reduced ? "auto" : "smooth" }); });

  // Menu mobile
  var toggle = document.querySelector(".menu-toggle");
  var nav = document.querySelector(".nav");
  if (toggle && nav) {
    var setOpen = function (open) { nav.classList.toggle("open", open); toggle.setAttribute("aria-expanded", open ? "true" : "false"); };
    toggle.addEventListener("click", function (e) { e.stopPropagation(); setOpen(!nav.classList.contains("open")); });
    document.addEventListener("click", function (e) { if (!nav.contains(e.target)) setOpen(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape") setOpen(false); });
    nav.addEventListener("click", function (e) { if (e.target.closest("a")) setOpen(false); });
  }

  // Apparition progressive des éléments (décalage entre frères)
  document.querySelectorAll("[data-stagger]").forEach(function (group) {
    Array.prototype.forEach.call(group.children, function (child, i) { child.style.setProperty("--i", String(i)); });
  });
  var revealItems = document.querySelectorAll("[data-reveal], .chart");
  function countUp(node) {
    var target = parseInt(node.dataset.count, 10);
    if (isNaN(target)) return;
    if (reduced) { node.textContent = String(target); return; }
    var start = null, dur = 1400;
    node.textContent = "0";
    (function frame(ts) {
      if (start === null) start = ts;
      var t = clamp((ts - start) / dur, 0, 1), eased = 1 - Math.pow(1 - t, 4);
      node.textContent = String(Math.round(target * eased));
      if (t < 1) requestAnimationFrame(frame);
    })(performance.now());
  }
  if ("IntersectionObserver" in window && !reduced) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add("in");
        en.target.querySelectorAll("[data-count]").forEach(countUp);
        if (en.target.hasAttribute("data-count")) countUp(en.target);
        io.unobserve(en.target);
      });
    }, { threshold: 0.14, rootMargin: "0px 0px -6% 0px" });
    revealItems.forEach(function (n) { io.observe(n); });
  } else {
    revealItems.forEach(function (n) {
      n.classList.add("in");
      n.querySelectorAll("[data-count]").forEach(function (c) { c.textContent = c.dataset.count; });
    });
  }

  // Relief au survol des cartes (souris uniquement)
  if (!reduced && window.matchMedia && window.matchMedia("(hover: hover)").matches) {
    document.querySelectorAll(".tilt").forEach(function (card) {
      card.addEventListener("mousemove", function (e) {
        var r = card.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5, y = (e.clientY - r.top) / r.height - 0.5;
        card.style.setProperty("--ry", (x * 7).toFixed(2) + "deg");
        card.style.setProperty("--rx", (-y * 7).toFixed(2) + "deg");
      });
      card.addEventListener("mouseleave", function () { card.style.setProperty("--rx", "0deg"); card.style.setProperty("--ry", "0deg"); });
    });
  }

  // Le bouton de langue conserve la page demandée (ex. l'actualité n°3)
  var sw = document.getElementById("lang-switch");
  if (sw && location.search) sw.href = sw.getAttribute("href") + location.search;

  // ---------- Données publiques (membres, actualités) ----------
  function sealClass(base, sigle) { return sigle.length > 6 ? base + " long" : base; }

  function renderMembers(data) {
    var box = document.getElementById("membres-list");
    if (!box || !data.membres.length) return;
    clear(box);
    data.membres.forEach(function (m, i) {
      var tile = el("div", "tile");
      tile.setAttribute("data-reveal", "");
      tile.style.setProperty("--i", String(i % 6));
      tile.appendChild(el("div", sealClass("num", m.sigle), m.sigle));
      if (m.nom && m.nom !== m.sigle) tile.appendChild(el("div", "", m.nom));
      tile.appendChild(el("div", "muted", LABELS[m.categorie] || ""));
      box.appendChild(tile);
      requestAnimationFrame(function () { tile.classList.add("in"); });
    });
  }

  function newsCard(n, short) {
    var card = el("article", "card news-card tilt");
    card.appendChild(el("time", "", n.date));
    card.appendChild(el(short ? "h3" : "h2", "", pick(n.titre)));
    var text = pick(n.contenu);
    var max = short ? 140 : 240;
    card.appendChild(el("p", "", text.length > max ? text.slice(0, max) + "…" : text));
    var link = el("a", "", LABELS.read);
    link.href = "actualite.html?id=" + encodeURIComponent(String(parseInt(n.id, 10)));
    link.appendChild(document.createTextNode(" "));
    var ico = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    ico.setAttribute("class", "icon flip");
    var use = document.createElementNS("http://www.w3.org/2000/svg", "use");
    use.setAttribute("href", "#i-arrow");
    ico.appendChild(use);
    link.appendChild(ico);
    card.appendChild(link);
    return card;
  }

  function renderNewsList(data) {
    var box = document.getElementById("actualites-list");
    if (!box) return;
    clear(box);
    if (!data.actualites.length) { box.appendChild(el("p", "muted", LABELS.none)); return; }
    data.actualites.forEach(function (n) { box.appendChild(newsCard(n, false)); });
  }

  function renderHomeNews(data) {
    var section = document.getElementById("home-news-section");
    var box = document.getElementById("home-news");
    if (!box) return;
    if (!data.actualites.length) { if (section) section.hidden = true; return; }
    clear(box);
    data.actualites.slice(0, 3).forEach(function (n, i) {
      var card = newsCard(n, true);
      card.setAttribute("data-reveal", "");
      card.style.setProperty("--i", String(i));
      box.appendChild(card);
      requestAnimationFrame(function () { card.classList.add("in"); });
    });
  }

  function renderNewsItem(data) {
    var box = document.getElementById("actualite");
    if (!box) return;
    var id = parseInt(new URLSearchParams(location.search).get("id"), 10);
    var item = data.actualites.filter(function (n) { return n.id === id; })[0];
    if (!item) { fail(); box.remove(); return; }
    clear(box);
    box.appendChild(el("h2", "", pick(item.titre)));
    box.appendChild(el("p", "muted", item.date));
    box.appendChild(el("div", "prose", pick(item.contenu)));
  }

  function fail() {
    document.querySelectorAll(".js-loading, .skeleton").forEach(function (n) { n.remove(); });
    if (page === "index") { var s = document.getElementById("home-news-section"); if (s) s.hidden = true; return; }
    var note = document.getElementById("members-note");
    if (page === "membres" && note) { note.hidden = false; return; }   // la liste des fondateurs reste affichée
    var f = document.getElementById("fallback");
    if (f) f.hidden = false;
  }

  if (!api || ["index", "membres", "actualites", "actualite"].indexOf(page) === -1) return;

  var controller = new AbortController();
  var timer = setTimeout(function () { controller.abort(); }, 10000);
  fetch(api + "/api/public/vitrine.json", { signal: controller.signal, credentials: "omit", mode: "cors" })
    .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); })
    .then(function (data) {
      if (!data || !Array.isArray(data.membres) || !Array.isArray(data.actualites)) throw new Error("format");
      if (page === "index") renderHomeNews(data);
      else if (page === "membres") renderMembers(data);
      else if (page === "actualites") renderNewsList(data);
      else renderNewsItem(data);
    })
    .catch(fail)
    .then(function () { clearTimeout(timer); });
})();
