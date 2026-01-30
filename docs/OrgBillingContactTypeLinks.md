# OrgBillingContactTypeLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the org billing contact type object using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing** | [**OrgBillingContactTypeLinksBilling**](OrgBillingContactTypeLinksBilling.md) |  | [optional] 

## Example

```python
from okta.models.org_billing_contact_type_links import OrgBillingContactTypeLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OrgBillingContactTypeLinks from a JSON string
org_billing_contact_type_links_instance = OrgBillingContactTypeLinks.from_json(json)
# print the JSON string representation of the object
print(OrgBillingContactTypeLinks.to_json())

# convert the object into a dict
org_billing_contact_type_links_dict = org_billing_contact_type_links_instance.to_dict()
# create an instance of OrgBillingContactTypeLinks from a dict
org_billing_contact_type_links_from_dict = OrgBillingContactTypeLinks.from_dict(org_billing_contact_type_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


