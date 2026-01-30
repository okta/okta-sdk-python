# BaseContextUser

Identifies the Okta user that the token was generated to authenticate and provides details of their Okta user profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the user | [optional] 
**password_changed** | **datetime** | The timestamp when the user&#39;s password was last updated | [optional] 
**profile** | [**BaseContextUserProfile**](BaseContextUserProfile.md) |  | [optional] 
**links** | [**BaseContextUserLinks**](BaseContextUserLinks.md) |  | [optional] 

## Example

```python
from okta.models.base_context_user import BaseContextUser

# TODO update the JSON string below
json = "{}"
# create an instance of BaseContextUser from a JSON string
base_context_user_instance = BaseContextUser.from_json(json)
# print the JSON string representation of the object
print(BaseContextUser.to_json())

# convert the object into a dict
base_context_user_dict = base_context_user_instance.to_dict()
# create an instance of BaseContextUser from a dict
base_context_user_from_dict = BaseContextUser.from_dict(base_context_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


