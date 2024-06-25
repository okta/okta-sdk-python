#!/bin/bash

openapi-generator-cli generate -g python-pydantic-v1 -o sdk -c config.json --skip-validate-spec