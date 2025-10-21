# ProvisioningConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprovisioned** | [**ProvisioningDeprovisionedCondition**](ProvisioningDeprovisionedCondition.md) |  | [optional] 
**suspended** | [**ProvisioningSuspendedCondition**](ProvisioningSuspendedCondition.md) |  | [optional] 

## Example

```python
from okta.models.provisioning_conditions import ProvisioningConditions

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningConditions from a JSON string
provisioning_conditions_instance = ProvisioningConditions.from_json(json)
# print the JSON string representation of the object
print(ProvisioningConditions.to_json())

# convert the object into a dict
provisioning_conditions_dict = provisioning_conditions_instance.to_dict()
# create an instance of ProvisioningConditions from a dict
provisioning_conditions_from_dict = ProvisioningConditions.from_dict(provisioning_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


