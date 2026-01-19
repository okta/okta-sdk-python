# AppInstanceAuthorizationServer

Authorization server for app instance connections

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_url** | **str** | Issuer URL for the authorization server | 

## Example

```python
from okta.models.app_instance_authorization_server import AppInstanceAuthorizationServer

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstanceAuthorizationServer from a JSON string
app_instance_authorization_server_instance = AppInstanceAuthorizationServer.from_json(json)
# print the JSON string representation of the object
print(AppInstanceAuthorizationServer.to_json())

# convert the object into a dict
app_instance_authorization_server_dict = app_instance_authorization_server_instance.to_dict()
# create an instance of AppInstanceAuthorizationServer from a dict
app_instance_authorization_server_from_dict = AppInstanceAuthorizationServer.from_dict(app_instance_authorization_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


