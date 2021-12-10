package org.example.swagger.codegen;

import java.util.Map;

public class Discriminator {
    private final String parentDefName;

    private final String fieldName;

    private final Map<String, String> valueDefMap;

    public Discriminator(String parentDefName, String fieldName, Map<String, String> valueDefMap) {
        this.parentDefName = parentDefName;
        this.fieldName = fieldName;
        this.valueDefMap = valueDefMap;
    }

    public String getParentDefName() {
        return parentDefName;
    }

    public String getFieldName() {
        return fieldName;
    }

    public Map<String, String> getValueDefMap() {
        return valueDefMap;
    }

    public String getDefaultFieldValue(String key) {
        return valueDefMap.get(key);
    }
}
