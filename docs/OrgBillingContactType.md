# OrgBillingContactType

Org billing contact

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_type** | [**OrgContactType**](OrgContactType.md) |  | [optional] 
**links** | [**OrgBillingContactTypeLinks**](OrgBillingContactTypeLinks.md) |  | [optional] 

## Example

```python
from okta.models.org_billing_contact_type import OrgBillingContactType

# TODO update the JSON string below
json = "{}"
# create an instance of OrgBillingContactType from a JSON string
org_billing_contact_type_instance = OrgBillingContactType.from_json(json)
# print the JSON string representation of the object
print(OrgBillingContactType.to_json())

# convert the object into a dict
org_billing_contact_type_dict = org_billing_contact_type_instance.to_dict()
# create an instance of OrgBillingContactType from a dict
org_billing_contact_type_from_dict = OrgBillingContactType.from_dict(org_billing_contact_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


