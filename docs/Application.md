# Application


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | [**ApplicationAccessibility**](ApplicationAccessibility.md) |  | [optional] 
**created** | **datetime** |  | [optional] [readonly] 
**features** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**label** | **str** |  | [optional] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**licensing** | [**ApplicationLicensing**](ApplicationLicensing.md) |  | [optional] 
**profile** | **Dict[str, object]** |  | [optional] 
**sign_on_mode** | [**ApplicationSignOnMode**](ApplicationSignOnMode.md) |  | [optional] 
**status** | [**ApplicationLifecycleStatus**](ApplicationLifecycleStatus.md) |  | [optional] 
**visibility** | [**ApplicationVisibility**](ApplicationVisibility.md) |  | [optional] 
**embedded** | **Dict[str, object]** |  | [optional] [readonly] 
**links** | [**ApplicationLinks**](ApplicationLinks.md) |  | [optional] 

## Example

```python
from okta.models.application import Application

# TODO update the JSON string below
json = "{}"
# create an instance of Application from a JSON string
application_instance = Application.from_json(json)
# print the JSON string representation of the object
print(Application.to_json())

# convert the object into a dict
application_dict = application_instance.to_dict()
# create an instance of Application from a dict
application_from_dict = Application.from_dict(application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


