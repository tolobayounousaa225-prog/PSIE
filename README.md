# PSIE — site vitrine

Site public de la **Plateforme des Structures Islamiques d'Éducation**, en français et en arabe
(lecture droite-gauche), publié gratuitement sur **GitHub Pages**.

Le site est entièrement statique. Il ne contient **aucune donnée sensible** : les membres et les
actualités sont lus à chaque visite sur l'application (hébergée sur un serveur à part), qui expose
uniquement des informations publiques. Le code de l'application est dans un autre dépôt.

```
Ce dépôt  ──►  GitHub Pages  (https://tolobayounousaa225-prog.github.io/PSIE/  puis  https://VOTRE-DOMAINE)
                    │  lit membres et actualités (lecture seule, sans cookie)
                    ▼
Application ──►  Serveur Hostinger  (connexion, adhésion, suivi, QR codes, espace interne)
```

> **Adresse actuelle du site : https://tolobayounousaa225-prog.github.io/PSIE/** (arabe : `/PSIE/ar/`).
> Attention aux **majuscules** : le nom du dépôt est repris tel quel dans l'adresse, `/psie/` en minuscules donne une erreur 404.

## Mettre le site en ligne (une seule fois)

1. Dans ce dépôt : **Settings → Pages → Build and deployment → Source : GitHub Actions**.
2. **Settings → Secrets and variables → Actions → onglet Variables → New repository variable**, puis créer :

   | Variable | Valeur | Quand |
   |---|---|---|
   | `API_BASE` | adresse de l'application, ex. `https://app.exemple.org` | dès que le serveur est en ligne |
   | `APP_URL` | idem (laisser vide si identique à `API_BASE`) | facultatif |
   | `CUSTOM_DOMAIN` | ex. `psie-ci.org` | quand le nom de domaine est choisi |
   | `GOATCOUNTER` | ex. `psie` | facultatif : code de votre compte GoatCounter (statistiques de visite sans cookies, voir ci-dessous) |
   | `SITE_URL` | ex. `https://psie-ci.org` | facultatif : adresse publique (sitemap, SEO). Par défaut : l'adresse GitHub Pages |

   Tant qu'elles ne sont pas définies, le site se publie quand même : les boutons « Adhérer » et
   « Connexion » sont alors absents ou inactifs, et les membres/actualités affichent un message
   « momentanément indisponible ».
3. Fusionner une modification dans `main` : le site se construit et se publie tout seul
   (onglet **Actions** pour suivre). L'adresse apparaît ensuite dans **Settings → Pages**.

## Brancher le nom de domaine (plus tard)

1. Définir la variable `CUSTOM_DOMAIN` (ci-dessus) et relancer le workflow (Actions → *Run workflow*).
2. Chez le vendeur du domaine, créer les enregistrements DNS indiqués par
   [la documentation GitHub](https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site)
   (domaine nu : quatre enregistrements `A` ; `www` : un `CNAME` vers `<compte>.github.io`).
3. **Settings → Pages → Enforce HTTPS** une fois le certificat émis.
4. Sur le serveur, renseigner `VITRINE_URL` et `VITRINE_ORIGINS` avec l'adresse du site (voir le guide
   de déploiement de l'application) : l'application autorise alors ce site à lire ses données publiques.

## Modifier le site

| Je veux… | Je modifie |
|---|---|
| Changer un texte (FR ou AR) | `content.py` |
| Changer la mise en page | `templates/*.html` et `assets/site.css` |
| Mettre le **logo** | déposer `assets/logo.svg` (ou `logo.png` / `logo.webp`) : il remplace la pastille « PSIE » |
| Publier une actualité | **pas ici** : dans l'application, menu « Actualités (gestion) » ; elle apparaît tout de suite |

Les traductions arabes sont une première version : à faire relire avant la mise en ligne.

## En local

```bash
pip install -r requirements-dev.txt
python -m pytest -q                       # tests
API_BASE=https://app.exemple.org python build.py   # génère dist/
python -m http.server 8000 --directory dist        # http://localhost:8000
```

## Sécurité

- Politique de sécurité du navigateur stricte (`script-src 'self'`, pas de style ni de script en ligne) et
  connexions limitées à l'adresse de l'application.
- Le JavaScript n'insère jamais de données comme du HTML (uniquement du texte) : une actualité contenant
  `<script>` s'affiche telle quelle, sans s'exécuter. Un test interdit `innerHTML` et équivalents.
- Les requêtes vers l'application sont faites **sans cookie** (`credentials: "omit"`).
- Les adresses saisies dans les variables sont vérifiées (une valeur piégée fait échouer la construction).
- Aucun secret n'est stocké dans ce dépôt public.


## Contenu modifiable sans programmer (dossier `data/`)

Annonce en bas d'écran, mot du Président, documents à télécharger, galerie, représentations régionales (DRENA, avec carte)
et fiches des faîtières se modifient dans les fichiers `.json` du dossier [`data/`](data/LISEZ-MOI.md) : bouton crayon sur GitHub,
enregistrer, le site se met à jour en 1 à 2 minutes. Une erreur d'écriture est signalée par le contrôle automatique
avec le nom du fichier et la ligne, et ne casse pas le site en ligne.

## Contenu géré depuis l'application (administration)

Quand l'application PSIE est en ligne, l'équipe Information et Communication modifie le site depuis son espace
(« Contenu du site ») et n'a plus besoin de GitHub.

1. Dans GitHub : Settings > Secrets and variables > Actions > **Variables** : ajouter `CONTENT_URL` =
   `https://adresse-de-l-application/api/public/site.json`.
2. À chaque modification, l'application demande à GitHub de reconstruire le site (événement `contenu-modifie`) ;
   le workflow lance `tools/fetch_content.py`, qui remplace `data/*.json` et `assets/media/` par le contenu de l'application.
3. **Tout ou rien** : si l'application est injoignable ou si une réponse est incorrecte, la construction s'arrête
   et le site déjà en ligne reste intact. Rien n'est jamais publié à moitié.
4. Sans `CONTENT_URL`, le site continue de lire le dossier `data/` comme avant.

À savoir : tant que `CONTENT_URL` est défini, les fichiers de `data/` ne sont plus la source du contenu
(ils sont remplacés à chaque construction). Pour reprendre le contenu actuel dans l'application, voir
`psie/deploy/CONTENU_SITE.md` du dépôt de l'application.

## Statistiques de visite (facultatif, sans cookies)

1. Créer un compte gratuit sur [goatcounter.com](https://www.goatcounter.com) : le « code » choisi donne l'adresse `https://CODE.goatcounter.com`.
2. Dans le dépôt : Settings → Secrets and variables → Actions → Variables → ajouter `GOATCOUNTER` = ce code.
3. Relancer le workflow. Rien n'est collecté tant que la variable n'est pas définie ; aucun cookie, aucune donnée personnelle.


## Fichiers générés automatiquement

À chaque construction, le site produit sans intervention :
- les **QR codes** du site en français et en arabe (SVG pour l'impression, PNG) : `assets/dl/qr-psie-fr.svg`, etc. Ils exigent `SITE_URL` (ou `CUSTOM_DOMAIN`) ;
- une **plaquette PDF d'une page** en français et en arabe, construite à partir des textes du site : `assets/dl/plaquette-psie-fr.pdf` et `-ar.pdf` ;
- des **images d'aperçu de lien** (1200×630) pour chaque page et chaque langue, dans `assets/og/` : elles s'affichent quand on partage une page sur WhatsApp ou Facebook. Elles ne sont créées que si `SITE_URL` est défini.

Ces fichiers ne se modifient pas à la main : ils changent quand les textes du site changent. La page « Affiche et plaquette »
les propose au téléchargement et imprime l'affiche. Les polices du PDF sont dans `tools/fonts/` (licence DejaVu incluse).
Dépendances : `requirements.txt` (`fpdf2`, `uharfbuzz`, `qrcode`, `pillow`).

## Pages interactives (sans serveur)

- **Les statuts en 10 points** : résumé pédagogique des règles essentielles (textes dans `content.py`).
- **Questionnaire d'adhésion** (page Adhérer) : construit à partir des conditions d'adhésion du site.
- **Organigramme cliquable** (page Gouvernance) et **graphique de répartition** (page Nos membres, à partir de `nombre_ecoles` dans `data/faitieres.json`).

## Chiffres clés de l'accueil

Les nombres de faîtières et de DRENA sont comptés dans `data/faitieres.json` et `data/regions.json`. Un chiffre « écoles » s'ajoute dès que des faîtières ont un `nombre_ecoles` numérique ; il indique combien de faîtières l'ont déclaré.
