#!/bin/bash

#openapi-generator-cli generate -g python -c config.yaml -i api.yaml --skip-validate-spec --server-variables=javaOpts="-Dswagger.v3.parser.max_depth=5000 -Dsnakeyaml.maxAliasesForCollections=10000"
#!/bin/bash

export JAVA_TOOL_OPTIONS="-Dswagger.v3.parser.max_depth=5000 -Dsnakeyaml.maxAliasesForCollections=10000"

openapi-generator-cli generate -g python -c config.yaml -i api.yaml --skip-validate-spec
