# EntitlementValuesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlement_values** | [**List[EntitlementValue]**](EntitlementValue.md) | List of entitlement values for a bundle entitlement | [optional] 
**links** | [**EntitlementValuesResponseLinks**](EntitlementValuesResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.entitlement_values_response import EntitlementValuesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementValuesResponse from a JSON string
entitlement_values_response_instance = EntitlementValuesResponse.from_json(json)
# print the JSON string representation of the object
print(EntitlementValuesResponse.to_json())

# convert the object into a dict
entitlement_values_response_dict = entitlement_values_response_instance.to_dict()
# create an instance of EntitlementValuesResponse from a dict
entitlement_values_response_from_dict = EntitlementValuesResponse.from_dict(entitlement_values_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


