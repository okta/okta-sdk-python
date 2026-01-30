# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated** | **datetime** | The timestamp when the user status transitioned to &#x60;ACTIVE&#x60; | [optional] [readonly] 
**created** | **datetime** | The timestamp when the user was created | [optional] [readonly] 
**credentials** | [**UserCredentials**](UserCredentials.md) |  | [optional] 
**id** | **str** | The unique key for the user | [optional] [readonly] 
**last_login** | **datetime** | The timestamp of the last login | [optional] [readonly] 
**last_updated** | **datetime** | The timestamp when the user was last updated | [optional] [readonly] 
**password_changed** | **datetime** | The timestamp when the user&#39;s password was last updated | [optional] [readonly] 
**profile** | [**UserProfile**](UserProfile.md) |  | [optional] 
**realm_id** | **str** | The ID of the realm in which the user is residing. See [Realms](/openapi/okta-management/management/tag/Realm/). | [optional] [readonly] 
**status** | [**UserStatus**](UserStatus.md) |  | [optional] 
**status_changed** | **datetime** | The timestamp when the status of the user last changed | [optional] [readonly] 
**transitioning_to_status** | **str** | The target status of an in-progress asynchronous status transition. This property is only returned if the user&#39;s state is transitioning. | [optional] [readonly] 
**type** | [**UserType**](UserType.md) |  | [optional] 
**embedded** | **Dict[str, object]** | Embedded resources related to the user using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification | [optional] [readonly] 
**links** | [**UserLinks**](UserLinks.md) |  | [optional] 

## Example

```python
from okta.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


