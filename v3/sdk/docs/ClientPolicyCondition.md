# ClientPolicyCondition

Specifies which clients are included in the Policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | Which clients are included in the Policy | [optional] 

## Example

```python
from openapi_client.models.client_policy_condition import ClientPolicyCondition

# TODO update the JSON string below
json = "{}"
# create an instance of ClientPolicyCondition from a JSON string
client_policy_condition_instance = ClientPolicyCondition.from_json(json)
# print the JSON string representation of the object
print(ClientPolicyCondition.to_json())

# convert the object into a dict
client_policy_condition_dict = client_policy_condition_instance.to_dict()
# create an instance of ClientPolicyCondition from a dict
client_policy_condition_form_dict = client_policy_condition.from_dict(client_policy_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


