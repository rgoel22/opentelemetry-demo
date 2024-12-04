# Copyright The OpenTelemetry Authors
# SPDX-License-Identifier: Apache-2.0

FROM alpine

WORKDIR /app

RUN apk --update add bash jq curl

COPY tracetest.tar.gz /app/
RUN tar -xzf /app/tracetest.tar.gz \
    && mv tracetest /usr/local/bin/ \
    && chmod +x /usr/local/bin/tracetest \
    && rm -f /app/tracetest.tar.gz

# Copy the remaining test files
COPY . /app/test/tracetesting

WORKDIR /app/test/tracetesting

ENTRYPOINT ["/bin/bash", "/app/test/tracetesting/run.bash"]
