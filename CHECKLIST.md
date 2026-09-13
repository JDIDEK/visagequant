# Checklist de construction VisageQuant

Cette checklist est l'ordre de marche du projet. Ne coche une case que lorsqu'une preuve existe : test automatise, benchmark, capture de l'interface ou decision documentee.

## M0 - Fondations du projet

- [x] Creer le monorepo et separer UI, moteur et contrats.
- [x] Ajouter les conventions Git, Python, TypeScript et Rust.
- [x] Ajouter les instructions permanentes pour les assistants IA.
- [x] Definir un contrat JSON versionne pour une demande et une reponse d'analyse.
- [x] Implementer les primitives geometriques testables sans framework ML.
- [x] Implementer un premier controle qualite deterministe.
- [x] Ajouter une CLI et un exemple sans photo personnelle.
- [x] Ajouter des tests unitaires du noyau.
- [x] Initialiser le depot Git sur la branche `main`.
- [x] Ajouter les images Docker pour l'API Python et l'interface React.
- [x] Ajouter Docker Compose avec healthcheck et ports limites a la machine locale.
- [x] Ajouter les scripts PowerShell de test, demarrage et arret.
- [x] Generer les fichiers de verrouillage des dependances Python, TypeScript et Rust.
- [ ] Ajouter une image GPU distincte lorsque le premier modele ML est selectionne.
- [x] Creer le premier commit local apres choix du nom et de la licence.
- [x] Choisir VisageQuant, la licence AGPL-3.0-or-later et la politique de contribution.
- [x] Ajouter le workflow CI : lint, formatage, types, tests Python, tests UI et audits.
- [ ] Publier le depot et verifier la premiere execution du workflow CI distant.

## M1 - Acquisition fiable

- [ ] Definir le protocole utilisateur : frontal, profils, trois-quarts et video guidee.
- [ ] Definir distance, focale equivalente, eclairage, expression et cadrage acceptes.
- [ ] Importer images JPEG/PNG/HEIC sans perte involontaire de metadonnees.
- [ ] Importer une video locale et extraire les frames candidates.
- [ ] Lire orientation et metadonnees EXIF utiles.
- [ ] Detecter plusieurs visages et refuser les cas ambigus.
- [ ] Mesurer nettete, exposition, contraste et occlusion.
- [ ] Estimer yaw, pitch et roll.
- [ ] Verifier expression neutre et bouche fermee.
- [ ] Verifier que cheveux, lunettes et mains ne cachent pas les zones requises.
- [ ] Guider l'utilisateur en temps reel pendant un scan de 10 a 20 secondes.
- [ ] Selectionner automatiquement les meilleures vues par angle.
- [ ] Expliquer precisement chaque refus et proposer une correction.
- [ ] Tester le controle qualite sur appareils, carnations et conditions varies.

### Criteres de sortie M1

- [ ] Deux scans consecutifs conformes produisent les memes vues cibles.
- [ ] Aucun calcul morphometrique n'est lance si un prerequis critique echoue.
- [ ] Les seuils sont mesures sur un jeu de validation, pas choisis visuellement.

## M2 - Detection et alignement 2D

- [ ] Comparer au moins deux detecteurs de visage sur le meme benchmark.
- [ ] Comparer plusieurs modeles de landmarks denses.
- [ ] Verifier licences du code, des poids et des donnees d'entrainement.
- [ ] Creer une interface `LandmarkProvider` independante du modele.
- [ ] Versionner la topologie et le mapping semantique des landmarks.
- [ ] Estimer l'incertitude de chaque landmark.
- [ ] Corriger rotation et distorsion de l'objectif.
- [ ] Conserver la matrice de transformation et son inverse.
- [ ] Visualiser les landmarks et erreurs de reprojection.
- [ ] Mesurer NME, taux d'echec et latence CPU/GPU.

### Criteres de sortie M2

- [ ] Le changement de modele ne modifie pas le contrat public.
- [ ] Chaque resultat permet de revenir aux coordonnees de la source.
- [ ] Les performances sont publiees par sous-groupe et type d'appareil.

## M3 - Reconstruction 3D multi-vues

- [ ] Evaluer une baseline FLAME avec au moins deux reconstructeurs candidats.
- [ ] Separer identite, expression, pose, texture et camera.
- [ ] Calibrer intrinseques et distorsion de camera quand les metadonnees le permettent.
- [ ] Optimiser une identite unique sur toutes les vues.
- [ ] Rejeter les frames incoherentes ou fortement deformees.
- [ ] Quantifier l'erreur de reprojection par vue et par zone.
- [ ] Ajouter une reference d'echelle optionnelle ou une source de profondeur.
- [ ] Exporter un mesh canonique local avec provenance complete.
- [ ] Afficher le mesh et les points utilises dans l'interface.
- [ ] Comparer reconstruction monoculaire et multi-vues.

### Criteres de sortie M3

- [ ] La geometrie reste stable entre trois scans d'une meme personne.
- [ ] Les mesures 3D indiquent clairement si l'echelle absolue est connue.
- [ ] Aucun millimetre n'est affiche sans calibration metrique valide.

## M4 - Moteur de mesures

- [ ] Rediger une fiche methodologique par mesure : definition, points, formule, unite, limites.
- [ ] Implementer d'abord 20 mesures prioritaires, pas 200 approximatives.
- [ ] Visage : rapport largeur/hauteur, tiers, fifths, midface.
- [ ] Yeux : distances, ouverture, canthal tilt, asymetries.
- [ ] Nez : largeur, hauteur, index, angles de profil et projection.
- [ ] Levres : largeur, hauteurs, ratio, philtrum et commissures.
- [ ] Machoire/menton : largeur, angle gonial, longueur et projection.
- [ ] Produire valeur, unite, methode, intervalle d'incertitude et confiance.
- [ ] Propager l'incertitude des landmarks jusqu'aux mesures.
- [ ] Tester invariance a l'echelle, translation, rotation et changement de vue.
- [ ] Afficher les constructions geometriques sur image et mesh.
- [ ] Ajouter des golden tests sur donnees synthetiques.

### Criteres de sortie M4

- [ ] Chaque mesure est reproductible et auditable.
- [ ] Une mesure indisponible est `null` avec une raison, jamais inventee.
- [ ] Les 20 mesures prioritaires passent les seuils de repetabilite convenus.

## M5 - Validation scientifique

- [ ] Rediger le protocole avant de collecter les resultats.
- [ ] Constituer un jeu de developpement et un jeu de test gele.
- [ ] Obtenir consentement, politique de retention et procedure de suppression.
- [ ] Definir une reference humaine ou instrumentale pour chaque famille de mesures.
- [ ] Mesurer erreur absolue, erreur angulaire, ICC et Bland-Altman.
- [ ] Mesurer repetition intra-session et inter-session.
- [ ] Analyser biais selon camera, lumiere, pose, age apparent, genre et carnation.
- [ ] Documenter les zones ou le systeme est insuffisant.
- [ ] Fixer des seuils de mise en production avant de regarder le test final.
- [ ] Faire relire la methode par une personne competente en morphometrie/vision.

## M6 - Interpretation et references

- [ ] Separer strictement mesure, reference statistique et jugement esthetique.
- [ ] Identifier des jeux de reference licites et representatifs.
- [ ] Versionner population, filtres, statistiques et intervalles.
- [ ] Preferer percentile et intervalle a une note universelle.
- [ ] Afficher les limites culturelles et statistiques.
- [ ] Interdire recommandations medicales automatisees.
- [ ] Concevoir des recommandations non invasives et reversibles en premier.
- [ ] Faire valider tout contenu medical ou chirurgical par un professionnel qualifie.
- [ ] Ajouter une option sans scoring esthetique.

## M7 - Rapport local et LLM

- [ ] Generer d'abord un rapport deterministe sans LLM.
- [ ] Definir un schema d'entree minimal pour le redacteur local.
- [ ] Tester un petit modele local quantifie sur RTX 4060.
- [ ] Interdire au LLM de modifier chiffres, confiance et provenance.
- [ ] Verifier automatiquement que les valeurs citees existent dans le JSON source.
- [ ] Ajouter des formulations prudentes pour faible confiance.
- [ ] Tester hallucinations, contradictions et formulations blessantes.
- [ ] Permettre l'export PDF et JSON sans image.
- [ ] Permettre la regeneration du texte sans refaire l'analyse.

## M8 - Application desktop

- [ ] Brancher React a l'API locale avec timeout et erreurs explicites.
- [ ] Ajouter le parcours import, scan, validation, traitement, resultats.
- [ ] Ajouter une vue 2D superposee et une vue mesh 3D.
- [ ] Rendre chaque mesure cliquable et explicable.
- [ ] Ajouter comparaison de scans avec conditions comparables.
- [ ] Chiffrer les donnees sensibles au repos.
- [ ] Ajouter suppression immediate et retention configurable.
- [ ] Fonctionner hors ligne apres installation.
- [ ] Signer et empaqueter l'application Linux puis Windows.
- [ ] Tester mises a jour et migration de base locale.
- [ ] Tester accessibilite clavier, contraste et lecteurs d'ecran.

## M9 - Securite, legal et produit

- [ ] Faire un inventaire des donnees personnelles et traitements locaux.
- [ ] Rediger notice de confidentialite et consentement explicite.
- [ ] Interdire telemetrie et crash reports contenant images ou geometrie faciale.
- [ ] Ajouter une analyse de menace : fichiers malveillants, modeles, API locale, exports.
- [ ] Verifier les licences avant toute distribution ou monetisation.
- [ ] Definir positionnement non medical et mentions obligatoires.
- [ ] Prevoir suppression, export et portabilite des donnees.
- [ ] Faire tester le produit par des utilisateurs sans guider leurs reponses.
- [ ] Definir les metriques produit sans optimiser l'insatisfaction corporelle.

## Routine pour chaque session avec une IA

- [ ] Donner une seule tache delimitee et le resultat attendu.
- [ ] Nommer les fichiers que l'IA peut modifier.
- [ ] Donner les invariants et les cas d'erreur.
- [ ] Demander les tests avant ou avec l'implementation.
- [ ] Exiger la commande exacte de verification.
- [ ] Lire le diff, surtout formules, seuils, licences et confidentialite.
- [ ] Lancer tests, lint et types localement.
- [ ] Refuser les dependances ou modeles ajoutes sans justification.
- [ ] Mettre a jour cette checklist et la decision associee.
- [ ] Faire un commit petit et reversible.

## Prompts reutilisables

### Implementer une tache

```text
Lis AGENTS.md, CHECKLIST.md et les fichiers concernes. Implemente uniquement [TACHE].
Invariants : [LISTE]. Cas d'erreur : [LISTE]. Ajoute les tests avant ou avec le code.
Ne change aucun contrat public sans me le signaler. Termine par le diff conceptuel,
les risques restants et les commandes exactes de verification.
```

### Revue scientifique

```text
Audite cette mesure comme un reviewer hostile. Verifie definition anatomique,
landmarks, formule, invariances, propagation d'incertitude, biais de perspective,
preuve de validation et limites. N'invente aucune norme. Liste les preuves manquantes.
```

### Revue de code

```text
Fais une revue sans modifier les fichiers. Cherche d'abord erreurs de calcul,
regressions, fuite de donnees, contrats casses et tests insuffisants. Donne chaque
probleme avec fichier, gravite, scenario de reproduction et correction minimale.
```
