# AppGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | The external ID of the app group whose members might be privileged app users | 
**name** | **str** | The name of the app group whose members might be privileged app users | 

## Example

```python
from okta.models.app_group import AppGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AppGroup from a JSON string
app_group_instance = AppGroup.from_json(json)
# print the JSON string representation of the object
print(AppGroup.to_json())

# convert the object into a dict
app_group_dict = app_group_instance.to_dict()
# create an instance of AppGroup from a dict
app_group_from_dict = AppGroup.from_dict(app_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


