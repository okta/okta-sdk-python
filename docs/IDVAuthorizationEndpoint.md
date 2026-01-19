# IDVAuthorizationEndpoint

IDV authorization endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding** | **str** |  | [optional] 
**url** | **str** | URL of the &#x60;authorization&#x60; endpoint of the IDV vendor | [optional] 

## Example

```python
from okta.models.idv_authorization_endpoint import IDVAuthorizationEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of IDVAuthorizationEndpoint from a JSON string
idv_authorization_endpoint_instance = IDVAuthorizationEndpoint.from_json(json)
# print the JSON string representation of the object
print(IDVAuthorizationEndpoint.to_json())

# convert the object into a dict
idv_authorization_endpoint_dict = idv_authorization_endpoint_instance.to_dict()
# create an instance of IDVAuthorizationEndpoint from a dict
idv_authorization_endpoint_from_dict = IDVAuthorizationEndpoint.from_dict(idv_authorization_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


