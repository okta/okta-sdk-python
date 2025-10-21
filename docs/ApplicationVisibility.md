# ApplicationVisibility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_links** | **Dict[str, bool]** |  | [optional] 
**auto_launch** | **bool** |  | [optional] 
**auto_submit_toolbar** | **bool** |  | [optional] 
**hide** | [**ApplicationVisibilityHide**](ApplicationVisibilityHide.md) |  | [optional] 

## Example

```python
from okta.models.application_visibility import ApplicationVisibility

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationVisibility from a JSON string
application_visibility_instance = ApplicationVisibility.from_json(json)
# print the JSON string representation of the object
print(ApplicationVisibility.to_json())

# convert the object into a dict
application_visibility_dict = application_visibility_instance.to_dict()
# create an instance of ApplicationVisibility from a dict
application_visibility_from_dict = ApplicationVisibility.from_dict(application_visibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


