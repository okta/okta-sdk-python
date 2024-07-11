# APIServiceIntegrationInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_guide_url** | **str** | The URL to the API service integration configuration guide | [optional] [readonly] 
**created_at** | **str** | Timestamp when the API Service Integration instance was created | [optional] [readonly] 
**created_by** | **str** | The user ID of the API Service Integration instance creator | [optional] [readonly] 
**granted_scopes** | **List[str]** | The list of Okta management scopes granted to the API Service Integration instance. See [Okta management OAuth 2.0 scopes](/oauth2/#okta-admin-management). | [optional] 
**id** | **str** | The ID of the API Service Integration instance | [optional] [readonly] 
**name** | **str** | The name of the API service integration that corresponds with the &#x60;type&#x60; property. This is the full name of the API service integration listed in the Okta Integration Network (OIN) catalog. | [optional] [readonly] 
**type** | **str** | The type of the API service integration. This string is an underscore-concatenated, lowercased API service integration name. For example, &#x60;my_api_log_integration&#x60;. | [optional] 
**links** | [**APIServiceIntegrationLinks**](APIServiceIntegrationLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.api_service_integration_instance import APIServiceIntegrationInstance

# TODO update the JSON string below
json = "{}"
# create an instance of APIServiceIntegrationInstance from a JSON string
api_service_integration_instance_instance = APIServiceIntegrationInstance.from_json(json)
# print the JSON string representation of the object
print(APIServiceIntegrationInstance.to_json())

# convert the object into a dict
api_service_integration_instance_dict = api_service_integration_instance_instance.to_dict()
# create an instance of APIServiceIntegrationInstance from a dict
api_service_integration_instance_from_dict = APIServiceIntegrationInstance.from_dict(api_service_integration_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


