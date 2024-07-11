# PolicyMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**links** | [**PolicyMappingLinks**](PolicyMappingLinks.md) |  | [optional] 

## Example

```python
from openapi_client.models.policy_mapping import PolicyMapping

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyMapping from a JSON string
policy_mapping_instance = PolicyMapping.from_json(json)
# print the JSON string representation of the object
print(PolicyMapping.to_json())

# convert the object into a dict
policy_mapping_dict = policy_mapping_instance.to_dict()
# create an instance of PolicyMapping from a dict
policy_mapping_from_dict = PolicyMapping.from_dict(policy_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


