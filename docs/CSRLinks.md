# CSRLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the current status of a CSR object using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification. This object is used for dynamic discovery of related resources and lifecycle operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish** | [**HrefCsrPublishLink**](HrefCsrPublishLink.md) |  | [optional] 
**var_self** | [**HrefCsrSelfLink**](HrefCsrSelfLink.md) |  | [optional] 

## Example

```python
from okta.models.csr_links import CSRLinks

# TODO update the JSON string below
json = "{}"
# create an instance of CSRLinks from a JSON string
csr_links_instance = CSRLinks.from_json(json)
# print the JSON string representation of the object
print(CSRLinks.to_json())

# convert the object into a dict
csr_links_dict = csr_links_instance.to_dict()
# create an instance of CSRLinks from a dict
csr_links_from_dict = CSRLinks.from_dict(csr_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


