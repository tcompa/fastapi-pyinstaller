#!/bin/bash

uv run pyinstaller \
   ./src/fastapi_bin/__init__.py \
   --name start-app \
    --clean \
    -D \
    --additional-hooks-dir=./hooks \
