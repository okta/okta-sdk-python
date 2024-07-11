# PolicyUserNameTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template** | **str** |  | [optional] 

## Example

```python
from okta.models.policy_user_name_template import PolicyUserNameTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyUserNameTemplate from a JSON string
policy_user_name_template_instance = PolicyUserNameTemplate.from_json(json)
# print the JSON string representation of the object
print(PolicyUserNameTemplate.to_json())

# convert the object into a dict
policy_user_name_template_dict = policy_user_name_template_instance.to_dict()
# create an instance of PolicyUserNameTemplate from a dict
policy_user_name_template_from_dict = PolicyUserNameTemplate.from_dict(policy_user_name_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


