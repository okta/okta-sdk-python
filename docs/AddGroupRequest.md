# AddGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**OktaUserGroupProfile**](OktaUserGroupProfile.md) |  | [optional] 

## Example

```python
from okta.models.add_group_request import AddGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddGroupRequest from a JSON string
add_group_request_instance = AddGroupRequest.from_json(json)
# print the JSON string representation of the object
print(AddGroupRequest.to_json())

# convert the object into a dict
add_group_request_dict = add_group_request_instance.to_dict()
# create an instance of AddGroupRequest from a dict
add_group_request_from_dict = AddGroupRequest.from_dict(add_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


