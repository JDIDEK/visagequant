# Travailler efficacement avec une IA

## Une session, une preuve

Decouper le travail en changements verifiables en moins d'une heure. Une bonne demande aboutit a un test, un benchmark, une decision ou une petite fonctionnalite observable.

## Contexte minimal a fournir

1. Le jalon et la case de `CHECKLIST.md`.
2. Les fichiers autorises.
3. Le comportement attendu et les invariants.
4. Les donnees de test autorisees.
5. La commande de verification.

## Quand ouvrir une decision d'architecture

Creer un fichier dans `docs/decisions/` lorsqu'un choix est couteux a inverser : topologie de landmarks, modele 3D, format de stockage, chiffrement, protocole d'acquisition ou methode de score.

## Strategie de branches

- une branche par petite fonctionnalite ;
- un commit pour le test et l'implementation coherente ;
- aucun poids de modele ou visage reel ;
- revue humaine obligatoire des formules et seuils ;
- benchmark avant remplacement d'un modele.

## Boucle recommandee

```text
Spec courte -> test qui echoue -> implementation -> test -> revue du diff
-> benchmark si necessaire -> documentation -> commit
```

