# IdPCsrLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**publish** | [**HrefObject**](HrefObject.md) | Publish the CSR | [optional] 

## Example

```python
from okta.models.id_p_csr_links import IdPCsrLinks

# TODO update the JSON string below
json = "{}"
# create an instance of IdPCsrLinks from a JSON string
id_p_csr_links_instance = IdPCsrLinks.from_json(json)
# print the JSON string representation of the object
print(IdPCsrLinks.to_json())

# convert the object into a dict
id_p_csr_links_dict = id_p_csr_links_instance.to_dict()
# create an instance of IdPCsrLinks from a dict
id_p_csr_links_from_dict = IdPCsrLinks.from_dict(id_p_csr_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


