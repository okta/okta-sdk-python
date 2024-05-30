#!/bin/bash

openapi-generator-cli generate -g python -o generated -i $1 --skip-validate-spec