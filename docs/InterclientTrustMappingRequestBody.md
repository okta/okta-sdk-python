# InterclientTrustMappingRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | App ID of the allowed app | [optional] 

## Example

```python
from okta.models.interclient_trust_mapping_request_body import InterclientTrustMappingRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of InterclientTrustMappingRequestBody from a JSON string
interclient_trust_mapping_request_body_instance = InterclientTrustMappingRequestBody.from_json(json)
# print the JSON string representation of the object
print(InterclientTrustMappingRequestBody.to_json())

# convert the object into a dict
interclient_trust_mapping_request_body_dict = interclient_trust_mapping_request_body_instance.to_dict()
# create an instance of InterclientTrustMappingRequestBody from a dict
interclient_trust_mapping_request_body_from_dict = InterclientTrustMappingRequestBody.from_dict(interclient_trust_mapping_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


