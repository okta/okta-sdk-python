#!/bin/bash

openapi-generator-cli generate -g python -o sdk -i $1 --skip-validate-spec