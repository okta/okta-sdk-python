# IDVParEndpoint

IDV [PAR](https://datatracker.ietf.org/doc/html/rfc9126) endpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binding** | **str** |  | [optional] 
**url** | **str** | URL of the &#x60;par&#x60; endpoint of the IDV vendor | [optional] 

## Example

```python
from okta.models.idv_par_endpoint import IDVParEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of IDVParEndpoint from a JSON string
idv_par_endpoint_instance = IDVParEndpoint.from_json(json)
# print the JSON string representation of the object
print(IDVParEndpoint.to_json())

# convert the object into a dict
idv_par_endpoint_dict = idv_par_endpoint_instance.to_dict()
# create an instance of IDVParEndpoint from a dict
idv_par_endpoint_from_dict = IDVParEndpoint.from_dict(idv_par_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


