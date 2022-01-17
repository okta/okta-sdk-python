package org.example.swagger.codegen;

import io.swagger.codegen.v3.CodegenModel;
import io.swagger.codegen.v3.CodegenOperation;
import io.swagger.codegen.v3.CodegenParameter;
import io.swagger.codegen.v3.SupportingFile;
import io.swagger.codegen.v3.generators.python.PythonClientCodegen;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.oas.models.media.Schema;
import org.apache.commons.lang3.StringUtils;
import org.yaml.snakeyaml.Yaml;

import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class CustomPythonClientCodegen extends PythonClientCodegen {

    protected Map<String, Object> rawSwaggerConfig;
    protected Map<String, Discriminator> discriminatorMap = new HashMap<>();
    protected Map<String, String> reverseDiscriminatorMap = new HashMap<>();

    public CustomPythonClientCodegen() {
        super();

        this.additionalProperties.put("packageName", "okta");
    }

    @Override
    public void preprocessOpenAPI(OpenAPI openAPI) {

        //raw config
        try {
            rawSwaggerConfig = new Yaml().loadAs(inputSpec, Map.class);
        } catch (Exception e) {
            throw new IllegalStateException("Failed to parse inputSpec variable", e);
        }

        super.preprocessOpenAPI(openAPI);

        this.buildDiscriminationMap(openAPI);
    }

    @Override
    public void processOpts() {
        super.processOpts();

        replaceDestinationFilename("api_client.py", "swagger_api_client.py");
    }

    void replaceDestinationFilename(String oldName, String newName) {
        for (SupportingFile supportingFile: supportingFiles) {
            if(supportingFile.destinationFilename.equals(oldName)) {
                supportingFile.destinationFilename = newName;
            }
        }
    }

    @Override
    public String getName() {
        return "python_test_example";
    }

    @Override
    public CodegenModel fromModel(String name, Schema model, Map<String, Schema> allDefinitions) {
        CodegenModel codegenModel = super.fromModel(name, model, allDefinitions);
        // super add these imports, and we don't want that dependency
        codegenModel.imports.remove("ApiModel");

        //TODO Review this and optimize if possible
        if(codegenModel.discriminator != null) {
            Map<String, String> map = codegenModel.discriminator.getMapping();
            if(map != null) {
                for (Map.Entry<String, String> item : map.entrySet()) {
                    if(item.getValue().lastIndexOf("/") != -1) {
                        item.setValue(toApiName(item.getValue().substring(item.getValue().lastIndexOf("/"))));
                    }
                }
            }
        }

        if (model.getExtensions() !=null && model.getExtensions().containsKey("x-baseType")) {
            String baseType = (String) model.getExtensions().get("x-baseType");
            codegenModel.vendorExtensions.put("baseType", toModelName(baseType));
            codegenModel.imports.add(toModelName(baseType));
        }

        Collection<CodegenOperation> operations = (Collection<CodegenOperation>) codegenModel.vendorExtensions.get("operations");
        if (operations != null) {
            operations.forEach(op -> {
                if (op.returnType != null) {
                    codegenModel.imports.add(op.returnType);
                }
                if (op.allParams != null) {
                    op.allParams.stream()
                            .filter(param -> needToImport(param.dataType))
                            .forEach(param -> codegenModel.imports.add(param.dataType));
                }
            });
        }

        if(model.getExtensions() != null) {
            String parent = (String) model.getExtensions().get("x-okta-parent");
            if (StringUtils.isNotEmpty(parent)) {
                codegenModel.parent = toApiName(parent.substring(parent.lastIndexOf("/")));
                codegenModel.imports.add(codegenModel.parent);

                // figure out the resourceClass if this model has a parent
                String discriminatorRoot = getRootDiscriminator(name);
                if (discriminatorRoot != null) {
                    model.getExtensions().put("discriminatorRoot", discriminatorRoot);
                }

            }
        }

        return codegenModel;
    }

    @Override
    public String toApiName(String name) {
        return name.length() == 0 ? "object" : camelize(name);
    }

    @Override
    public String toVarName(String name) {

        // sanitize name
        name = sanitizeName(name); // FIXME: a parameter should not be assigned. Also declare the methods parameters as 'final'.

        // remove dollar sign
        name = name.replaceAll("$", "");

        // if it's all uppper case, convert to lower case
        if (name.matches("^[A-Z_]*$")) {
            name = name.toLowerCase();
        }

        // underscore the variable name
        // petId => pet_id
        name = camelToSnakeAndToLower(name);

        // remove leading underscore
        name = name.replaceAll("^_*", "");

        // for reserved word or word starting with number, append _
        if (isReservedWord(name) || name.matches("^\\d.*")) {
            name = escapeReservedWord(name);
        }

        return name;
    }

    @Override
    public CodegenOperation fromOperation(String path, String httpMethod, Operation operation, Map<String, Schema> schemas, OpenAPI openAPI) {

        CodegenOperation codegenOperation = super.fromOperation(path, httpMethod, operation, schemas, openAPI);

        //put a weight for each parameter
        codegenOperation.getContents().forEach(x -> setParamWeight(x.getParameters()));

        //sort required only parameters according to param weight
        codegenOperation.getContents().forEach(x -> x.getParameters().sort((left, right) -> {
            if (left.required && right.required) {
                return Integer.compare(
                        (Integer) left.getVendorExtensions().get("param-weight"),
                        (Integer) right.getVendorExtensions().get("param-weight")
                );
            } else {
                return 0;
            }
        }));

        return codegenOperation;
    }

    private void setParamWeight(List<CodegenParameter> list) {
        list.forEach(x -> {
            if(x.getVendorExtensions().containsKey("x-is-path-param")) {
                x.getVendorExtensions().put("param-weight", 0);
            } else if(x.getVendorExtensions().containsKey("x-is-body-param")) {
                x.getVendorExtensions().put("param-weight", 1);
            } else if(x.getVendorExtensions().containsKey("x-is-query-param")) {
                x.getVendorExtensions().put("param-weight", 2);
            } else if(x.getVendorExtensions().containsKey("x-is-form-data-param")) {
                x.getVendorExtensions().put("param-weight", 3);
            } else {
                x.getVendorExtensions().put("param-weight", 4);
            }
        });
    }

    private String camelToSnakeAndToLower(String camelString) {

        String ret = camelString.replaceAll("([A-Za-z]+)([0-9]+)", "$1_$2")
                .replaceAll("([0-9])([A-Za-z]+)", "$1_$2")
                .replaceAll("([A-Z]+)([A-Z][a-z])", "$1_$2")
                .replaceAll("([a-z])([A-Z])", "$1_$2");
        return ret.toLowerCase();
    }

    private String getRootDiscriminator(String name) {
        String result = reverseDiscriminatorMap.get(name);

        if (result != null) {
            String parentResult = getRootDiscriminator(result);
            if (parentResult != null) {
                result = parentResult;
            }
        }
        return result;
    }

    protected void buildDiscriminationMap(OpenAPI openAPI) {
        openAPI.getComponents().getSchemas().forEach((name, model) -> {
            if (model.getDiscriminator() != null && model.getDiscriminator().getMapping() != null) {
                String propertyName = model.getDiscriminator().getPropertyName();
                Map<String, String> mapping = model.getDiscriminator().getMapping().entrySet().stream()
                        .collect(
                                Collectors.toMap(
                                        e -> e.getValue().substring(e.getValue().lastIndexOf('/') + 1),
                                        Map.Entry::getKey,
                                        (oldValue, newValue) -> newValue
                                )
                        );
                mapping.forEach((key, value) -> reverseDiscriminatorMap.put(key, name));
                discriminatorMap.put(name, new Discriminator(name, propertyName, mapping));
            }
        });
    }
}
