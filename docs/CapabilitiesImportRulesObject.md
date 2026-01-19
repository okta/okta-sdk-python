# CapabilitiesImportRulesObject

Defines user import rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_create_and_match** | [**CapabilitiesImportRulesUserCreateAndMatchObject**](CapabilitiesImportRulesUserCreateAndMatchObject.md) |  | [optional] 

## Example

```python
from okta.models.capabilities_import_rules_object import CapabilitiesImportRulesObject

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesImportRulesObject from a JSON string
capabilities_import_rules_object_instance = CapabilitiesImportRulesObject.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesImportRulesObject.to_json())

# convert the object into a dict
capabilities_import_rules_object_dict = capabilities_import_rules_object_instance.to_dict()
# create an instance of CapabilitiesImportRulesObject from a dict
capabilities_import_rules_object_from_dict = CapabilitiesImportRulesObject.from_dict(capabilities_import_rules_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


