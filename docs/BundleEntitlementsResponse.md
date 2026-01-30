# BundleEntitlementsResponse

Entitlement list for a governance bundle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlements** | [**List[BundleEntitlement]**](BundleEntitlement.md) | List of bundle entitlements | [optional] 
**links** | [**BundleEntitlementsResponseLinks**](BundleEntitlementsResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.bundle_entitlements_response import BundleEntitlementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BundleEntitlementsResponse from a JSON string
bundle_entitlements_response_instance = BundleEntitlementsResponse.from_json(json)
# print the JSON string representation of the object
print(BundleEntitlementsResponse.to_json())

# convert the object into a dict
bundle_entitlements_response_dict = bundle_entitlements_response_instance.to_dict()
# create an instance of BundleEntitlementsResponse from a dict
bundle_entitlements_response_from_dict = BundleEntitlementsResponse.from_dict(bundle_entitlements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


