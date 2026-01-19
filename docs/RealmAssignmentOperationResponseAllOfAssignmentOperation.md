# RealmAssignmentOperationResponseAllOfAssignmentOperation

Definition of the realm assignment operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**RealmAssignmentOperationResponseAllOfAssignmentOperationConfiguration**](RealmAssignmentOperationResponseAllOfAssignmentOperationConfiguration.md) |  | [optional] 

## Example

```python
from okta.models.realm_assignment_operation_response_all_of_assignment_operation import RealmAssignmentOperationResponseAllOfAssignmentOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RealmAssignmentOperationResponseAllOfAssignmentOperation from a JSON string
realm_assignment_operation_response_all_of_assignment_operation_instance = RealmAssignmentOperationResponseAllOfAssignmentOperation.from_json(json)
# print the JSON string representation of the object
print(RealmAssignmentOperationResponseAllOfAssignmentOperation.to_json())

# convert the object into a dict
realm_assignment_operation_response_all_of_assignment_operation_dict = realm_assignment_operation_response_all_of_assignment_operation_instance.to_dict()
# create an instance of RealmAssignmentOperationResponseAllOfAssignmentOperation from a dict
realm_assignment_operation_response_all_of_assignment_operation_from_dict = RealmAssignmentOperationResponseAllOfAssignmentOperation.from_dict(realm_assignment_operation_response_all_of_assignment_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


