# HrefHints

Describes allowed HTTP verbs for the `href`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | [**List[HttpMethod]**](HttpMethod.md) |  | [optional] 

## Example

```python
from okta.models.href_hints import HrefHints

# TODO update the JSON string below
json = "{}"
# create an instance of HrefHints from a JSON string
href_hints_instance = HrefHints.from_json(json)
# print the JSON string representation of the object
print(HrefHints.to_json())

# convert the object into a dict
href_hints_dict = href_hints_instance.to_dict()
# create an instance of HrefHints from a dict
href_hints_from_dict = HrefHints.from_dict(href_hints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


