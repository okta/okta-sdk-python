# PolicyLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**activate** | [**HrefObjectActivateLink**](HrefObjectActivateLink.md) |  | [optional] 
**deactivate** | [**HrefObjectDeactivateLink**](HrefObjectDeactivateLink.md) |  | [optional] 
**rules** | [**HrefObjectRulesLink**](HrefObjectRulesLink.md) |  | [optional] 
**mappings** | [**HrefObjectMappingsLink**](HrefObjectMappingsLink.md) |  | [optional] 

## Example

```python
from openapi_client.models.policy_links import PolicyLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyLinks from a JSON string
policy_links_instance = PolicyLinks.from_json(json)
# print the JSON string representation of the object
print(PolicyLinks.to_json())

# convert the object into a dict
policy_links_dict = policy_links_instance.to_dict()
# create an instance of PolicyLinks from a dict
policy_links_from_dict = PolicyLinks.from_dict(policy_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


