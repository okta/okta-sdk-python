# ApplicationAccessibility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_redirect_url** | **str** |  | [optional] 
**login_redirect_url** | **str** |  | [optional] 
**self_service** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.application_accessibility import ApplicationAccessibility

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationAccessibility from a JSON string
application_accessibility_instance = ApplicationAccessibility.from_json(json)
# print the JSON string representation of the object
print(ApplicationAccessibility.to_json())

# convert the object into a dict
application_accessibility_dict = application_accessibility_instance.to_dict()
# create an instance of ApplicationAccessibility from a dict
application_accessibility_form_dict = application_accessibility.from_dict(application_accessibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


