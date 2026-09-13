# Contribuer a VisageQuant

Merci de contribuer a une analyse faciale libre, locale et explicable.

## Avant une modification

Une contribution de code doit annoncer son objectif, les fichiers concernes, les
invariants, les tests attendus, la commande de verification et les points encore
non resolus. Les changements petits et auditables sont preferes.

Toute nouvelle mesure, reference statistique ou hypothese qui influence un resultat
doit d'abord etre documentee dans `docs/METHODOLOGY.md`. Une correlation ne doit
pas etre transformee en causalite.

## Regles techniques et donnees

- Ne placez aucun visage reel dans les tests unitaires.
- Ne commitez aucun poids de modele, secret ou donnee faciale personnelle.
- Isolez les modeles externes derriere un adaptateur versionne.
- Versionnez tout changement de contrat public.
- Faites echouer explicitement les entrees invalides.
- Utilisez les environnements Docker de reference lorsque c'est possible.

Verification minimale du moteur :

```powershell
docker compose run --rm --build --no-deps api python -m unittest discover -s tests -v
```

La CI verifie egalement formatage, lint, types, tests de l'interface, builds et
vulnerabilites connues des dependances.

## Licence des contributions

En soumettant une contribution, vous confirmez avoir le droit de la proposer et
acceptez qu'elle soit distribuee sous la licence
`AGPL-3.0-or-later`, comme le reste du code original du projet. Les composants
tiers restent soumis a leurs propres licences et doivent etre declares.

N'incluez jamais de photo ou d'information personnelle dans une issue, un journal
de test ou une capture publique.
