# Copyright The OpenTelemetry Authors
# SPDX-License-Identifier: Apache-2.0

FROM alpine

WORKDIR /app

ARG TRACETEST_IMAGE_VERSION=1.7.1

RUN apk --update add bash jq curl \
    && curl -L -o tracetest.tar.gz https://github.com/kubeshop/tracetest/releases/download/v$TRACETEST_IMAGE_VERSION/tracetest_$TRACETEST_IMAGE_VERSION_linux_amd64.tar.gz \
    && tar -xvzf tracetest.tar.gz \
    && mv tracetest /usr/local/bin/ \
    && chmod +x /usr/local/bin/tracetest \
    && rm -rf tracetest.tar.gz

COPY test/tracetesting /app/test/tracetesting

WORKDIR /app/test/tracetesting

ENTRYPOINT ["/bin/bash", "/app/test/tracetesting/run.bash"]
