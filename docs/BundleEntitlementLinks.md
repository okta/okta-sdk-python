# BundleEntitlementLinks

Link relations available

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**BundleEntitlementLinksValues**](BundleEntitlementLinksValues.md) |  | [optional] 

## Example

```python
from okta.models.bundle_entitlement_links import BundleEntitlementLinks

# TODO update the JSON string below
json = "{}"
# create an instance of BundleEntitlementLinks from a JSON string
bundle_entitlement_links_instance = BundleEntitlementLinks.from_json(json)
# print the JSON string representation of the object
print(BundleEntitlementLinks.to_json())

# convert the object into a dict
bundle_entitlement_links_dict = bundle_entitlement_links_instance.to_dict()
# create an instance of BundleEntitlementLinks from a dict
bundle_entitlement_links_from_dict = BundleEntitlementLinks.from_dict(bundle_entitlement_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


