# RoleTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignment_type** | **str** | The assignment type of how the user receives this target | [optional] [readonly] 
**expiration** | **datetime** | The expiry time stamp of the associated target. It&#39;s only included in the response if the associated target will expire. | [optional] [readonly] 
**orn** | **str** | The [Okta Resource Name (ORN)](https://support.okta.com/help/s/article/understanding-okta-resource-name-orn) of the app target or group target | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.role_target import RoleTarget

# TODO update the JSON string below
json = "{}"
# create an instance of RoleTarget from a JSON string
role_target_instance = RoleTarget.from_json(json)
# print the JSON string representation of the object
print(RoleTarget.to_json())

# convert the object into a dict
role_target_dict = role_target_instance.to_dict()
# create an instance of RoleTarget from a dict
role_target_from_dict = RoleTarget.from_dict(role_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


