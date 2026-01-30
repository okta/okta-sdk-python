# OperationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **datetime** | Timestamp of when the operation completed | [optional] 
**created** | **datetime** | Timestamp of when the operation was created | 
**id** | **str** | ID of the asynchronous operation | 
**started** | **datetime** | Timestamp of when the operation started | [optional] 
**status** | **str** | The status of the asynchronous operation | 
**type** | **str** | The operation type | 

## Example

```python
from okta.models.operation_response import OperationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OperationResponse from a JSON string
operation_response_instance = OperationResponse.from_json(json)
# print the JSON string representation of the object
print(OperationResponse.to_json())

# convert the object into a dict
operation_response_dict = operation_response_instance.to_dict()
# create an instance of OperationResponse from a dict
operation_response_from_dict = OperationResponse.from_dict(operation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


