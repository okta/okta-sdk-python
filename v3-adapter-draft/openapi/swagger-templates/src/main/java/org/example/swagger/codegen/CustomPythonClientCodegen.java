package org.example.swagger.codegen;

import io.swagger.codegen.v3.CodegenModel;
import io.swagger.codegen.v3.CodegenOperation;
import io.swagger.codegen.v3.SupportingFile;
import io.swagger.codegen.v3.generators.python.PythonClientCodegen;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.media.Schema;
import org.apache.commons.lang3.StringUtils;
import org.yaml.snakeyaml.Yaml;

import java.io.File;
import java.util.Collection;
import java.util.HashMap;
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
