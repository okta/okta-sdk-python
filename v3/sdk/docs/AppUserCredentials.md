# AppUserCredentials

Specifies a user's credentials for the app. The authentication scheme of the app determines whether a username or password can be assigned to a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | [**AppUserPasswordCredential**](AppUserPasswordCredential.md) |  | [optional] 
**user_name** | **str** | Username for the app | [optional] 

## Example

```python
from okta.models.app_user_credentials import AppUserCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserCredentials from a JSON string
app_user_credentials_instance = AppUserCredentials.from_json(json)
# print the JSON string representation of the object
print(AppUserCredentials.to_json())

# convert the object into a dict
app_user_credentials_dict = app_user_credentials_instance.to_dict()
# create an instance of AppUserCredentials from a dict
app_user_credentials_from_dict = AppUserCredentials.from_dict(app_user_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


