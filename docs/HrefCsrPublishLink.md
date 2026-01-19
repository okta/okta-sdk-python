# HrefCsrPublishLink

Link to publish CSR

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**CsrPublishHrefHints**](CsrPublishHrefHints.md) |  | [optional] 
**href** | **str** | Link URI | 

## Example

```python
from okta.models.href_csr_publish_link import HrefCsrPublishLink

# TODO update the JSON string below
json = "{}"
# create an instance of HrefCsrPublishLink from a JSON string
href_csr_publish_link_instance = HrefCsrPublishLink.from_json(json)
# print the JSON string representation of the object
print(HrefCsrPublishLink.to_json())

# convert the object into a dict
href_csr_publish_link_dict = href_csr_publish_link_instance.to_dict()
# create an instance of HrefCsrPublishLink from a dict
href_csr_publish_link_from_dict = HrefCsrPublishLink.from_dict(href_csr_publish_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


