# PolicyMappingLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**application** | [**PolicyMappingLinksAllOfApplication**](PolicyMappingLinksAllOfApplication.md) |  | [optional] 
**authenticator** | [**PolicyMappingLinksAllOfAuthenticator**](PolicyMappingLinksAllOfAuthenticator.md) |  | [optional] 
**policy** | [**PolicyMappingLinksAllOfPolicy**](PolicyMappingLinksAllOfPolicy.md) |  | [optional] 

## Example

```python
from openapi_client.models.policy_mapping_links import PolicyMappingLinks

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyMappingLinks from a JSON string
policy_mapping_links_instance = PolicyMappingLinks.from_json(json)
# print the JSON string representation of the object
print(PolicyMappingLinks.to_json())

# convert the object into a dict
policy_mapping_links_dict = policy_mapping_links_instance.to_dict()
# create an instance of PolicyMappingLinks from a dict
policy_mapping_links_form_dict = policy_mapping_links.from_dict(policy_mapping_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


