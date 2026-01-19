# CsrPublishHrefHints

Describes allowed HTTP verbs for the `href`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | **List[str]** |  | [optional] 

## Example

```python
from okta.models.csr_publish_href_hints import CsrPublishHrefHints

# TODO update the JSON string below
json = "{}"
# create an instance of CsrPublishHrefHints from a JSON string
csr_publish_href_hints_instance = CsrPublishHrefHints.from_json(json)
# print the JSON string representation of the object
print(CsrPublishHrefHints.to_json())

# convert the object into a dict
csr_publish_href_hints_dict = csr_publish_href_hints_instance.to_dict()
# create an instance of CsrPublishHrefHints from a dict
csr_publish_href_hints_from_dict = CsrPublishHrefHints.from_dict(csr_publish_href_hints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


