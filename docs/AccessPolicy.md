# AccessPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | **str** | Policy conditions aren&#39;t supported. Conditions are applied at the rule level for this policy type. | [optional] 

## Example

```python
from okta.models.access_policy import AccessPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicy from a JSON string
access_policy_instance = AccessPolicy.from_json(json)
# print the JSON string representation of the object
print(AccessPolicy.to_json())

# convert the object into a dict
access_policy_dict = access_policy_instance.to_dict()
# create an instance of AccessPolicy from a dict
access_policy_from_dict = AccessPolicy.from_dict(access_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


