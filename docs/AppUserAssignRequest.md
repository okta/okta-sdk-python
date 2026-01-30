# AppUserAssignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the object was created | [optional] [readonly] 
**credentials** | [**AppUserCredentials**](AppUserCredentials.md) |  | [optional] 
**external_id** | **str** | The ID of the user in the target app that&#39;s linked to the Okta application user object. This value is the native app-specific identifier or primary key for the user in the target app.  The &#x60;externalId&#x60; is set during import when the user is confirmed (reconciled) or during provisioning when the user is created in the target app. This value isn&#39;t populated for SSO app assignments (for example, SAML or SWA) because it isn&#39;t synchronized with a target app. | [optional] [readonly] 
**id** | **str** | Unique identifier for the Okta user | 
**last_sync** | **datetime** | Timestamp of the last synchronization operation. This value is only updated for apps with the &#x60;IMPORT_PROFILE_UPDATES&#x60; or &#x60;PUSH PROFILE_UPDATES&#x60; feature. | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the object was last updated | [optional] [readonly] 
**password_changed** | **datetime** | Timestamp when the application user password was last changed | [optional] [readonly] 
**profile** | **Dict[str, object]** | Specifies the default and custom profile properties for a user. Properties that are visible in the Admin Console for an app assignment can also be assigned through the API. Some properties are reference properties that are imported from the target app and can&#39;t be configured. See [profile](/openapi/okta-management/management/tag/User/#tag/User/operation/getUser!c&#x3D;200&amp;path&#x3D;profile&amp;t&#x3D;response).  | [optional] 
**scope** | **str** | Indicates if the assignment is direct (&#x60;USER&#x60;) or by group membership (&#x60;GROUP&#x60;). | [optional] 
**status** | [**AppUserStatus**](AppUserStatus.md) |  | [optional] 
**status_changed** | **datetime** | Timestamp when the application user status was last changed | [optional] [readonly] 
**sync_state** | [**AppUserSyncState**](AppUserSyncState.md) |  | [optional] 
**embedded** | **Dict[str, object]** | Embedded resources related to the application user using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification | [optional] [readonly] 
**links** | [**LinksAppAndUser**](LinksAppAndUser.md) |  | [optional] 

## Example

```python
from okta.models.app_user_assign_request import AppUserAssignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppUserAssignRequest from a JSON string
app_user_assign_request_instance = AppUserAssignRequest.from_json(json)
# print the JSON string representation of the object
print(AppUserAssignRequest.to_json())

# convert the object into a dict
app_user_assign_request_dict = app_user_assign_request_instance.to_dict()
# create an instance of AppUserAssignRequest from a dict
app_user_assign_request_from_dict = AppUserAssignRequest.from_dict(app_user_assign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


