# OrgTechnicalContactType

Org technical contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_type** | [**OrgContactType**](OrgContactType.md) |  | [optional] 
**links** | [**OrgTechnicalContactTypeLinks**](OrgTechnicalContactTypeLinks.md) |  | [optional] 

## Example

```python
from okta.models.org_technical_contact_type import OrgTechnicalContactType

# TODO update the JSON string below
json = "{}"
# create an instance of OrgTechnicalContactType from a JSON string
org_technical_contact_type_instance = OrgTechnicalContactType.from_json(json)
# print the JSON string representation of the object
print(OrgTechnicalContactType.to_json())

# convert the object into a dict
org_technical_contact_type_dict = org_technical_contact_type_instance.to_dict()
# create an instance of OrgTechnicalContactType from a dict
org_technical_contact_type_from_dict = OrgTechnicalContactType.from_dict(org_technical_contact_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


