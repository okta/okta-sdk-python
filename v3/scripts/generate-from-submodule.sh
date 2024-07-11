#!/bin/bash

GITROOT=`git rev-parse --show-toplevel`
SPEC=$GITROOT/submodules/okta-management-openapi-spec/dist/current/management-minimal.yaml

openapi-generator-cli generate -g python -c config.yaml -i $SPEC --skip-validate-spec

