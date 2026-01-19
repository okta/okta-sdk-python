# EntitlementValuesResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**bundle** | [**BundleLink**](BundleLink.md) |  | [optional] 
**entitlements** | [**EntitlementsLink**](EntitlementsLink.md) |  | [optional] 
**next** | [**HrefObjectNextLink**](HrefObjectNextLink.md) |  | [optional] 

## Example

```python
from okta.models.entitlement_values_response_links import EntitlementValuesResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementValuesResponseLinks from a JSON string
entitlement_values_response_links_instance = EntitlementValuesResponseLinks.from_json(json)
# print the JSON string representation of the object
print(EntitlementValuesResponseLinks.to_json())

# convert the object into a dict
entitlement_values_response_links_dict = entitlement_values_response_links_instance.to_dict()
# create an instance of EntitlementValuesResponseLinks from a dict
entitlement_values_response_links_from_dict = EntitlementValuesResponseLinks.from_dict(entitlement_values_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


