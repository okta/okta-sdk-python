# APIServiceIntegrationInstanceSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret** | **str** | The OAuth 2.0 client secret string. The client secret string is returned in the response of a Secret creation request. In other responses (such as list, activate, or deactivate requests), the client secret is returned as an undisclosed hashed value. | [readonly] 
**created** | **str** | Timestamp when the API Service Integration instance Secret was created | [readonly] 
**id** | **str** | The ID of the API Service Integration instance Secret | [readonly] 
**last_updated** | **str** | Timestamp when the API Service Integration instance Secret was updated | [readonly] 
**secret_hash** | **str** | OAuth 2.0 client secret string hash | [readonly] 
**status** | **str** | Status of the API Service Integration instance Secret | 
**links** | [**APIServiceIntegrationSecretLinks**](APIServiceIntegrationSecretLinks.md) |  | 

## Example

```python
from openapi_client.models.api_service_integration_instance_secret import APIServiceIntegrationInstanceSecret

# TODO update the JSON string below
json = "{}"
# create an instance of APIServiceIntegrationInstanceSecret from a JSON string
api_service_integration_instance_secret_instance = APIServiceIntegrationInstanceSecret.from_json(json)
# print the JSON string representation of the object
print(APIServiceIntegrationInstanceSecret.to_json())

# convert the object into a dict
api_service_integration_instance_secret_dict = api_service_integration_instance_secret_instance.to_dict()
# create an instance of APIServiceIntegrationInstanceSecret from a dict
api_service_integration_instance_secret_form_dict = api_service_integration_instance_secret.from_dict(api_service_integration_instance_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


