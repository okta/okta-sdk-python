# AcsEndpoint

An array of ACS endpoints. You can configure a maximum of 100 endpoints.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Index of the URL in the array of ACS endpoints | 
**url** | **str** | URL of the ACS | 

## Example

```python
from openapi_client.models.acs_endpoint import AcsEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of AcsEndpoint from a JSON string
acs_endpoint_instance = AcsEndpoint.from_json(json)
# print the JSON string representation of the object
print(AcsEndpoint.to_json())

# convert the object into a dict
acs_endpoint_dict = acs_endpoint_instance.to_dict()
# create an instance of AcsEndpoint from a dict
acs_endpoint_from_dict = AcsEndpoint.from_dict(acs_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


