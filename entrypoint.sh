#!/bin/sh -l

cd "$GITHUB_WORKSPACE"
echo $(python -V)

python /render.py "$@"
