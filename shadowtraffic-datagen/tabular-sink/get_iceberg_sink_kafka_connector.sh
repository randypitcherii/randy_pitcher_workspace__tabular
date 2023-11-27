#!/bin/bash

VERSION="0.6.4"

# Download the zip file
wget "https://github.com/tabular-io/iceberg-kafka-connect/releases/download/v${VERSION}/iceberg-kafka-connect-runtime-${VERSION}.zip"

# Extract the zip file
unzip "iceberg-kafka-connect-runtime-${VERSION}.zip"