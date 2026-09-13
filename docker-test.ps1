$ErrorActionPreference = "Stop"

docker compose build api
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

docker compose run --rm --no-deps api `
    python -m unittest discover -s tests -v
exit $LASTEXITCODE

