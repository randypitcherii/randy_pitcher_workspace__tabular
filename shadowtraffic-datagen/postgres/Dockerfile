FROM postgres:latest

ENV POSTGRES_USER=postgres \
    POSTGRES_PASSWORD=postgres \
    POSTGRES_DB=tabular

COPY . /docker-entrypoint-initdb.d

USER postgres

CMD ["postgres", "-c", "wal_level=logical"]