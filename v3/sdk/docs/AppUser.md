# AppUser

The App User object defines a user's app-specific profile and credentials for an app.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the App User object was created | [readonly] 
**credentials** | [**AppUserCredentials**](AppUserCredentials.md) |  | [optional] 
**external_id** | **str** | The ID of the user in the target app that&#39;s linked to the Okta App User object. This value is the native app-specific identifier or primary key for the user in the target app.  The &#x60;externalId&#x60; is set during import when the user is confirmed (reconciled) or during provisioning when the user has been successfully created in the target app. This value isn&#39;t populated for SSO app assignments (for example, SAML or SWA) because it isn&#39;t synchronized with a target app. | [optional] [readonly] 
**id** | **str** | Unique identifier of the App User object (only required for apps with &#x60;signOnMode&#x60; or authentication schemes that don&#39;t require credentials) | [optional] 
**last_sync** | **datetime** | Timestamp of the last synchronization operation. This value is only updated for apps with the &#x60;IMPORT_PROFILE_UPDATES&#x60; or &#x60;PUSH PROFILE_UPDATES&#x60; feature. | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when App User was last updated | [readonly] 
**password_changed** | **datetime** | Timestamp when the App User password was last changed | [optional] [readonly] 
**profile** | **Dict[str, object]** | App user profiles are app-specific and can be customized by the Profile Editor in the Admin Console. SSO apps typically don&#39;t support app user profiles, while apps with user provisioning features have app-specific profiles. Properties that are visible in the Admin Console for an app assignment can also be assigned through the API. Some properties are reference properties that are imported from the target app and can&#39;t be configured. | [optional] 
**scope** | **str** | Toggles the assignment between user or group scope | 
**status** | [**AppUserStatus**](AppUserStatus.md) |  | 
**status_changed** | **datetime** | Timestamp when the App User status was last changed | [readonly] 
**sync_state** | [**AppUserSyncState**](AppUserSyncState.md) |  | [optional] 
**embedded** | **Dict[str, object]** | Embedded resources related to the App User using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification | [optional] [readonly] 
**links** | [**LinksAppAndUser**](LinksAppAndUser.md) |  | 

## Example

```python
from openapi_client.models.app_user import AppUser

# TODO update the JSON string below
json = "{}"
# create an instance of AppUser from a JSON string
app_user_instance = AppUser.from_json(json)
# print the JSON string representation of the object
print(AppUser.to_json())

# convert the object into a dict
app_user_dict = app_user_instance.to_dict()
# create an instance of AppUser from a dict
app_user_form_dict = app_user.from_dict(app_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


