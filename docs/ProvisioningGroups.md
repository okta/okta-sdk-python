# ProvisioningGroups

Provisioning settings for a user's group memberships

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ProvisioningGroupsAction**](ProvisioningGroupsAction.md) |  | [optional] 
**assignments** | **List[str]** | List of &#x60;OKTA_GROUP&#x60; group identifiers to add an IdP user as a member with the &#x60;ASSIGN&#x60; action | [optional] 
**filter** | **List[str]** | Allowlist of &#x60;OKTA_GROUP&#x60; group identifiers for the &#x60;APPEND&#x60; or &#x60;SYNC&#x60; provisioning action | [optional] 
**source_attribute_name** | **str** | IdP user profile attribute name (case-insensitive) for an array value that contains group memberships | [optional] 

## Example

```python
from okta.models.provisioning_groups import ProvisioningGroups

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningGroups from a JSON string
provisioning_groups_instance = ProvisioningGroups.from_json(json)
# print the JSON string representation of the object
print(ProvisioningGroups.to_json())

# convert the object into a dict
provisioning_groups_dict = provisioning_groups_instance.to_dict()
# create an instance of ProvisioningGroups from a dict
provisioning_groups_from_dict = ProvisioningGroups.from_dict(provisioning_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


