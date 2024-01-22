# Debian 11 is recommended.
FROM debian:11-slim

# Suppress interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# (Required) Install utilities required by Spark scripts.
RUN apt update && apt install -y procps tini libjemalloc2

# Enable jemalloc2 as default memory allocator
ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.2

# Add Apache Iceberg dependencies
ENV SPARK_EXTRA_JARS_DIR=/opt/spark/jars/
ENV SPARK_EXTRA_CLASSPATH='/opt/spark/jars/*'
RUN mkdir -p "${SPARK_EXTRA_JARS_DIR}"

# Variables for Apache Iceberg runtime and GCP bundle URLs
ARG ICEBERG_RUNTIME_URL=https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-spark-runtime-3.3_2.12/1.4.3/iceberg-spark-runtime-3.3_2.12-1.4.3.jar
ARG ICEBERG_GCP_BUNDLE_URL=https://search.maven.org/remotecontent?filepath=org/apache/iceberg/iceberg-gcp-bundle/1.4.3/iceberg-gcp-bundle-1.4.3.jar

# Download and place the Apache Iceberg runtime for Spark and GCP bundle in the jars directory
ADD "${ICEBERG_RUNTIME_URL}" "${SPARK_EXTRA_JARS_DIR}"
ADD "${ICEBERG_GCP_BUNDLE_URL}" "${SPARK_EXTRA_JARS_DIR}"

# (Required) Create the 'spark' group/user.
# The GID and UID must be 1099. Home directory is required.
RUN groupadd -g 1099 spark
RUN useradd -u 1099 -g 1099 -d /home/spark -m spark
USER spark