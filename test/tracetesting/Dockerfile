# Copyright The OpenTelemetry Authors
# SPDX-License-Identifier: Apache-2.0

FROM alpine

WORKDIR /app

# Set the Tracetest CLI version
ARG TRACETEST_IMAGE_VERSION=1.7.1

# Install required packages and download Tracetest CLI
RUN apk --update add bash jq curl
RUN curl -L https://raw.githubusercontent.com/kubeshop/tracetest/main/install-cli.sh | bash -s -- $TRACETEST_IMAGE_VERSION

COPY test/tracetesting /app/test/tracetesting
COPY . /app/test/tracetesting

# Set the working directory for tests
WORKDIR /app/test/tracetesting

# Set the entrypoint to execute the test script
ENTRYPOINT ["/bin/bash", "/app/test/tracetesting/run.bash"]
