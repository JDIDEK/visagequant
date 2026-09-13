.PHONY: test demo docker-test docker-up docker-down

test:
	cd apps/analysis-engine && PYTHONPATH=src python3 -m unittest discover -s tests -v

demo:
	cd apps/analysis-engine && PYTHONPATH=src python3 -m visagequant_engine.cli ../../packages/contracts/examples/analysis-request.json

docker-test:
	docker compose run --rm --build --no-deps api python -m unittest discover -s tests -v

docker-up:
	docker compose up --build

docker-down:
	docker compose down
