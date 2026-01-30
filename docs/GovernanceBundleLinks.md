# GovernanceBundleLinks

Link relations available

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlements** | [**EntitlementsLink**](EntitlementsLink.md) |  | [optional] 
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 

## Example

```python
from okta.models.governance_bundle_links import GovernanceBundleLinks

# TODO update the JSON string below
json = "{}"
# create an instance of GovernanceBundleLinks from a JSON string
governance_bundle_links_instance = GovernanceBundleLinks.from_json(json)
# print the JSON string representation of the object
print(GovernanceBundleLinks.to_json())

# convert the object into a dict
governance_bundle_links_dict = governance_bundle_links_instance.to_dict()
# create an instance of GovernanceBundleLinks from a dict
governance_bundle_links_from_dict = GovernanceBundleLinks.from_dict(governance_bundle_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


