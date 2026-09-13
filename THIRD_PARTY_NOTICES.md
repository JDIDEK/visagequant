# Composants tiers

La licence AGPL-3.0-or-later couvre le code original de VisageQuant. Elle ne change
pas les licences des bibliotheques, modeles, poids ou jeux de donnees tiers.

Les versions logicielles actuelles sont conservees dans `uv.lock` et
`pnpm-lock.yaml`. Avant l'ajout d'un modele externe, la contribution doit consigner :

- le nom, la version, la source et l'adaptateur utilise ;
- la licence du code ;
- la licence et le hash des poids ;
- les conditions du jeu d'entrainement lorsque celles-ci sont connues ;
- les droits de redistribution et les restrictions d'usage ;
- le benchmark justifiant la selection ou le remplacement.

Aucun poids de modele externe n'est distribue dans le depot a ce stade.
