# StandardRoleEmbeddedTargetsCatalog

App targets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**List[CatalogApplication]**](CatalogApplication.md) |  | [optional] 

## Example

```python
from okta.models.standard_role_embedded_targets_catalog import StandardRoleEmbeddedTargetsCatalog

# TODO update the JSON string below
json = "{}"
# create an instance of StandardRoleEmbeddedTargetsCatalog from a JSON string
standard_role_embedded_targets_catalog_instance = StandardRoleEmbeddedTargetsCatalog.from_json(json)
# print the JSON string representation of the object
print(StandardRoleEmbeddedTargetsCatalog.to_json())

# convert the object into a dict
standard_role_embedded_targets_catalog_dict = standard_role_embedded_targets_catalog_instance.to_dict()
# create an instance of StandardRoleEmbeddedTargetsCatalog from a dict
standard_role_embedded_targets_catalog_from_dict = StandardRoleEmbeddedTargetsCatalog.from_dict(standard_role_embedded_targets_catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


