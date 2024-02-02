FROM quay.io/debezium/connect:2.5

ENV BOOTSTRAP_SERVERS="kafka:9092" \
    GROUP_ID="5432" \
    CONFIG_STORAGE_TOPIC="dbz_connect_configs" \
    OFFSET_STORAGE_TOPIC="dbz_connect_offsets" \
    STATUS_STORAGE_TOPIC="dbz_connect_statuses" \
    KEY_CONVERTER="org.apache.kafka.connect.json.JsonConverter" \
    VALUE_CONVERTER="org.apache.kafka.connect.json.JsonConverter" \
    CONNECT_KEY_CONVERTER_SCHEMAS_ENABLE="false" \
    CONNECT_VALUE_CONVERTER_SCHEMAS_ENABLE="false" \
    CONNECT_PRODUCER_INTERCEPTOR_CLASSES="io.confluent.monitoring.clients.interceptor.MonitoringProducerInterceptor" \
    CONNECT_CONSUMER_INTERCEPTOR_CLASSES="io.confluent.monitoring.clients.interceptor.MonitoringConsumerInterceptor" \
    CONNECT_PLUGIN_PATH="/kafka/connect"

USER root
COPY . /debezium_connector
RUN chmod +x /debezium_connector/deploy_debezium_connector.sh && /debezium_connector/deploy_debezium_connector.sh