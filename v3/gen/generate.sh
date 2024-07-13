#!/bin/bash

openapi-generator-cli generate -g python -c config.yaml -i management.yaml --skip-validate-spec
