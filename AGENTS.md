# Instructions aux agents IA

## Mission

Construire une application locale d'analyse morphometrique faciale precise, reproductible, explicable et respectueuse de la vie privee. Ne jamais presenter le projet comme un outil medical ou comme une mesure objective de l'attractivite.

## Ordre de priorite

1. Validite des mesures.
2. Reproductibilite.
3. Confidentialite locale.
4. Explicabilite.
5. Performance.
6. Esthetique de l'interface.

## Contraintes d'architecture

- Garder `visagequant_engine.domain` independant de FastAPI, PyTorch, OpenCV et de l'UI.
- Faire circuler des contrats JSON versionnes entre le moteur et l'interface.
- Isoler chaque modele externe derriere un adaptateur.
- Conserver les sorties brutes, les transformations et les versions de modeles dans la provenance d'une analyse.
- Le LLM ne calcule ni landmarks, ni angles, ni distances, ni scores.
- Ne pas telecharger de poids de modele dans Git.
- Ne jamais utiliser de photos reelles dans les tests unitaires.
- Garder gratuites les mesures essentielles, leurs explications et les exports personnels officiels.
- Separer les conseils choisis par l'utilisateur des mesures et des references statistiques.

## Definition of Done pour toute tache

- Le comportement est decrit dans un test ou un critere d'acceptation.
- Les entrees invalides echouent explicitement.
- Aucun secret, chemin personnel ou donnee faciale n'est commite.
- La documentation et la checklist sont mises a jour si le perimetre change.
- Les commandes de test concernees passent localement.
- Les hypotheses scientifiques sont referencees dans `docs/METHODOLOGY.md` avant d'influencer un score.

## Commandes de reference

- Environnement principal Windows : `./docker-test.ps1` puis `./docker-start.ps1`.
- Commande de test portable : `docker compose run --rm --build --no-deps api python -m unittest discover -s tests -v`.
- Ne pas demander l'installation locale de Python, Node ou `make` lorsqu'une tache peut etre executee dans les conteneurs.
- Ne pas ajouter CUDA ou de runtime GPU a l'image tant qu'un modele benchmarke ne le necessite pas.

## Interdits

- Inventer des seuils cliniques ou esthetiques.
- Transformer une correlation en causalite.
- Ajouter un score global opaque.
- Masquer une faible confiance derriere un texte rassurant.
- Modifier un contrat public sans incrementer sa version.
- Remplacer silencieusement un modele ou ses poids.

## Format attendu des contributions IA

Dans chaque demande de code, exiger : objectif, fichiers autorises, invariants, tests attendus, commande de verification et points non resolus. Preferer de petits changements auditables a une generation massive.
