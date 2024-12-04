# Copyright The OpenTelemetry Authors
# SPDX-License-Identifier: Apache-2.0

FROM alpine

WORKDIR /app

# Set the Tracetest CLI version
ARG TRACETEST_IMAGE_VERSION=1.7.1

# Install required packages and download Tracetest CLI
RUN apk --no-cache add bash jq curl \
    && curl -L -o tracetest.tar.gz https://github.com/kubeshop/tracetest/releases/download/v${TRACETEST_IMAGE_VERSION}/tracetest_${TRACETEST_IMAGE_VERSION}_linux_amd64.tar.gz \
    && tar -xzf tracetest.tar.gz \
    && mv tracetest /usr/local/bin/ \
    && chmod +x /usr/local/bin/tracetest \
    && rm -rf tracetest.tar.gz

# Verify Tracetest installation
RUN /usr/local/bin/tracetest version || echo "Tracetest installation failed. Check compatibility."

# Copy test files
COPY . /app/test/tracetesting

# Set the working directory for tests
WORKDIR /app/test/tracetesting

# Set the entrypoint to execute the test script
ENTRYPOINT ["/bin/bash", "/app/test/tracetesting/run.bash"]
