# Données du site (modifiables sans programmer)

Chaque fichier `.json` de ce dossier alimente une partie du site. Modifiez-le directement sur GitHub
(bouton crayon), enregistrez : le site se met à jour tout seul en 1 à 2 minutes.
Un champ vide = la section correspondante reste cachée (ou affiche « bientôt »).
Gardez les guillemets, les virgules et les accolades tels quels ; GitHub signale une erreur de syntaxe avant l'enregistrement.

| Fichier | Rôle |
|---|---|
| `annonce.json` | Bandeau en haut du site. Mettre `"actif": true` et écrire le texte `fr` / `ar` (`lien` facultatif, commençant par `https://`). |
| `president.json` | Mot du Président : `nom`, `photo` (ex. `assets/president.jpg`), `message` en `fr` et `ar`. |
| `documents.json` | Documents à télécharger : `titre`, `description` (`fr`/`ar`), `fichier` (ex. `assets/docs/statuts.pdf`). Déposez le PDF dans `assets/docs/`. |
| `actualites.json` | Actualités : `slug` (lettres minuscules, chiffres, tirets), `date` (AAAA-MM-JJ), `titre`, `resume` (une phrase), `contenu` (`fr`/`ar`, un retour à la ligne = un nouveau paragraphe), `image` facultative. Les plus récentes passent en premier. |
| `equipe.json` | Bureau exécutif : `nom`, `fonction` (`fr`/`ar`), `organisation`, `organe` (`den` = Direction Exécutive Nationale, `ca` = Conseil d'Administration, `cc` = Commissariat aux Comptes), `photo` (ex. `assets/equipe/nom.jpg`). |
| `partenaires.json` | Partenaires : `nom`, `type` (`etat`, `technique` ou `financier`), `logo`, `site_web`, `description` (`fr`/`ar`). |
| `contact.json` | `whatsapp` (numéro avec l'indicatif, sans + ni espaces, ex. `22507XXXXXXXX`) et `message` pré-rempli ; liens `facebook`, `youtube`, `instagram` (en `https://`). Un champ vide = le bouton n'apparaît pas. |
| `galerie.json` | Photos : `image` (ex. `assets/galerie/ag-2026.jpg`), `legende` (`fr`/`ar`), `date`. Déposez les images dans `assets/galerie/`. |
| `regions.json` | Les 41 DRENA : `region`, `drena`, `delegue`, `telephone`, et `lat` / `lon` (pour la carte). |
| `faitieres.json` | Fiche de chaque faîtière : `nom`, `presentation` (`fr`/`ar`), `logo`, `annee_creation`, `nombre_ecoles`, `telephone`, `email`, `adresse`, `site_web`. |

Formats d'image acceptés : `.jpg`, `.png`, `.webp`, `.svg` (maximum conseillé : 1 Mo par image).
Documents : `.pdf`.
