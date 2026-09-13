# Registre methodologique

Ce document devient la source de verite scientifique du produit. Aucune reference statistique ni interpretation esthetique ne doit entrer dans le code avant d'etre documentee ici.

## Statut des seuils actuels

Les seuils de `quality.py` sont provisoires et servent uniquement a rendre le squelette executable. Ils ne sont ni valides cliniquement, ni adaptes a une publication. Le lot M1 doit les remplacer par des seuils calibres sur un jeu representatif.

## Protocole d'acquisition M1

Le protocole `acquisition-1.0.0` definit cinq cibles nominales : face, deux
trois-quarts et deux profils. Ces angles servent uniquement au guidage. Aucune
tolerance d'acceptation n'est definie avant calibration. Les conditions, inconnues
et criteres de validation sont detailles dans [ACQUISITION_PROTOCOL.md](ACQUISITION_PROTOCOL.md).

## Fiche obligatoire pour chaque mesure

- identifiant stable ;
- nom et definition anatomique ;
- vues compatibles ;
- landmarks ou surfaces requis ;
- repere de coordonnees ;
- formule et unite ;
- invariances attendues ;
- sources scientifiques ;
- methode de reference ;
- propagation d'incertitude ;
- limites et causes d'indisponibilite ;
- resultats de repetabilite et d'exactitude ;
- version de methode.

## Mesures baseline

Les quatre mesures presentes dans le prototype servent a valider l'architecture logicielle. Elles ne doivent pas encore alimenter un score ni une recommandation.
