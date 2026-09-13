# Protocole d'acquisition M1

- Statut : brouillon executable
- Version : `acquisition-1.0.0`
- Population initiale : adultes consentants
- Traitement : local par defaut

## Objectif

Produire une sequence multi-vues reproductible avant toute detection de landmarks
ou mesure morphometrique. Une sequence incomplete ou une vue critique invalide
bloque les mesures concernees.

## Parcours utilisateur

Deux modes sont prevus : une video guidee de 10 a 20 secondes et cinq images
fixes. Les vues candidates sont selectionnees dans cet ordre :

1. face, yaw nominal `0 deg` ;
2. trois-quarts gauche, yaw nominal `-45 deg` ;
3. profil gauche, yaw nominal `-90 deg` ;
4. trois-quarts droit, yaw nominal `45 deg` ;
5. profil droit, yaw nominal `90 deg`.

Les angles sont des cibles de guidage et ne constituent pas encore des seuils
d'acceptation. Leur tolerance restera absente du contrat jusqu'a calibration sur
un jeu de validation representatif.

## Conditions demandees

- camera a hauteur des yeux et immobile pendant la sequence ;
- distance stable, visage entierement visible et absence de zoom numerique ;
- lumiere diffuse et uniforme, sans zone surexposee ni ombre dure ;
- expression neutre, bouche fermee et yeux visibles ;
- contours utiles du visage degages des cheveux, mains et objets.

L'application devra mesurer ces conditions. Une simple confirmation de
l'utilisateur ne suffit pas a valider une acquisition.

## Parametres encore a calibrer

- plage de distance et proportion minimale du visage dans l'image ;
- plage de focale equivalente et distorsion acceptable ;
- tolerances de yaw, pitch et roll par vue ;
- seuils de nettete, exposition, contraste et occlusion ;
- confiance minimale pour l'expression neutre et la fermeture de la bouche ;
- nombre minimal de frames conformes et stabilite entre frames.

Chaque seuil sera fixe avant evaluation finale, avec sa methode, son jeu de
validation, ses erreurs par sous-groupe et sa version. Les valeurs provisoires de
`quality.py` ne sont pas des criteres de sortie M1.

## Contrat et provenance

Le moteur expose `GET /v1/acquisition-protocol`. Sa reponse suit
`packages/contracts/acquisition-protocol.schema.json`. Une future session conservera
au minimum le mode, les vues sources, les frames retenues, les metadonnees de
camera disponibles, les transformations, les signaux de qualite et leurs versions.

Les images ne sont jamais incluses dans les tests unitaires. Les tests du protocole
utilisent uniquement des identifiants et des donnees synthetiques.
