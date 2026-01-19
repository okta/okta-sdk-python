# BundleEntitlement

An entitlement in a governance bundle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the role | [optional] 
**id** | **str** | Entitlement ID | [optional] 
**name** | **str** | The name of the role | [optional] 
**role** | **str** | The role key | [optional] 
**links** | [**BundleEntitlementLinks**](BundleEntitlementLinks.md) |  | [optional] 

## Example

```python
from okta.models.bundle_entitlement import BundleEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of BundleEntitlement from a JSON string
bundle_entitlement_instance = BundleEntitlement.from_json(json)
# print the JSON string representation of the object
print(BundleEntitlement.to_json())

# convert the object into a dict
bundle_entitlement_dict = bundle_entitlement_instance.to_dict()
# create an instance of BundleEntitlement from a dict
bundle_entitlement_from_dict = BundleEntitlement.from_dict(bundle_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


