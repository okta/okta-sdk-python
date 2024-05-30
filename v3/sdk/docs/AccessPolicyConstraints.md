# AccessPolicyConstraints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge** | [**KnowledgeConstraint**](KnowledgeConstraint.md) |  | [optional] 
**possession** | [**PossessionConstraint**](PossessionConstraint.md) |  | [optional] 

## Example

```python
from openapi_client.models.access_policy_constraints import AccessPolicyConstraints

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyConstraints from a JSON string
access_policy_constraints_instance = AccessPolicyConstraints.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyConstraints.to_json())

# convert the object into a dict
access_policy_constraints_dict = access_policy_constraints_instance.to_dict()
# create an instance of AccessPolicyConstraints from a dict
access_policy_constraints_form_dict = access_policy_constraints.from_dict(access_policy_constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


