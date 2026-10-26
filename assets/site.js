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
    var fromSite = !!box.dataset.static;            // actualités déjà publiées dans le site : celles du serveur s'y ajoutent
    if (!fromSite) clear(box); else box.querySelectorAll(".skeleton").forEach(function (n) { n.remove(); });
    if (!data.actualites.length) { if (!fromSite) box.appendChild(el("p", "muted", LABELS.none)); return; }
    data.actualites.forEach(function (n) { box.appendChild(newsCard(n, false)); });
  }

  function renderHomeNews(data) {
    var section = document.getElementById("home-news-section");
    var box = document.getElementById("home-news");
    if (!box) return;
    if (box.dataset.static) return;                 // les actualités du site ont la priorité sur l'accueil
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

  // ---------- Questionnaire « Mon organisation peut-elle adhérer ? » ----------
  var checker = document.querySelector(".checker");
  if (checker) {
    var questions = Array.prototype.map.call(checker.querySelectorAll(".checker-questions li"), function (li) { return li.textContent.trim(); });
    var conditions = Array.prototype.map.call(checker.querySelectorAll(".checker-questions li"), function (li) { return li.dataset.condition; });
    var prepare = Array.prototype.map.call(checker.querySelectorAll(".checker-prepare li"), function (li) { return li.textContent.trim(); });
    var d = checker.dataset, stage = el("div", "checker-stage"), step = 0;
    stage.setAttribute("aria-live", "polite");
    checker.querySelector(".checker-questions").hidden = true;
    checker.appendChild(stage);
    var button = function (label, cls, onClick) { var b = el("button", "btn " + cls, label); b.type = "button"; b.addEventListener("click", onClick); return b; };
    var show = function () {
      clear(stage);
      if (step === 0) {
        var intro = el("div", "cta-row"); intro.appendChild(button(d.start, "dark", function () { step = 1; show(); })); stage.appendChild(intro); return;
      }
      var n = step, total = questions.length;
      var meter = el("div", "meter"); var fill = el("span", "meter-fill"); fill.style.setProperty("--w", ((n - 1) / total * 100) + "%"); meter.appendChild(fill); stage.appendChild(meter);
      stage.appendChild(el("p", "muted", d.progress.replace("{n}", String(n)).replace("{total}", String(total))));
      stage.appendChild(el("h3", "", questions[n - 1]));
      var row = el("div", "cta-row");
      row.appendChild(button(d.yes, "dark", function () { if (n === total) { result(null); } else { step = n + 1; show(); } }));
      row.appendChild(button(d.no, "outline", function () { result(conditions[n - 1]); }));
      stage.appendChild(row);
    };
    var result = function (failed) {
      clear(stage);
      var box = el("div", "checker-result " + (failed ? "ko" : "ok"));
      box.appendChild(el("h3", "", failed ? d.koTitle : d.okTitle));
      if (failed) {
        box.appendChild(el("p", "", d.koText)); box.appendChild(el("p", "strong", failed)); box.appendChild(el("p", "muted", d.koHelp));
        var link = el("a", "btn outline", d.contact); link.href = "contact.html"; var r1 = el("div", "cta-row"); r1.appendChild(link); box.appendChild(r1);
      } else {
        box.appendChild(el("p", "", d.okText));
        var list = el("ul", "check-list dark"); prepare.forEach(function (x) { list.appendChild(el("li", "", x)); }); box.appendChild(list);
        if (d.joinHref) { var go = el("a", "btn", d.join); go.href = d.joinHref; var r2 = el("div", "cta-row"); r2.appendChild(go); box.appendChild(r2); }
      }
      var again = el("div", "cta-row"); again.appendChild(button(d.restart, "outline", function () { step = 1; show(); })); box.appendChild(again);
      stage.appendChild(box);
      var heading = box.querySelector("h3"); if (heading) { heading.setAttribute("tabindex", "-1"); heading.focus({ preventScroll: true }); }
    };
    show();
  }

  // ---------- Organigramme interactif ----------
  var panel = document.getElementById("organ-panel");
  if (panel) {
    var nodes = Array.prototype.slice.call(document.querySelectorAll(".chart .node"));
    var cards = {};
    document.querySelectorAll("[data-organ-card]").forEach(function (c) { cards[c.dataset.organCard] = c; });
    var closePanel = function () {
      panel.hidden = true; clear(panel);
      nodes.forEach(function (n) { n.classList.remove("on"); n.setAttribute("aria-expanded", "false"); });
    };
    var openOrgan = function (node) {
      var key = node.dataset.organ, targetId = node.dataset.target;
      if (key === undefined) {                               // commissions, représentations régionales : on descend vers la section
        var target = document.getElementById(targetId);
        if (target) target.scrollIntoView({ behavior: reduced ? "auto" : "smooth", block: "start" });
        return;
      }
      var card = cards[key];
      if (!card) return;
      var already = node.classList.contains("on");
      closePanel();
      if (already) return;
      node.classList.add("on"); node.setAttribute("aria-expanded", "true");
      var head = el("h3", "", card.querySelector("h3").textContent);
      var close = el("button", "close", "×"); close.type = "button"; close.setAttribute("aria-label", panel.dataset.close); close.addEventListener("click", closePanel);
      var list = el("ul"); card.querySelectorAll("li").forEach(function (li) { list.appendChild(el("li", "", li.textContent)); });
      panel.appendChild(close); panel.appendChild(head); panel.appendChild(list); panel.hidden = false;
    };
    nodes.forEach(function (n) {
      n.setAttribute("role", "button"); n.setAttribute("tabindex", "0"); n.setAttribute("aria-expanded", "false");
      n.addEventListener("click", function () { openOrgan(n); });
      n.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); openOrgan(n); } });
    });
  }

  // ---------- Graphique de répartition (barres animées) ----------
  var bars = document.querySelector(".bars");
  if (bars) {
    var fillBars = function () {
      bars.querySelectorAll("li").forEach(function (li, i) {
        var pct = Math.max(3, Math.round(parseFloat(li.dataset.value) / parseFloat(li.dataset.max) * 100));
        setTimeout(function () { li.querySelector(".bar-fill").style.setProperty("--w", pct + "%"); }, reduced ? 0 : i * 140);
      });
    };
    if ("IntersectionObserver" in window && !reduced) {
      var seen = new IntersectionObserver(function (entries) { if (entries[0].isIntersecting) { fillBars(); seen.disconnect(); } }, { threshold: 0.3 });
      seen.observe(bars);
    } else fillBars();
  }

  // ---------- Centre de transparence : filtres par type et par année ----------
  var tFilters = document.querySelector(".filters");
  if (tFilters) {
    var tState = { kind: "", year: "" }, tCards = Array.prototype.slice.call(document.querySelectorAll("#transp-list [data-kind]"));
    var tGroups = Array.prototype.slice.call(document.querySelectorAll("#transp-list .year-group")), tNone = document.getElementById("transp-none");
    var applyFilters = function () {
      tCards.forEach(function (c) { c.hidden = (tState.kind && c.dataset.kind !== tState.kind) || (tState.year && c.dataset.year !== tState.year); });
      var shown = 0;
      tGroups.forEach(function (g) { var any = g.querySelector("[data-kind]:not([hidden])"); g.hidden = !any; if (any) shown++; });
      if (tNone) tNone.hidden = shown > 0;
    };
    tFilters.querySelectorAll(".chips").forEach(function (group) {
      group.querySelectorAll(".chip").forEach(function (chip) {
        chip.addEventListener("click", function () {
          group.querySelectorAll(".chip").forEach(function (c) { c.classList.remove("on"); c.setAttribute("aria-pressed", "false"); });
          chip.classList.add("on"); chip.setAttribute("aria-pressed", "true");
          tState[group.dataset.filter] = chip.dataset.value;
          applyFilters();
        });
      });
    });
  }

  // ---------- Affiche : impression de la version choisie ----------
  document.querySelectorAll("[data-print]").forEach(function (b) {
    b.addEventListener("click", function () {
      body.dataset.print = b.dataset.print;
      var done = function () { delete body.dataset.print; window.removeEventListener("afterprint", done); };
      window.addEventListener("afterprint", done);
      window.print();
    });
  });

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
      if (window.psieMapFilter) window.psieMapFilter(q, norm);
    });
  }

  // ---------- Carte des DRENA (Leaflet + fond OpenStreetMap, comme la plateforme LECIM) ----------
  var civ = document.getElementById("civ-map");
  if (civ) {
    var rows = Array.prototype.slice.call(document.querySelectorAll("#region-list li"));
    var info = document.getElementById("civ-info");
    var mapFallback = document.getElementById("map-fallback");
    if (!window.L) { if (mapFallback) mapFallback.hidden = false; civ.hidden = true; }
    else {
      var map = L.map(civ, { zoomSnap: 0.25, minZoom: 6, maxZoom: 14, scrollWheelZoom: false, worldCopyJump: false })
        .setView([7.54, -5.55], 6.5);
      map.attributionControl.setPrefix(false);
      L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", { attribution: civ.dataset.attribution || "© OpenStreetMap", maxZoom: 19 }).addTo(map);
      map.setMaxBounds([[2.5, -11.5], [12.5, 0.5]]);       // reste autour de la Côte d'Ivoire
      var tileFail = 0;
      map.eachLayer(function (l) { if (l.on) l.on("tileerror", function () { if (++tileFail === 6 && mapFallback) mapFallback.hidden = false; }); });

      // ctrl + molette (ou pincement du pavé tactile) pour zoomer sans bloquer le défilement de la page
      civ.addEventListener("wheel", function (e) {
        if (!e.ctrlKey && !e.metaKey) return;
        e.preventDefault();
        map.setZoomAround(map.mouseEventToContainerPoint(e), map.getZoom() + clamp(-e.deltaY, -40, 40) * 0.03, { animate: false });
      }, { passive: false });

      var groups = {}, markers = [];                       // une pastille par lieu (Abidjan 1 à 4 = un seul point)
      rows.forEach(function (r) {
        if (r.dataset.lat === "" || r.dataset.lon === "") return;
        var key = r.dataset.lat + "," + r.dataset.lon;
        (groups[key] = groups[key] || { lat: parseFloat(r.dataset.lat), lon: parseFloat(r.dataset.lon), rows: [] }).rows.push(r);
      });
      var style = { radius: 8, color: "#fff", weight: 2, fillColor: "#c9a24b", fillOpacity: 0.95, className: "drena-dot" };
      var activeStyle = { radius: 11, fillColor: "#136b46", color: "#e7cf8e", weight: 3 };
      var activeGroup = null;
      var hideInfo = function () {
        info.hidden = true;
        markers.forEach(function (m) { m.setStyle(style); });
        rows.forEach(function (r) { r.classList.remove("active"); });
        activeGroup = null;
      };
      var showGroup = function (g, fly) {
        clear(info);
        var close = el("button", "close", "×"); close.type = "button"; close.setAttribute("aria-label", LABELS.close);
        close.addEventListener("click", hideInfo); info.appendChild(close);
        g.rows.forEach(function (r) {
          info.appendChild(el("h3", "", r.dataset.drena));
          if (r.dataset.region) info.appendChild(el("p", "muted", r.dataset.region));
          if (r.dataset.delegue) info.appendChild(el("p", "", r.dataset.delegue));
          if (r.dataset.tel) { var a = el("a", "", r.dataset.tel); a.href = "tel:" + r.dataset.tel.replace(/\s+/g, ""); a.dir = "ltr"; var p = el("p"); p.appendChild(a); info.appendChild(p); }
        });
        info.hidden = false;
        markers.forEach(function (m) { m.setStyle(m._group === g ? activeStyle : style); if (m._group === g) m.bringToFront(); });
        rows.forEach(function (r) { r.classList.toggle("active", g.rows.indexOf(r) !== -1); });
        activeGroup = g;
        if (fly) map.flyTo([g.lat, g.lon], Math.max(map.getZoom(), 9), { animate: !reduced, duration: 0.8 });
      };
      Object.keys(groups).forEach(function (k) {
        var g = groups[k];
        var m = L.circleMarker([g.lat, g.lon], style).addTo(map);
        m._group = g; g.marker = m; markers.push(m);
        var label = document.createElement("span");          // nœud DOM : jamais de HTML venant des données
        label.textContent = g.rows.map(function (r) { return r.dataset.drena; }).join(" · ");
        m.bindTooltip(label, { permanent: true, direction: "top", offset: [0, -8], className: "drena-label", interactive: false });
        m.on("click", function () { showGroup(g, false); });
        m.on("keypress", function (e) { if (e.originalEvent && (e.originalEvent.key === "Enter" || e.originalEvent.key === " ")) showGroup(g, true); });
      });
      var showLabels = function () { civ.classList.toggle("show-labels", map.getZoom() >= 8); };
      map.on("zoomend", showLabels); showLabels();
      if (markers.length) map.fitBounds(L.featureGroup(markers).getBounds().pad(0.15));

      rows.forEach(function (r) {
        if (r.dataset.lat === "") return;
        var open = function () {
          var k = r.dataset.lat + "," + r.dataset.lon;
          showGroup(groups[k], true);
          civ.scrollIntoView({ block: "nearest", behavior: reduced ? "auto" : "smooth" });
        };
        r.addEventListener("click", function (e) { if (e.target.tagName !== "A") open(); });
        r.addEventListener("keydown", function (e) { if (e.key === "Enter") open(); });
      });
      // la recherche estompe les pastilles qui ne correspondent pas
      window.psieMapFilter = function (q, norm) {
        markers.forEach(function (m) {
          var hit = !q || m._group.rows.some(function (r) { return norm(r.dataset.q).indexOf(q) !== -1; });
          m.setStyle({ opacity: hit ? 1 : 0.15, fillOpacity: hit ? 0.95 : 0.15 });
          if (m.getTooltip() && m.getTooltip().getElement()) m.getTooltip().getElement().style.opacity = hit ? "" : "0.15";
        });
      };
      map.on("click", function () { /* un clic sur le fond de carte ne ferme pas la fiche */ });
    }
  }

  function fail() {
    document.querySelectorAll(".js-loading, .skeleton").forEach(function (n) { n.remove(); });
    var published = document.querySelector("[data-static]");   // des actualités du site restent affichées
    if (page === "index") { var s = document.getElementById("home-news-section"); if (s && !published) s.hidden = true; return; }
    if (page === "actualites" && published) return;
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
