# ApplicationEmbedded

Embedded resources related to the app using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification. If the `expand=user/{userId}` query parameter is specified, then the assigned [Application User](/openapi/okta-management/management/tag/ApplicationUsers/) is embedded.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **Dict[str, object]** | The specified [Application User](/openapi/okta-management/management/tag/ApplicationUsers/) assigned to the app | [optional] 

## Example

```python
from okta.models.application_embedded import ApplicationEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationEmbedded from a JSON string
application_embedded_instance = ApplicationEmbedded.from_json(json)
# print the JSON string representation of the object
print(ApplicationEmbedded.to_json())

# convert the object into a dict
application_embedded_dict = application_embedded_instance.to_dict()
# create an instance of ApplicationEmbedded from a dict
application_embedded_from_dict = ApplicationEmbedded.from_dict(application_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


