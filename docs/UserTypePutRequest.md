# UserTypePutRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The human-readable description of the user type | 
**display_name** | **str** | The human-readable name of the user type | 
**name** | **str** | The name of the existing type | 

## Example

```python
from okta.models.user_type_put_request import UserTypePutRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserTypePutRequest from a JSON string
user_type_put_request_instance = UserTypePutRequest.from_json(json)
# print the JSON string representation of the object
print(UserTypePutRequest.to_json())

# convert the object into a dict
user_type_put_request_dict = user_type_put_request_instance.to_dict()
# create an instance of UserTypePutRequest from a dict
user_type_put_request_from_dict = UserTypePutRequest.from_dict(user_type_put_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


