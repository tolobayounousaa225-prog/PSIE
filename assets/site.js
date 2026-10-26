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
    fr: { fondateur: "Membre fondateur", ordinaire: "Membre ordinaire", honneur: "Membre d'honneur", none: "Aucune actualité pour le moment.", read: "Lire la suite", close: "Fermer" },
    ar: { fondateur: "عضو مؤسس", ordinaire: "عضو عادي", honneur: "عضو شرف", none: "لا توجد أخبار حاليا.", read: "اقرأ المزيد", close: "إغلاق" }
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
    // les fiches des faîtières (liens) restent affichées ; on ajoute seulement les membres inconnus de la liste statique
    var known = {};
    box.querySelectorAll(".num").forEach(function (n) { known[n.textContent.trim().toUpperCase()] = true; });
    data.membres.forEach(function (m, i) {
      if (known[String(m.sigle).trim().toUpperCase()]) return;
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

  // Chiffre « organisations fondatrices » lu sur l'application (valeur validée : entier raisonnable)
  function renderLiveStats(data) {
    var n = data.membres.filter(function (m) { return m.categorie === "fondateur"; }).length;
    var first = document.querySelector(".stat .num");
    if (first && Number.isInteger(n) && n > 0 && n < 1000) { first.dataset.count = String(n); first.textContent = String(n); }
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

  // ---------- Bandeau d'annonce (fermable pour la session) ----------
  var announce = document.querySelector(".announce");
  if (announce) {
    var stored = null;
    try { stored = sessionStorage.getItem("psie-annonce"); } catch (e) { /* stockage indisponible : on affiche */ }
    var text = announce.textContent.trim();
    if (stored !== text) {
      announce.hidden = false;
      body.classList.add("has-announce");
      announce.querySelector(".announce-close").addEventListener("click", function () {
        announce.hidden = true;
        body.classList.remove("has-announce");
        try { sessionStorage.setItem("psie-annonce", text); } catch (e) { /* ignoré */ }
      });
    }
  }

  // ---------- Galerie : visionneuse ----------
  var lightbox = document.querySelector(".lightbox");
  if (lightbox) {
    var lbImg = lightbox.querySelector("img"), lbCap = lightbox.querySelector("figcaption");
    var shots = Array.prototype.slice.call(document.querySelectorAll(".shot")), current = -1, opener = null;
    var show = function (i) {
      current = (i + shots.length) % shots.length;
      lbImg.src = shots[current].dataset.full;
      lbImg.alt = shots[current].dataset.caption || "";
      lbCap.textContent = shots[current].dataset.caption || "";
    };
    var close = function () { lightbox.hidden = true; document.body.classList.remove("no-scroll"); if (opener) opener.focus(); };
    shots.forEach(function (b, i) {
      b.addEventListener("click", function () { opener = b; show(i); lightbox.hidden = false; document.body.classList.add("no-scroll"); lightbox.querySelector(".lb-close").focus(); });
    });
    lightbox.querySelector(".lb-close").addEventListener("click", close);
    lightbox.addEventListener("click", function (e) { if (e.target === lightbox) close(); });
    document.addEventListener("keydown", function (e) {
      if (lightbox.hidden) return;
      if (e.key === "Escape") close();
      else if (e.key === "ArrowRight") show(current + (lang === "ar" ? -1 : 1));
      else if (e.key === "ArrowLeft") show(current + (lang === "ar" ? 1 : -1));
    });
  }

  // ---------- Représentations régionales : recherche ----------
  var search = document.getElementById("region-search");
  if (search) {
    var items = Array.prototype.slice.call(document.querySelectorAll("#region-list li"));
    var count = document.getElementById("region-count");
    var tpl = count.dataset.template;
    var norm = function (v) { return v.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, ""); };
    search.addEventListener("input", function () {
      var q = norm(search.value.trim()), n = 0;
      items.forEach(function (li) { var ok = !q || norm(li.dataset.q).indexOf(q) !== -1; li.hidden = !ok; if (ok) n++; });
      count.textContent = tpl.replace("{n}", String(n));
      document.querySelectorAll(".civ-map .pin").forEach(function (c) { c.classList.toggle("dim", !!q && norm(c.dataset.name).indexOf(q) === -1); });
    });
  }

  // ---------- Carte interactive : zoom, déplacement, fiche au clic ----------
  var civ = document.getElementById("civ-map");
  if (civ) {
    var W = parseFloat(civ.dataset.w), H = parseFloat(civ.dataset.h);
    var vp = civ.querySelector(".viewport");
    var pins = Array.prototype.slice.call(civ.querySelectorAll(".pin"));
    var rows = Array.prototype.slice.call(document.querySelectorAll("#region-list li"));
    var info = document.getElementById("civ-info");
    var MAXZ = 8, view = { s: 1, x: 0, y: 0 }, anim = null, active = null;

    var clampView = function (v) {
      v.s = clamp(v.s, 1, MAXZ);
      v.x = clamp(v.x, W * (1 - v.s), 0);
      v.y = clamp(v.y, H * (1 - v.s), 0);
      return v;
    };
    var paint = function () {
      vp.setAttribute("transform", "translate(" + view.x.toFixed(2) + " " + view.y.toFixed(2) + ") scale(" + view.s.toFixed(3) + ")");
      var r = (6 / view.s).toFixed(2);          // les points gardent la même taille à l'écran
      pins.forEach(function (c) { c.setAttribute("r", c.classList.contains("active") ? String(r * 1.4) : r); });
    };
    var go = function (target) {
      target = clampView(target);
      if (anim) cancelAnimationFrame(anim);
      if (reduced) { view = target; paint(); return; }
      var from = { s: view.s, x: view.x, y: view.y }, t0 = performance.now(), dur = 380;
      var step = function (now) {
        var k = clamp((now - t0) / dur, 0, 1), e = 1 - Math.pow(1 - k, 3);
        view = { s: from.s + (target.s - from.s) * e, x: from.x + (target.x - from.x) * e, y: from.y + (target.y - from.y) * e };
        paint();
        if (k < 1) anim = requestAnimationFrame(step); else anim = null;
      };
      anim = requestAnimationFrame(step);
    };
    var factor = function () { var b = civ.getBoundingClientRect(); return { k: W / b.width, left: b.left, top: b.top }; };
    var zoomAt = function (cx, cy, ns, animate) {         // (cx, cy) en coordonnées de la carte
      ns = clamp(ns, 1, MAXZ);
      var px = (cx - view.x) / view.s, py = (cy - view.y) / view.s;
      var target = { s: ns, x: cx - px * ns, y: cy - py * ns };
      if (animate) go(target); else { view = clampView(target); paint(); }
    };
    var centre = function (px, py, ns) {                  // amène le point (px, py) au centre
      go({ s: ns, x: W / 2 - px * ns, y: H / 2 - py * ns });
    };

    document.querySelectorAll(".map-tools button").forEach(function (b) {
      b.addEventListener("click", function () {
        var a = b.dataset.map;
        if (a === "reset") { go({ s: 1, x: 0, y: 0 }); hideInfo(); }
        else zoomAt(W / 2, H / 2, view.s * (a === "in" ? 1.6 : 1 / 1.6), true);
      });
    });

    // molette : seulement avec Ctrl / pincement du pavé tactile, pour ne pas bloquer le défilement de la page
    civ.addEventListener("wheel", function (e) {
      if (!e.ctrlKey && !e.metaKey) return;
      e.preventDefault();
      var f = factor();
      zoomAt((e.clientX - f.left) * f.k, (e.clientY - f.top) * f.k, view.s * Math.exp(-clamp(e.deltaY, -40, 40) * 0.01), false);
    }, { passive: false });
    civ.addEventListener("dblclick", function (e) {
      if (e.target.classList && e.target.classList.contains("pin")) return;
      var f = factor();
      zoomAt((e.clientX - f.left) * f.k, (e.clientY - f.top) * f.k, view.s * 1.8, true);
    });

    // glisser (souris ou doigt) et pincement (deux doigts)
    var pts = {}, drag = null, pinch = null, moved = false;
    civ.addEventListener("pointerdown", function (e) {
      pts[e.pointerId] = { x: e.clientX, y: e.clientY };
      var ids = Object.keys(pts);
      moved = false;
      if (ids.length === 1) drag = { x: e.clientX, y: e.clientY, vx: view.x, vy: view.y };
      else if (ids.length === 2) {
        var a = pts[ids[0]], b = pts[ids[1]];
        pinch = { d: Math.hypot(a.x - b.x, a.y - b.y), s: view.s }; drag = null;
      }
    });
    civ.addEventListener("pointermove", function (e) {
      if (!pts[e.pointerId]) return;
      pts[e.pointerId] = { x: e.clientX, y: e.clientY };
      var ids = Object.keys(pts), f = factor();
      if (ids.length >= 2 && pinch) {
        var a = pts[ids[0]], b = pts[ids[1]], d = Math.hypot(a.x - b.x, a.y - b.y);
        zoomAt(((a.x + b.x) / 2 - f.left) * f.k, ((a.y + b.y) / 2 - f.top) * f.k, pinch.s * d / pinch.d, false);
        moved = true;
      } else if (drag) {
        var dx = e.clientX - drag.x, dy = e.clientY - drag.y;
        if (!moved && Math.hypot(dx, dy) < 4) return;
        if (!moved) { moved = true; civ.classList.add("dragging"); try { civ.setPointerCapture(e.pointerId); } catch (err) { /* ignoré */ } }
        view = clampView({ s: view.s, x: drag.vx + dx * f.k, y: drag.vy + dy * f.k });
        paint();
      }
    });
    var release = function (e) {
      delete pts[e.pointerId];
      if (Object.keys(pts).length < 2) pinch = null;
      if (!Object.keys(pts).length) { drag = null; civ.classList.remove("dragging"); }
    };
    civ.addEventListener("pointerup", release);
    civ.addEventListener("pointercancel", release);
    civ.addEventListener("lostpointercapture", release);

    // clavier : flèches = déplacer, + / - = zoomer, 0 = recentrer
    civ.addEventListener("keydown", function (e) {
      if (e.target !== civ) return;
      var step = 30, handled = true;
      if (e.key === "ArrowLeft") go({ s: view.s, x: view.x + step, y: view.y });
      else if (e.key === "ArrowRight") go({ s: view.s, x: view.x - step, y: view.y });
      else if (e.key === "ArrowUp") go({ s: view.s, x: view.x, y: view.y + step });
      else if (e.key === "ArrowDown") go({ s: view.s, x: view.x, y: view.y - step });
      else if (e.key === "+" || e.key === "=") zoomAt(W / 2, H / 2, view.s * 1.6, true);
      else if (e.key === "-") zoomAt(W / 2, H / 2, view.s / 1.6, true);
      else if (e.key === "0") go({ s: 1, x: 0, y: 0 });
      else handled = false;
      if (handled) e.preventDefault();
    });

    // fiche d'un point : toutes les DRENA situées au même endroit (ex. Abidjan 1 à 4)
    var hideInfo = function () {
      info.hidden = true;
      pins.forEach(function (c) { c.classList.remove("active"); });
      rows.forEach(function (r) { r.classList.remove("active"); });
      active = null; paint();
    };
    var showInfo = function (i, zoom) {
      var row = rows[i];
      if (!row || !row.dataset.x) return;
      var x = row.dataset.x, y = row.dataset.y;
      var same = rows.filter(function (r) { return r.dataset.x === x && r.dataset.y === y; });
      clear(info);
      var close = el("button", "close", "×"); close.type = "button"; close.setAttribute("aria-label", info.dataset.close || "×");
      close.addEventListener("click", hideInfo); info.appendChild(close);
      same.forEach(function (r) {
        info.appendChild(el("h3", "", r.dataset.drena));
        if (r.dataset.region) info.appendChild(el("p", "muted", r.dataset.region));
        if (r.dataset.delegue) info.appendChild(el("p", "", r.dataset.delegue));
        if (r.dataset.tel) { var a = el("a", "", r.dataset.tel); a.href = "tel:" + r.dataset.tel.replace(/\s+/g, ""); a.dir = "ltr"; var p = el("p"); p.appendChild(a); info.appendChild(p); }
      });
      info.hidden = false;
      pins.forEach(function (c) { c.classList.toggle("active", c.getAttribute("cx") === x && c.getAttribute("cy") === y); });
      rows.forEach(function (r) { r.classList.toggle("active", r.dataset.x === x && r.dataset.y === y); });
      active = i; paint();
      if (zoom) centre(parseFloat(x), parseFloat(y), Math.max(view.s, 3.2));
    };
    pins.forEach(function (c) {
      c.addEventListener("click", function () { if (!moved) showInfo(parseInt(c.dataset.i, 10), false); });
      c.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); showInfo(parseInt(c.dataset.i, 10), true); } });
    });
    rows.forEach(function (r) {
      if (!r.dataset.x) return;
      var open = function () { showInfo(parseInt(r.dataset.i, 10), true); civ.scrollIntoView({ block: "nearest", behavior: reduced ? "auto" : "smooth" }); };
      r.addEventListener("click", function (e) { if (e.target.tagName !== "A") open(); });
      r.addEventListener("keydown", function (e) { if (e.key === "Enter") open(); });
    });
    info.dataset.close = (LABELS.close || "×");
    paint();
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
      if (page === "index") { renderHomeNews(data); renderLiveStats(data); }
      else if (page === "membres") renderMembers(data);
      else if (page === "actualites") renderNewsList(data);
      else renderNewsItem(data);
    })
    .catch(fail)
    .then(function () { clearTimeout(timer); });
})();
