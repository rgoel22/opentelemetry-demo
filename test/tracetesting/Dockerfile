# Copyright The OpenTelemetry Authors
# SPDX-License-Identifier: Apache-2.0

FROM alpine

WORKDIR /app

# Add required utilities
RUN apk --update add bash jq curl

# Copy the tar.gz file to the container
COPY ./test/tracetesting/tracetest.tar.gz /app/

# Extract the tar.gz file and move the binary to a known location
RUN tar -xzf /app/tracetest.tar.gz \
    && mv tracetest /usr/local/bin/ \
    && chmod +x /usr/local/bin/tracetest \
    && rm -rf /app/tracetest.tar.gz

# Copy the testing files to the container
COPY ./test/tracetesting /app/test/tracetesting

WORKDIR /app/test/tracetesting

ENTRYPOINT ["/bin/bash", "/app/test/tracetesting/run.bash"]
