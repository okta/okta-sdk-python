# AppConnectionUserProvisionJWKList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | [**List[JsonWebKey]**](JsonWebKey.md) |  | 

## Example

```python
from okta.models.app_connection_user_provision_jwk_list import AppConnectionUserProvisionJWKList

# TODO update the JSON string below
json = "{}"
# create an instance of AppConnectionUserProvisionJWKList from a JSON string
app_connection_user_provision_jwk_list_instance = AppConnectionUserProvisionJWKList.from_json(json)
# print the JSON string representation of the object
print(AppConnectionUserProvisionJWKList.to_json())

# convert the object into a dict
app_connection_user_provision_jwk_list_dict = app_connection_user_provision_jwk_list_instance.to_dict()
# create an instance of AppConnectionUserProvisionJWKList from a dict
app_connection_user_provision_jwk_list_from_dict = AppConnectionUserProvisionJWKList.from_dict(app_connection_user_provision_jwk_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


