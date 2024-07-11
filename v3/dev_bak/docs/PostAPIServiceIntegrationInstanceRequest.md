# PostAPIServiceIntegrationInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**granted_scopes** | **List[str]** | The list of Okta management scopes granted to the API Service Integration instance. See [Okta management OAuth 2.0 scopes](/oauth2/#okta-admin-management). | 
**type** | **str** | The type of the API service integration. This string is an underscore-concatenated, lowercased API service integration name. For example, &#x60;my_api_log_integration&#x60;. | 

## Example

```python
from openapi_client.models.post_api_service_integration_instance_request import PostAPIServiceIntegrationInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAPIServiceIntegrationInstanceRequest from a JSON string
post_api_service_integration_instance_request_instance = PostAPIServiceIntegrationInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(PostAPIServiceIntegrationInstanceRequest.to_json())

# convert the object into a dict
post_api_service_integration_instance_request_dict = post_api_service_integration_instance_request_instance.to_dict()
# create an instance of PostAPIServiceIntegrationInstanceRequest from a dict
post_api_service_integration_instance_request_from_dict = PostAPIServiceIntegrationInstanceRequest.from_dict(post_api_service_integration_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


