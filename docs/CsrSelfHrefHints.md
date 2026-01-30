# CsrSelfHrefHints

Describes allowed HTTP verbs for the `href`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | **List[str]** |  | [optional] 

## Example

```python
from okta.models.csr_self_href_hints import CsrSelfHrefHints

# TODO update the JSON string below
json = "{}"
# create an instance of CsrSelfHrefHints from a JSON string
csr_self_href_hints_instance = CsrSelfHrefHints.from_json(json)
# print the JSON string representation of the object
print(CsrSelfHrefHints.to_json())

# convert the object into a dict
csr_self_href_hints_dict = csr_self_href_hints_instance.to_dict()
# create an instance of CsrSelfHrefHints from a dict
csr_self_href_hints_from_dict = CsrSelfHrefHints.from_dict(csr_self_href_hints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


