# ProvisioningDeprovisionedCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ProvisioningDeprovisionedAction**](ProvisioningDeprovisionedAction.md) |  | [optional] 

## Example

```python
from okta.models.provisioning_deprovisioned_condition import ProvisioningDeprovisionedCondition

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningDeprovisionedCondition from a JSON string
provisioning_deprovisioned_condition_instance = ProvisioningDeprovisionedCondition.from_json(json)
# print the JSON string representation of the object
print(ProvisioningDeprovisionedCondition.to_json())

# convert the object into a dict
provisioning_deprovisioned_condition_dict = provisioning_deprovisioned_condition_instance.to_dict()
# create an instance of ProvisioningDeprovisionedCondition from a dict
provisioning_deprovisioned_condition_from_dict = ProvisioningDeprovisionedCondition.from_dict(provisioning_deprovisioned_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


