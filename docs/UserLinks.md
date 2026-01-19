# UserLinks

Specifies link relations (see [Web Linking](https://datatracker.ietf.org/doc/html/rfc8288) available for the current status of a user. The links object is used for dynamic discovery of related resources, lifecycle operations, and credential operations. The links object is read-only.  For an individual user result, the links object contains a full set of link relations available for that user as determined by your policies. For a collection of users, the links object contains only the `self` link. Operations that return a collection of users include [List all users](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/User/#tag/User/operation/listUsers) and [List all group member users](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/#tag/Group/operation/listGroupUsers).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObject**](HrefObject.md) | URL to the individual user | [optional] 
**activate** | [**HrefObject**](HrefObject.md) | URL to activate the user | [optional] 
**reset_password** | [**HrefObject**](HrefObject.md) | URL to reset the user&#39;s password | [optional] 
**reset_factors** | [**HrefObject**](HrefObject.md) | URL to reset the user&#39;s factors | [optional] 
**expire_password** | [**HrefObject**](HrefObject.md) | URL to expire the user&#39;s password | [optional] 
**forgot_password** | [**HrefObject**](HrefObject.md) | URL to initiate a forgot password operation | [optional] 
**change_recovery_question** | [**HrefObject**](HrefObject.md) | URL to change the user&#39;s recovery question | [optional] 
**deactivate** | [**HrefObject**](HrefObject.md) | URL to deactivate a user | [optional] 
**reactivate** | [**HrefObject**](HrefObject.md) | URL to reactivate the user | [optional] 
**change_password** | [**HrefObject**](HrefObject.md) | URL to change the user&#39;s password | [optional] 
**var_schema** | [**HrefObject**](HrefObject.md) | URL to the user&#39;s profile schema | [optional] 
**suspend** | [**HrefObject**](HrefObject.md) | URL to suspend the user | [optional] 
**unsuspend** | [**HrefObject**](HrefObject.md) | URL to unsuspend the user | [optional] 
**unlock** | [**HrefObject**](HrefObject.md) | URL to unlock the locked-out user | [optional] 
**type** | [**HrefObject**](HrefObject.md) | URL to the user type | [optional] 

## Example

```python
from okta.models.user_links import UserLinks

# TODO update the JSON string below
json = "{}"
# create an instance of UserLinks from a JSON string
user_links_instance = UserLinks.from_json(json)
# print the JSON string representation of the object
print(UserLinks.to_json())

# convert the object into a dict
user_links_dict = user_links_instance.to_dict()
# create an instance of UserLinks from a dict
user_links_from_dict = UserLinks.from_dict(user_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


