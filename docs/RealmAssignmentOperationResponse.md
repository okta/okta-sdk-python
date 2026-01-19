# RealmAssignmentOperationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **datetime** | Timestamp of when the operation completed | [optional] 
**created** | **datetime** | Timestamp of when the operation was created | 
**id** | **str** | ID of the asynchronous operation | 
**started** | **datetime** | Timestamp of when the operation started | [optional] 
**status** | **str** | The status of the asynchronous operation | 
**type** | **str** | The operation type | 
**assignment_operation** | [**RealmAssignmentOperationResponseAllOfAssignmentOperation**](RealmAssignmentOperationResponseAllOfAssignmentOperation.md) |  | [optional] 
**num_user_moved** | **float** | Number of users moved | [optional] [readonly] 
**realm_id** | **str** | ID of the realm | [optional] [readonly] 
**realm_name** | **str** | Name of the realm | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.realm_assignment_operation_response import RealmAssignmentOperationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RealmAssignmentOperationResponse from a JSON string
realm_assignment_operation_response_instance = RealmAssignmentOperationResponse.from_json(json)
# print the JSON string representation of the object
print(RealmAssignmentOperationResponse.to_json())

# convert the object into a dict
realm_assignment_operation_response_dict = realm_assignment_operation_response_instance.to_dict()
# create an instance of RealmAssignmentOperationResponse from a dict
realm_assignment_operation_response_from_dict = RealmAssignmentOperationResponse.from_dict(realm_assignment_operation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


