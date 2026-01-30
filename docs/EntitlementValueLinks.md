# EntitlementValueLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**HrefObjectGroupLink**](HrefObjectGroupLink.md) |  | [optional] 
**app** | [**HrefObjectAppLink**](HrefObjectAppLink.md) |  | [optional] 
**resource_set** | [**HrefObjectResourceSetLink**](HrefObjectResourceSetLink.md) |  | [optional] 

## Example

```python
from okta.models.entitlement_value_links import EntitlementValueLinks

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementValueLinks from a JSON string
entitlement_value_links_instance = EntitlementValueLinks.from_json(json)
# print the JSON string representation of the object
print(EntitlementValueLinks.to_json())

# convert the object into a dict
entitlement_value_links_dict = entitlement_value_links_instance.to_dict()
# create an instance of EntitlementValueLinks from a dict
entitlement_value_links_from_dict = EntitlementValueLinks.from_dict(entitlement_value_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


