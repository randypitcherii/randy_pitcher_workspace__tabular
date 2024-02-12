all: run

down:
	docker-compose down --volumes --remove-orphans

run: down
	docker compose up --force-recreate --build --remove-orphans -d

run_dbz: down
	docker compose up --force-recreate --build --remove-orphans -d kafka debezium shadowtraffic_pg postgres tabular_connector

restart_tabular_connector:
	@echo 'Restarting tabular_connector...'
	docker compose down  --volumes --remove-orphans tabular_connector
	docker compose up --force-recreate --build --remove-orphans tabular_connector

restart_shadowtraffic:
	@echo 'Restarting shadowtraffic...'
	docker compose down  --volumes --remove-orphans shadowtraffic
	docker compose up --force-recreate --build --remove-orphans shadowtraffic

restart_debezium:
	@echo 'Restarting debezium...'
	docker compose down  --volumes --remove-orphans debezium
	docker compose up --force-recreate --build --remove-orphans debezium

logs:
	docker compose logs -f

watch_topics:
	docker compose exec -it kafka watch /opt/bitnami/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092 

sample:
	docker run --env-file $$(pwd)/shadowtraffic/license.env -v $$(pwd)/shadowtraffic/pg-config.json:/home/config.json shadowtraffic/shadowtraffic:latest --config /home/config.json --watch --sample 10 --stdout
	docker run --env-file $$(pwd)/shadowtraffic/license.env -v $$(pwd)/shadowtraffic/kafka-config.json:/home/config.json shadowtraffic/shadowtraffic:latest --config /home/config.json --watch --sample 10 --stdout
