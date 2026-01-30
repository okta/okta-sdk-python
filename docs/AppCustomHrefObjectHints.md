# AppCustomHrefObjectHints

Describes allowed HTTP verbs for the `href`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | **List[str]** |  | [optional] 

## Example

```python
from okta.models.app_custom_href_object_hints import AppCustomHrefObjectHints

# TODO update the JSON string below
json = "{}"
# create an instance of AppCustomHrefObjectHints from a JSON string
app_custom_href_object_hints_instance = AppCustomHrefObjectHints.from_json(json)
# print the JSON string representation of the object
print(AppCustomHrefObjectHints.to_json())

# convert the object into a dict
app_custom_href_object_hints_dict = app_custom_href_object_hints_instance.to_dict()
# create an instance of AppCustomHrefObjectHints from a dict
app_custom_href_object_hints_from_dict = AppCustomHrefObjectHints.from_dict(app_custom_href_object_hints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


