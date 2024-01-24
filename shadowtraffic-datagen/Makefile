all: run

run:
	docker-compose down --volumes --remove-orphans
	docker compose pull
	docker compose up -d

logs:
	docker compose logs -f

sample:
	docker run --env-file $$(pwd)/shadowtraffic/license.env -v $$(pwd)/shadowtraffic/config.json:/home/config.json shadowtraffic/shadowtraffic:latest --config /home/config.json --watch --sample 10 --stdout
