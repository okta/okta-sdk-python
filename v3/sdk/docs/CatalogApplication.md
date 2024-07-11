# CatalogApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**features** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**sign_on_modes** | **List[str]** |  | [optional] 
**status** | [**CatalogApplicationStatus**](CatalogApplicationStatus.md) |  | [optional] 
**verification_status** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.catalog_application import CatalogApplication

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogApplication from a JSON string
catalog_application_instance = CatalogApplication.from_json(json)
# print the JSON string representation of the object
print(CatalogApplication.to_json())

# convert the object into a dict
catalog_application_dict = catalog_application_instance.to_dict()
# create an instance of CatalogApplication from a dict
catalog_application_from_dict = CatalogApplication.from_dict(catalog_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


