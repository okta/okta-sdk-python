# PolicyContextGroups

An array of Group IDs for the simulate operation. Only user IDs or Group IDs are allowed, not both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | 

## Example

```python
from openapi_client.models.policy_context_groups import PolicyContextGroups

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyContextGroups from a JSON string
policy_context_groups_instance = PolicyContextGroups.from_json(json)
# print the JSON string representation of the object
print(PolicyContextGroups.to_json())

# convert the object into a dict
policy_context_groups_dict = policy_context_groups_instance.to_dict()
# create an instance of PolicyContextGroups from a dict
policy_context_groups_form_dict = policy_context_groups.from_dict(policy_context_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


