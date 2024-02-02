#!/bin/bash

# Function to submit the connector configuration
submit_connector() {
  until curl -s http://localhost:8083/ | grep -q "version"; do
    echo "Waiting for Kafka Connect to start..."
    sleep 5
  done
  curl -X POST -H "Content-Type: application/json" --data @/debezium_connector/debezium-connector.json http://localhost:8083/connectors
}

# Run the submit_connector function in the background
submit_connector &