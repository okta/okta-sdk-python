# PolicyMappingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** |  | [optional] 
**resource_type** | [**PolicyMappingResourceType**](PolicyMappingResourceType.md) |  | [optional] 

## Example

```python
from openapi_client.models.policy_mapping_request import PolicyMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyMappingRequest from a JSON string
policy_mapping_request_instance = PolicyMappingRequest.from_json(json)
# print the JSON string representation of the object
print(PolicyMappingRequest.to_json())

# convert the object into a dict
policy_mapping_request_dict = policy_mapping_request_instance.to_dict()
# create an instance of PolicyMappingRequest from a dict
policy_mapping_request_form_dict = policy_mapping_request.from_dict(policy_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


