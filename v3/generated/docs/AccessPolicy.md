# AccessPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**PolicyRuleConditions**](PolicyRuleConditions.md) |  | [optional] 

## Example

```python
from openapi_client.models.access_policy import AccessPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicy from a JSON string
access_policy_instance = AccessPolicy.from_json(json)
# print the JSON string representation of the object
print(AccessPolicy.to_json())

# convert the object into a dict
access_policy_dict = access_policy_instance.to_dict()
# create an instance of AccessPolicy from a dict
access_policy_form_dict = access_policy.from_dict(access_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


