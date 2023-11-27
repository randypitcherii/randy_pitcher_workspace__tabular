docker run --env-file license.env -v $(pwd)/config.json:/home/config.json shadowtraffic/shadowtraffic:latest --config /home/config.json --watch --sample 10 --stdout
