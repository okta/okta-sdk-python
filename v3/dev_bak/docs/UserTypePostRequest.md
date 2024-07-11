# UserTypePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The updated human-readable description of the User Type | [optional] 
**display_name** | **str** | The updated human-readable display name for the User Type | [optional] 

## Example

```python
from openapi_client.models.user_type_post_request import UserTypePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserTypePostRequest from a JSON string
user_type_post_request_instance = UserTypePostRequest.from_json(json)
# print the JSON string representation of the object
print(UserTypePostRequest.to_json())

# convert the object into a dict
user_type_post_request_dict = user_type_post_request_instance.to_dict()
# create an instance of UserTypePostRequest from a dict
user_type_post_request_from_dict = UserTypePostRequest.from_dict(user_type_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


