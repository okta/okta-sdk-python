# AppInstanceProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from okta.models.app_instance_property import AppInstanceProperty

# TODO update the JSON string below
json = "{}"
# create an instance of AppInstanceProperty from a JSON string
app_instance_property_instance = AppInstanceProperty.from_json(json)
# print the JSON string representation of the object
print(AppInstanceProperty.to_json())

# convert the object into a dict
app_instance_property_dict = app_instance_property_instance.to_dict()
# create an instance of AppInstanceProperty from a dict
app_instance_property_from_dict = AppInstanceProperty.from_dict(app_instance_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


