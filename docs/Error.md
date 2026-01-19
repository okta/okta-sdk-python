# Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_causes** | [**List[ErrorCause]**](ErrorCause.md) |  | [optional] 
**error_code** | **str** | An Okta code for this type of error | [optional] 
**error_id** | **str** | A unique identifier for this error. This can be used by Okta Support to help with troubleshooting. | [optional] 
**error_link** | **str** | An Okta code for this type of error | [optional] 
**error_summary** | **str** | A short description of what caused this error. Sometimes this contains dynamically-generated information about your specific error. | [optional] 

## Example

```python
from okta.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


