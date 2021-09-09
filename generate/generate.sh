#!/usr/bin/env bash

set -eo pipefail

cd "$(dirname "$0")"

function die() {
    echo 1>&2 $*
    exit 1
}

if [ -z "$GEN_PATH" ]; then
    die "GEN_PATH must be set, e.g. /path/to/sajari/sdk-python"
fi
if [ -z "$TEMPLATES_PATH" ]; then
    die "TEMPLATES_PATH must be set, e.g. /path/to/sajari/sdk-python/generate/templates"
fi

VERSION=4.1.0

docker-entrypoint.sh generate \
  -i /openapi.json  \
  -g python \
  -o $GEN_PATH \
  -t $TEMPLATES_PATH \
  --artifact-version $VERSION \
  --http-user-agent "sajari-sdk-python-$VERSION" \
  --group-id com.sajari \
  --git-host "github.com" \
  --git-user-id "sajari" \
  --git-repo-id sdk-python \
  --api-package com.sajari.client.api \
  --model-package com.sajari.client.models \
  --additional-properties licenseUrl="http://www.opensource.org/licenses/mit-license.php" \
  --additional-properties licenseName="MIT license" \
  --additional-properties artifactId=sajari-sdk-python-client \
  --additional-properties artifactUrl="https://github.com/sajari/sdk-python" \
  --additional-properties artifactDescription="Sajari SDK Python Client" \
  --additional-properties packageName="sajari_client" \
  --additional-properties projectName="sajari-client"