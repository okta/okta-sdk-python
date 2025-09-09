# ProvisioningSuspendedCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ProvisioningSuspendedAction**](ProvisioningSuspendedAction.md) |  | [optional] 

## Example

```python
from okta.models.provisioning_suspended_condition import ProvisioningSuspendedCondition

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningSuspendedCondition from a JSON string
provisioning_suspended_condition_instance = ProvisioningSuspendedCondition.from_json(json)
# print the JSON string representation of the object
print(ProvisioningSuspendedCondition.to_json())

# convert the object into a dict
provisioning_suspended_condition_dict = provisioning_suspended_condition_instance.to_dict()
# create an instance of ProvisioningSuspendedCondition from a dict
provisioning_suspended_condition_from_dict = ProvisioningSuspendedCondition.from_dict(provisioning_suspended_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


