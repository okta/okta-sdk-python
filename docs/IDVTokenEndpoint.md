# IDVTokenEndpoint

Token endpoint of the IDV vendor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding** | **str** |  | [optional] 
**url** | **str** | URL of the &#x60;token&#x60; endpoint of the IDV vendor | [optional] 

## Example

```python
from okta.models.idv_token_endpoint import IDVTokenEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of IDVTokenEndpoint from a JSON string
idv_token_endpoint_instance = IDVTokenEndpoint.from_json(json)
# print the JSON string representation of the object
print(IDVTokenEndpoint.to_json())

# convert the object into a dict
idv_token_endpoint_dict = idv_token_endpoint_instance.to_dict()
# create an instance of IDVTokenEndpoint from a dict
idv_token_endpoint_from_dict = IDVTokenEndpoint.from_dict(idv_token_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


