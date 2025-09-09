# ProvisioningGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ProvisioningGroupsAction**](ProvisioningGroupsAction.md) |  | [optional] 
**assignments** | **List[str]** |  | [optional] 
**filter** | **List[str]** |  | [optional] 
**source_attribute_name** | **str** |  | [optional] 

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


