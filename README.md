# VisageQuant

Alternative open source, locale et transparente aux services payants d'analyse
faciale. VisageQuant aide chacun a comprendre sa morphologie et a explorer des
ameliorations personnelles accessibles, sans verrouiller les resultats derriere un
abonnement.

Les modeles de vision produisent la geometrie, le moteur deterministe produit les
mesures, et un LLM eventuel ne fait qu'expliquer les resultats.

> Etat actuel : phase 0, socle d'architecture et moteur geometrique minimal. Ce depot ne produit pas encore d'analyse medicale ou esthetique validee.

## Objectifs

- conserver gratuitement les fonctions essentielles et les rapports officiels ;
- traitement local des photos et scans ;
- acquisition multi-vues avec controle qualite strict ;
- reconstruction 3D et mesures reproductibles ;
- score de confiance par mesure ;
- methodologie versionnee et testable ;
- separation claire entre mesure objective et interpretation subjective.

La [charte produit](docs/PRODUCT_CHARTER.md) definit les engagements de gratuite,
de dignite, de confidentialite et d'independance vis-a-vis des produits existants.

## Architecture

```text
apps/desktop          Interface React puis enveloppe Tauri
apps/analysis-engine Moteur Python, controle qualite, geometrie, API locale
packages/contracts   Contrats JSON echanges entre l'UI et le moteur
docs                  Architecture, decisions et methode de travail avec l'IA
```

## Demarrage rapide du moteur minimal

### Windows avec Docker — recommande

Prerequis unique : Docker Desktop lance avec le moteur WSL 2.

Depuis PowerShell, a la racine du projet :

```powershell
.\docker-test.ps1
.\docker-start.ps1
```

Puis ouvrir <http://127.0.0.1:1420>. L'API locale est exposee sur
<http://127.0.0.1:8765> et sa documentation sur <http://127.0.0.1:8765/docs>.

Pour arreter :

```powershell
.\docker-stop.ps1
```

Les commandes equivalentes, sans scripts PowerShell, sont :

```powershell
docker compose run --rm --build --no-deps api python -m unittest discover -s tests -v
docker compose up --build
docker compose down
```

Il n'est pas necessaire d'installer Python, Node, pnpm, Rust ou `make` sur Windows
pour lancer cette version navigateur. Tauri sera utilise plus tard pour produire
l'application desktop native.

### Execution sans Docker

Le noyau actuel utilise uniquement la bibliotheque standard Python :

```bash
cd apps/analysis-engine
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m visagequant_engine.cli ../../packages/contracts/examples/analysis-request.json
```

Pour installer ensuite l'environnement complet :

```bash
cd apps/analysis-engine
uv sync --extra dev
uv run uvicorn visagequant_engine.api:app --host 127.0.0.1 --port 8765
```

Pour l'interface :

```bash
cd apps/desktop
pnpm install
pnpm dev
```

Les dependances lourdes de reconstruction ne sont volontairement pas branchees a ce stade. Leur selection doit passer par la verification de licence, la mesure de precision et un benchmark reproductible.

## Verification continue

Le workflow `.github/workflows/ci.yml` verifie le formatage, le lint, les types,
les tests Python et React, les builds et les vulnerabilites connues des dependances.
Les environnements Python et TypeScript sont reproduits depuis `uv.lock` et
`pnpm-lock.yaml`. Les memes controles peuvent etre executes localement dans Docker.

## Regles du projet

1. Une mauvaise acquisition est refusee, jamais maquillee par un score.
2. Une mesure affiche toujours son unite, sa methode, sa confiance et la version du pipeline.
3. Aucun score esthetique global n'est ajoute avant validation des mesures qui le composent.
4. Les images personnelles restent hors du depot Git.
5. Toute modification generee par IA passe par les tests et les criteres de [CHECKLIST.md](CHECKLIST.md).

## Contribuer et licence

VisageQuant est distribue sous licence
[GNU Affero General Public License v3.0 ou ulterieure](LICENSE). Les contributions
sont bienvenues selon [CONTRIBUTING.md](CONTRIBUTING.md). Les bibliotheques, jeux de
donnees et futurs poids de modeles conservent leurs licences propres, documentees
dans [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## Prochain jalon

Terminer le lot `M1 - Acquisition fiable` de la checklist : import photo/video, extraction de frames, controle de nettete/lumiere/pose et refus explicite des acquisitions insuffisantes.
