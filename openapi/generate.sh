#!/bin/bash

#openapi-generator-cli generate -g python -c config.yaml -i api.yaml --skip-validate-spec --server-variables=javaOpts="-Dswagger.v3.parser.max_depth=5000 -Dsnakeyaml.maxAliasesForCollections=10000"
#!/bin/bash

export JAVA_TOOL_OPTIONS="-Dswagger.v3.parser.max_depth=5000 -Dsnakeyaml.maxAliasesForCollections=10000"
java -Xmx12g -DmaxYamlCodePoints=10000000 -Dsnakeyaml.codepoint.limit=10000000 -jar openapi-generator-cli-7.7.0.jar generate -g python -c config.yaml -i api.yaml --skip-validate-spec
#openapi-generator-cli generate -g python -c config.yaml -i api.yaml --skip-validate-spec
