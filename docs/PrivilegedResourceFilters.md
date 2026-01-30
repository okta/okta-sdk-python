# PrivilegedResourceFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_groups** | [**List[AppGroup]**](AppGroup.md) | Array of app groups whose members might be privileged app users | [optional] 
**organizational_units** | [**List[OrganizationalUnit]**](OrganizationalUnit.md) | Array of organizational units where privileged app users are present | [optional] 

## Example

```python
from okta.models.privileged_resource_filters import PrivilegedResourceFilters

# TODO update the JSON string below
json = "{}"
# create an instance of PrivilegedResourceFilters from a JSON string
privileged_resource_filters_instance = PrivilegedResourceFilters.from_json(json)
# print the JSON string representation of the object
print(PrivilegedResourceFilters.to_json())

# convert the object into a dict
privileged_resource_filters_dict = privileged_resource_filters_instance.to_dict()
# create an instance of PrivilegedResourceFilters from a dict
privileged_resource_filters_from_dict = PrivilegedResourceFilters.from_dict(privileged_resource_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


