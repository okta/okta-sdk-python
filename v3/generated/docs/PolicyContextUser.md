# PolicyContextUser

The user ID for the simulate operation. Only user IDs or Group IDs are allowed, not both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID number for the user. | 

## Example

```python
from openapi_client.models.policy_context_user import PolicyContextUser

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyContextUser from a JSON string
policy_context_user_instance = PolicyContextUser.from_json(json)
# print the JSON string representation of the object
print(PolicyContextUser.to_json())

# convert the object into a dict
policy_context_user_dict = policy_context_user_instance.to_dict()
# create an instance of PolicyContextUser from a dict
policy_context_user_form_dict = policy_context_user.from_dict(policy_context_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


