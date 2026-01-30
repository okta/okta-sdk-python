# BundleEntitlementsResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**next** | [**HrefObjectNextLink**](HrefObjectNextLink.md) |  | [optional] 
**bundle** | [**BundleLink**](BundleLink.md) |  | [optional] 

## Example

```python
from okta.models.bundle_entitlements_response_links import BundleEntitlementsResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of BundleEntitlementsResponseLinks from a JSON string
bundle_entitlements_response_links_instance = BundleEntitlementsResponseLinks.from_json(json)
# print the JSON string representation of the object
print(BundleEntitlementsResponseLinks.to_json())

# convert the object into a dict
bundle_entitlements_response_links_dict = bundle_entitlements_response_links_instance.to_dict()
# create an instance of BundleEntitlementsResponseLinks from a dict
bundle_entitlements_response_links_from_dict = BundleEntitlementsResponseLinks.from_dict(bundle_entitlements_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


