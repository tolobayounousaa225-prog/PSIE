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
