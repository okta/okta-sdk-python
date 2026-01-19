# CatalogApplication

An app in the OIN catalog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Category for the app in the OIN catalog | [optional] [readonly] 
**description** | **str** | Description of the app in the OIN catalog | [optional] [readonly] 
**display_name** | **str** | OIN catalog app display name | [optional] [readonly] 
**features** | **List[str]** | Features supported by the app. See app [features](/openapi/okta-management/management/tag/Application/#tag/Application/operation/listApplications!c&#x3D;200&amp;path&#x3D;0/features&amp;t&#x3D;response). | [optional] [readonly] 
**id** | **str** | ID of the app instance. Okta returns this property only for apps not in the OIN catalog. | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the object was last updated | [optional] [readonly] 
**name** | **str** | App key name. For OIN catalog apps, this is a unique key for the app definition. | [optional] 
**sign_on_modes** | **List[str]** | Authentication mode for the app. See app [signOnMode](/openapi/okta-management/management/tag/Application/#tag/Application/operation/listApplications!c&#x3D;200&amp;path&#x3D;0/signOnMode&amp;t&#x3D;response). | [optional] 
**status** | [**CatalogApplicationStatus**](CatalogApplicationStatus.md) |  | [optional] 
**verification_status** | **str** | OIN verification status of the catalog app | [optional] 
**website** | **str** | Website of the OIN catalog app | [optional] 
**links** | [**CatalogApplicationLinks**](CatalogApplicationLinks.md) |  | [optional] 

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


