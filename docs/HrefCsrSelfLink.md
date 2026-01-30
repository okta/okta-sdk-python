# HrefCsrSelfLink

Link to the resource (self)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**CsrSelfHrefHints**](CsrSelfHrefHints.md) |  | [optional] 
**href** | **str** | Link URI | 

## Example

```python
from okta.models.href_csr_self_link import HrefCsrSelfLink

# TODO update the JSON string below
json = "{}"
# create an instance of HrefCsrSelfLink from a JSON string
href_csr_self_link_instance = HrefCsrSelfLink.from_json(json)
# print the JSON string representation of the object
print(HrefCsrSelfLink.to_json())

# convert the object into a dict
href_csr_self_link_dict = href_csr_self_link_instance.to_dict()
# create an instance of HrefCsrSelfLink from a dict
href_csr_self_link_from_dict = HrefCsrSelfLink.from_dict(href_csr_self_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


