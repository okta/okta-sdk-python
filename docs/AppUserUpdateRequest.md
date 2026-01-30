# AppUserUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**AppUserCredentials**](AppUserCredentials.md) |  | [optional] 
**profile** | **Dict[str, object]** | Specifies the default and custom profile properties for a user. Properties that are visible in the Admin Console for an app assignment can also be assigned through the API. Some properties are reference properties that are imported from the target app and can&#39;t be configured. See [profile](/openapi/okta-management/management/tag/User/#tag/User/operation/getUser!c&#x3D;200&amp;path&#x3D;profile&amp;t&#x3D;response).  | [optional] 

## Example

```python
from okta.models.app_user_update_request import AppUserUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserUpdateRequest from a JSON string
app_user_update_request_instance = AppUserUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AppUserUpdateRequest.to_json())

# convert the object into a dict
app_user_update_request_dict = app_user_update_request_instance.to_dict()
# create an instance of AppUserUpdateRequest from a dict
app_user_update_request_from_dict = AppUserUpdateRequest.from_dict(app_user_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


