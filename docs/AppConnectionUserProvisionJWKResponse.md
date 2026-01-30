# AppConnectionUserProvisionJWKResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwks** | [**AppConnectionUserProvisionJWKList**](AppConnectionUserProvisionJWKList.md) |  | 

## Example

```python
from okta.models.app_connection_user_provision_jwk_response import AppConnectionUserProvisionJWKResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppConnectionUserProvisionJWKResponse from a JSON string
app_connection_user_provision_jwk_response_instance = AppConnectionUserProvisionJWKResponse.from_json(json)
# print the JSON string representation of the object
print(AppConnectionUserProvisionJWKResponse.to_json())

# convert the object into a dict
app_connection_user_provision_jwk_response_dict = app_connection_user_provision_jwk_response_instance.to_dict()
# create an instance of AppConnectionUserProvisionJWKResponse from a dict
app_connection_user_provision_jwk_response_from_dict = AppConnectionUserProvisionJWKResponse.from_dict(app_connection_user_provision_jwk_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


