# APIServiceIntegrationLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the current status of an application using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification. This object is used for dynamic discovery of related resources and lifecycle operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | [**HrefObjectClientLink**](HrefObjectClientLink.md) |  | [optional] 
**logo** | [**HrefObjectLogoLink**](HrefObjectLogoLink.md) |  | [optional] 
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 

## Example

```python
from openapi_client.models.api_service_integration_links import APIServiceIntegrationLinks

# TODO update the JSON string below
json = "{}"
# create an instance of APIServiceIntegrationLinks from a JSON string
api_service_integration_links_instance = APIServiceIntegrationLinks.from_json(json)
# print the JSON string representation of the object
print(APIServiceIntegrationLinks.to_json())

# convert the object into a dict
api_service_integration_links_dict = api_service_integration_links_instance.to_dict()
# create an instance of APIServiceIntegrationLinks from a dict
api_service_integration_links_from_dict = APIServiceIntegrationLinks.from_dict(api_service_integration_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


