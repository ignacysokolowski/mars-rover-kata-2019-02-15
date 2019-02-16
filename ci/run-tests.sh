#!/usr/bin/env bash

set -e

cd "$(dirname "$0")/../src"

if [ "$1" = "--coverage" ]; then
  ARGS="\
  -v \
  --cov mars_rover \
  --cov-report term-missing \
  --cov-report html:../ci/test/reports/coverage \
  --junit-xml=../ci/test/reports/results.xml \
  "
else
  ARGS=""
fi
../venv/bin/python -m pytest $ARGS tests
