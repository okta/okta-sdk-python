# AppUserProfileRequestPayload

Updates the assigned user profile > **Note:** The Okta API currently doesn't support entity tags for conditional updates. As long as you're the only user updating the the user profile, Okta recommends you fetch the most recent profile with [Retrieve an Application User](/openapi/okta-management/management/tag/ApplicationUsers/#tag/ApplicationUsers/operation/getApplicationUser), apply your profile update, and then `POST` back the updated profile.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | **Dict[str, object]** | Specifies the default and custom profile properties for a user. Properties that are visible in the Admin Console for an app assignment can also be assigned through the API. Some properties are reference properties that are imported from the target app and can&#39;t be configured. See [profile](/openapi/okta-management/management/tag/User/#tag/User/operation/getUser!c&#x3D;200&amp;path&#x3D;profile&amp;t&#x3D;response).  | [optional] 

## Example

```python
from okta.models.app_user_profile_request_payload import AppUserProfileRequestPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserProfileRequestPayload from a JSON string
app_user_profile_request_payload_instance = AppUserProfileRequestPayload.from_json(json)
# print the JSON string representation of the object
print(AppUserProfileRequestPayload.to_json())

# convert the object into a dict
app_user_profile_request_payload_dict = app_user_profile_request_payload_instance.to_dict()
# create an instance of AppUserProfileRequestPayload from a dict
app_user_profile_request_payload_from_dict = AppUserProfileRequestPayload.from_dict(app_user_profile_request_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


