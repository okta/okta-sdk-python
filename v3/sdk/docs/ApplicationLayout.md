# ApplicationLayout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elements** | **List[Dict[str, object]]** |  | [optional] 
**label** | **str** |  | [optional] 
**options** | **Dict[str, object]** |  | [optional] 
**rule** | [**ApplicationLayoutRule**](ApplicationLayoutRule.md) |  | [optional] 
**scope** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from okta.models.application_layout import ApplicationLayout

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationLayout from a JSON string
application_layout_instance = ApplicationLayout.from_json(json)
# print the JSON string representation of the object
print(ApplicationLayout.to_json())

# convert the object into a dict
application_layout_dict = application_layout_instance.to_dict()
# create an instance of ApplicationLayout from a dict
application_layout_from_dict = ApplicationLayout.from_dict(application_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


