// Charge les membres et actualités depuis l'application et les affiche.
// Aucune donnée n'est insérée comme HTML : tout passe par textContent (pas d'injection possible).
(function () {
  "use strict";
  var body = document.body;
  var api = body.dataset.api;
  var lang = body.dataset.lang === "ar" ? "ar" : "fr";
  var page = body.dataset.page;

  var LABELS = {
    fr: { fondateur: "Membre fondateur", ordinaire: "Membre ordinaire", honneur: "Membre d'honneur",
          none: "Aucune actualité pour le moment.", read: "Lire" },
    ar: { fondateur: "عضو مؤسس", ordinaire: "عضو عادي", honneur: "عضو شرف",
          none: "لا توجد أخبار حاليا.", read: "قراءة" }
  }[lang];

  function el(tag, className, text) {
    var node = document.createElement(tag);
    if (className) node.className = className;
    if (text !== undefined && text !== null) node.textContent = text;
    return node;
  }
  function pick(obj) {            // texte dans la langue de la page, à défaut dans l'autre
    if (!obj) return "";
    return obj[lang] || obj[lang === "ar" ? "fr" : "ar"] || "";
  }
  function clear(node) { while (node.firstChild) node.removeChild(node.firstChild); }
  function fail() {
    var f = document.getElementById("fallback");
    if (f) f.hidden = false;
    document.querySelectorAll(".js-loading").forEach(function (n) { n.remove(); });
  }

  function renderMembers(data) {
    var box = document.getElementById("membres-list");
    if (!box) return;
    clear(box);
    data.membres.forEach(function (m) {
      var tile = el("div", "tile");
      tile.appendChild(el("div", "num", m.sigle));
      if (m.nom && m.nom !== m.sigle) tile.appendChild(el("div", "", m.nom));
      tile.appendChild(el("div", "muted", LABELS[m.categorie] || ""));
      box.appendChild(tile);
    });
  }

  function renderNewsList(data) {
    var box = document.getElementById("actualites-list");
    if (!box) return;
    clear(box);
    if (!data.actualites.length) { box.appendChild(el("p", "muted", LABELS.none)); return; }
    data.actualites.forEach(function (n) {
      var card = el("article", "card");
      card.appendChild(el("h2", "", pick(n.titre)));
      card.appendChild(el("p", "muted", n.date));
      var text = pick(n.contenu);
      card.appendChild(el("p", "", text.length > 240 ? text.slice(0, 240) + "…" : text));
      var link = el("a", "", LABELS.read);
      link.href = "actualite.html?id=" + encodeURIComponent(String(parseInt(n.id, 10)));
      card.appendChild(link);
      box.appendChild(card);
    });
  }

  function renderNewsItem(data) {
    var box = document.getElementById("actualite");
    if (!box) return;
    var id = parseInt(new URLSearchParams(location.search).get("id"), 10);
    var item = data.actualites.filter(function (n) { return n.id === id; })[0];
    if (!item) { fail(); box.remove(); return; }
    clear(box);
    box.appendChild(el("h1", "", pick(item.titre)));
    box.appendChild(el("p", "muted", item.date));
    box.appendChild(el("div", "prose", pick(item.contenu)));
  }

  // Le bouton de langue conserve la page demandée (ex. l'actualité n°3)
  var sw = document.getElementById("lang-switch");
  if (sw && location.search) sw.href = sw.getAttribute("href") + location.search;

  if (!api || ["membres", "actualites", "actualite"].indexOf(page) === -1) return;

  var controller = new AbortController();
  var timer = setTimeout(function () { controller.abort(); }, 10000);
  fetch(api + "/api/public/vitrine.json", { signal: controller.signal, credentials: "omit", mode: "cors" })
    .then(function (r) { if (!r.ok) throw new Error("HTTP " + r.status); return r.json(); })
    .then(function (data) {
      if (!data || !Array.isArray(data.membres) || !Array.isArray(data.actualites)) throw new Error("format");
      if (page === "membres") renderMembers(data);
      else if (page === "actualites") renderNewsList(data);
      else renderNewsItem(data);
    })
    .catch(fail)
    .then(function () { clearTimeout(timer); });
})();
