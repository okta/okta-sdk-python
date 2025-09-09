# Success


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_message** | [**List[SuccessSuccessMessageInner]**](SuccessSuccessMessageInner.md) |  | [optional] 
**success_code** | **str** | An Okta code for this type of success | [optional] 
**success_summary** | **str** | A short description of success message. Sometimes this contains dynamically-generated information about your specific response. | [optional] 

## Example

```python
from okta.models.success import Success

# TODO update the JSON string below
json = "{}"
# create an instance of Success from a JSON string
success_instance = Success.from_json(json)
# print the JSON string representation of the object
print(Success.to_json())

# convert the object into a dict
success_dict = success_instance.to_dict()
# create an instance of Success from a dict
success_from_dict = Success.from_dict(success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


