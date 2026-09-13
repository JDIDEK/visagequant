# ADR 0001 - Pipeline centre sur la qualite

- Statut : accepte
- Date : 2026-09-13

## Decision

Le pipeline refuse une acquisition qui echoue a un controle critique avant toute mesure. Les mesures sont deterministes, versionnees et accompagnees d'une confiance. Le LLM est facultatif et intervient uniquement apres la production d'un rapport structure.

## Consequences

- L'application donnera parfois moins de resultats, mais ils seront plus auditables.
- Les seuils de qualite devront etre valides et maintenus comme une partie du produit.
- Les modeles externes resteront remplacables sans changer les contrats UI.

