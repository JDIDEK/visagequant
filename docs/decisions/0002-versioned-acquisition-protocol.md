# ADR 0002 - Protocole d'acquisition versionne

- Statut : accepte
- Date : 2026-09-13

## Decision

L'interface obtient le parcours d'acquisition depuis un contrat JSON versionne
expose par le moteur. La premiere version demande cinq vues ordonnees et accepte
les modes video guidee ou images fixes. Les angles sont des cibles nominales ; les
tolerances restent absentes tant qu'elles ne sont pas calibrees.

## Consequences

- le guidage et le moteur partagent les memes identifiants de vues ;
- un changement incompatible exige une nouvelle version du contrat ;
- aucune mesure ne doit demarrer sur la seule base d'une sequence declaree complete ;
- les futurs seuils devront etre documentes et valides avant de passer le protocole
  du statut `draft` a un statut publiable.
