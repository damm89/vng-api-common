#!/bin/bash

set -e

if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "You need to activate your virtual env before running this script"
    exit 1
fi

toplevel=$(git rev-parse --show-toplevel)
cd $toplevel

./manage.py generate_swagger -f yaml swagger2.0.yaml
