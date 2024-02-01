all: run

run:
	docker-compose down --volumes --remove-orphans
	docker compose pull
	docker compose up -d

restart_tabular_connector:
	@echo 'Restarting tabular_connector...'
	docker compose down tabular_connector
	docker compose up --force-recreate --build --remove-orphans tabular_connector

logs:
	docker compose logs -f

sample:
	docker run --env-file $$(pwd)/shadowtraffic/license.env -v $$(pwd)/shadowtraffic/config.json:/home/config.json shadowtraffic/shadowtraffic:latest --config /home/config.json --watch --sample 10 --stdout
