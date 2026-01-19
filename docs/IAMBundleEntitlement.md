# IAMBundleEntitlement

An entitlement in a governance bundle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_sets** | **List[str]** | List of resource set IDs for the custom role | [optional] 
**role** | **str** | The role | [optional] 
**targets** | **List[str]** | List of target resource IDs to scope the entitlement with the role | [optional] 

## Example

```python
from okta.models.iam_bundle_entitlement import IAMBundleEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of IAMBundleEntitlement from a JSON string
iam_bundle_entitlement_instance = IAMBundleEntitlement.from_json(json)
# print the JSON string representation of the object
print(IAMBundleEntitlement.to_json())

# convert the object into a dict
iam_bundle_entitlement_dict = iam_bundle_entitlement_instance.to_dict()
# create an instance of IAMBundleEntitlement from a dict
iam_bundle_entitlement_from_dict = IAMBundleEntitlement.from_dict(iam_bundle_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


