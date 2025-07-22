#!/bin/bash

#python3 generate_constants_context.py management.yaml constants_context.json
python3 update_config.py management.yaml config.yaml
openapi-generator-cli generate -g python -c config.yaml -i management.yaml --skip-validate-spec --global-property debugModels
