# OrgBillingContactTypeLinksBilling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**HrefHints**](HrefHints.md) |  | [optional] 
**href** | **str** | Link URI | 
**name** | **str** | Link name | [optional] [readonly] 
**templated** | **bool** | Indicates whether the link object&#39;s &#x60;href&#x60; property is a URI template. | [optional] [readonly] 
**type** | **str** | The media type of the link. If omitted, it is implicitly &#x60;application/json&#x60;. | [optional] [readonly] 

## Example

```python
from okta.models.org_billing_contact_type_links_billing import OrgBillingContactTypeLinksBilling

# TODO update the JSON string below
json = "{}"
# create an instance of OrgBillingContactTypeLinksBilling from a JSON string
org_billing_contact_type_links_billing_instance = OrgBillingContactTypeLinksBilling.from_json(json)
# print the JSON string representation of the object
print(OrgBillingContactTypeLinksBilling.to_json())

# convert the object into a dict
org_billing_contact_type_links_billing_dict = org_billing_contact_type_links_billing_instance.to_dict()
# create an instance of OrgBillingContactTypeLinksBilling from a dict
org_billing_contact_type_links_billing_from_dict = OrgBillingContactTypeLinksBilling.from_dict(org_billing_contact_type_links_billing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


