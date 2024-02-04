FROM docker.io/bitnami/kafka:3.5

# Switch to root user to install packages
USER root
RUN apt-get update && apt-get install -y unzip wget

# Get the Iceberg Kafka Connect runtime 
ARG VERSION="0.6.5"
RUN wget "https://github.com/tabular-io/iceberg-kafka-connect/releases/download/v${VERSION}/iceberg-kafka-connect-runtime-${VERSION}.zip" \
  && unzip -d /bitnami "iceberg-kafka-connect-runtime-${VERSION}.zip" \
  && rm "iceberg-kafka-connect-runtime-${VERSION}.zip"

COPY . /tabular_connector
RUN chmod +x /tabular_connector/deploy_tabular_connector.sh

CMD ["/tabular_connector/deploy_tabular_connector.sh"]