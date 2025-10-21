# Csr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] [readonly] 
**csr** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**kty** | **str** |  | [optional] [readonly] 

## Example

```python
from okta.models.csr import Csr

# TODO update the JSON string below
json = "{}"
# create an instance of Csr from a JSON string
csr_instance = Csr.from_json(json)
# print the JSON string representation of the object
print(Csr.to_json())

# convert the object into a dict
csr_dict = csr_instance.to_dict()
# create an instance of Csr from a dict
csr_from_dict = Csr.from_dict(csr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


