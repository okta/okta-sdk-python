# OrgContactTypeObj


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_type** | [**OrgContactType**](OrgContactType.md) |  | [optional] 
**links** | [**OrgTechnicalContactTypeLinks**](OrgTechnicalContactTypeLinks.md) |  | [optional] 

## Example

```python
from okta.models.org_contact_type_obj import OrgContactTypeObj

# TODO update the JSON string below
json = "{}"
# create an instance of OrgContactTypeObj from a JSON string
org_contact_type_obj_instance = OrgContactTypeObj.from_json(json)
# print the JSON string representation of the object
print(OrgContactTypeObj.to_json())

# convert the object into a dict
org_contact_type_obj_dict = org_contact_type_obj_instance.to_dict()
# create an instance of OrgContactTypeObj from a dict
org_contact_type_obj_from_dict = OrgContactTypeObj.from_dict(org_contact_type_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


