# KeepCurrent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keep_current** | **bool** | Skip deleting the user&#39;s current session when set to &#x60;true&#x60; | [optional] [default to True]

## Example

```python
from okta.models.keep_current import KeepCurrent

# TODO update the JSON string below
json = "{}"
# create an instance of KeepCurrent from a JSON string
keep_current_instance = KeepCurrent.from_json(json)
# print the JSON string representation of the object
print(KeepCurrent.to_json())

# convert the object into a dict
keep_current_dict = keep_current_instance.to_dict()
# create an instance of KeepCurrent from a dict
keep_current_from_dict = KeepCurrent.from_dict(keep_current_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


