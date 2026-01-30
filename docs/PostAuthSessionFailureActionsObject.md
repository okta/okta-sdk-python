# PostAuthSessionFailureActionsObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 

## Example

```python
from okta.models.post_auth_session_failure_actions_object import PostAuthSessionFailureActionsObject

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthSessionFailureActionsObject from a JSON string
post_auth_session_failure_actions_object_instance = PostAuthSessionFailureActionsObject.from_json(json)
# print the JSON string representation of the object
print(PostAuthSessionFailureActionsObject.to_json())

# convert the object into a dict
post_auth_session_failure_actions_object_dict = post_auth_session_failure_actions_object_instance.to_dict()
# create an instance of PostAuthSessionFailureActionsObject from a dict
post_auth_session_failure_actions_object_from_dict = PostAuthSessionFailureActionsObject.from_dict(post_auth_session_failure_actions_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


