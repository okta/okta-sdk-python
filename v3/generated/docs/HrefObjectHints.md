# HrefObjectHints

Describes allowed HTTP verbs for the `href`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | [**List[HttpMethod]**](HttpMethod.md) |  | [optional] 

## Example

```python
from openapi_client.models.href_object_hints import HrefObjectHints

# TODO update the JSON string below
json = "{}"
# create an instance of HrefObjectHints from a JSON string
href_object_hints_instance = HrefObjectHints.from_json(json)
# print the JSON string representation of the object
print(HrefObjectHints.to_json())

# convert the object into a dict
href_object_hints_dict = href_object_hints_instance.to_dict()
# create an instance of HrefObjectHints from a dict
href_object_hints_form_dict = href_object_hints.from_dict(href_object_hints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


