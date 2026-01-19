# RealmAssignmentOperationResponseAllOfAssignmentOperationConfiguration

Configuration defintion of the realm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**RealmAssignmentOperationResponseAllOfAssignmentOperationConfigurationActions**](RealmAssignmentOperationResponseAllOfAssignmentOperationConfigurationActions.md) |  | [optional] 
**conditions** | [**Conditions**](Conditions.md) |  | [optional] 
**id** | **str** | ID of the realm assignment operation | [optional] 
**name** | **str** | Name of the realm assignment operation | [optional] 

## Example

```python
from okta.models.realm_assignment_operation_response_all_of_assignment_operation_configuration import RealmAssignmentOperationResponseAllOfAssignmentOperationConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RealmAssignmentOperationResponseAllOfAssignmentOperationConfiguration from a JSON string
realm_assignment_operation_response_all_of_assignment_operation_configuration_instance = RealmAssignmentOperationResponseAllOfAssignmentOperationConfiguration.from_json(json)
# print the JSON string representation of the object
print(RealmAssignmentOperationResponseAllOfAssignmentOperationConfiguration.to_json())

# convert the object into a dict
realm_assignment_operation_response_all_of_assignment_operation_configuration_dict = realm_assignment_operation_response_all_of_assignment_operation_configuration_instance.to_dict()
# create an instance of RealmAssignmentOperationResponseAllOfAssignmentOperationConfiguration from a dict
realm_assignment_operation_response_all_of_assignment_operation_configuration_from_dict = RealmAssignmentOperationResponseAllOfAssignmentOperationConfiguration.from_dict(realm_assignment_operation_response_all_of_assignment_operation_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


