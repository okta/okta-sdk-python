# AppUserCredentials

Specifies a user's credentials for the app. This parameter can be omitted for apps with [sign-on mode](/openapi/okta-management/management/tag/Application/#tag/Application/operation/getApplication!c=200&path=0/signOnMode&t=response) (`signOnMode`) or [authentication schemes](/openapi/okta-management/management/tag/Application/#tag/Application/operation/getApplication!c=200&path=0/credentials/scheme&t=response) (`credentials.scheme`) that don't require credentials. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | [**AppUserPasswordCredential**](AppUserPasswordCredential.md) |  | [optional] 
**user_name** | **str** | The user&#39;s username in the app  &gt; **Note:** The [userNameTemplate](/openapi/okta-management/management/tag/Application/#tag/Application/operation/createApplication!path&#x3D;0/credentials/userNameTemplate&amp;t&#x3D;request) in the application object defines the default username generated when a user is assigned to that app. &gt; If you attempt to assign a username or password to an app with an incompatible [authentication scheme](/openapi/okta-management/management/tag/Application/#tag/Application/operation/createApplication!path&#x3D;0/credentials/scheme&amp;t&#x3D;request), the following error is returned: &gt; \&quot;Credentials should not be set on this resource based on the scheme.\&quot; | [optional] 

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


