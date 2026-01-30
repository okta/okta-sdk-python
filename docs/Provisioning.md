# Provisioning

Specifies the behavior for just-in-time (JIT) provisioning of an IdP user as a new Okta user and their group memberships

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ProvisioningAction**](ProvisioningAction.md) |  | [optional] 
**conditions** | [**ProvisioningConditions**](ProvisioningConditions.md) |  | [optional] 
**groups** | [**ProvisioningGroups**](ProvisioningGroups.md) |  | [optional] 
**profile_master** | **bool** | Determines if the IdP should act as a source of truth for user profile attributes | [optional] 

## Example

```python
from okta.models.provisioning import Provisioning

# TODO update the JSON string below
json = "{}"
# create an instance of Provisioning from a JSON string
provisioning_instance = Provisioning.from_json(json)
# print the JSON string representation of the object
print(Provisioning.to_json())

# convert the object into a dict
provisioning_dict = provisioning_instance.to_dict()
# create an instance of Provisioning from a dict
provisioning_from_dict = Provisioning.from_dict(provisioning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


