# DefaultApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_instance_id** | **str** |  | [optional] 
**app_link_name** | **str** |  | [optional] 
**classic_application_uri** | **str** |  | [optional] 

## Example

```python
from okta.models.default_app import DefaultApp

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultApp from a JSON string
default_app_instance = DefaultApp.from_json(json)
# print the JSON string representation of the object
print(DefaultApp.to_json())

# convert the object into a dict
default_app_dict = default_app_instance.to_dict()
# create an instance of DefaultApp from a dict
default_app_from_dict = DefaultApp.from_dict(default_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


