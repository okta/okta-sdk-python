# RealmAssignmentOperationResponseAllOfAssignmentOperationConfigurationActions

Realm assignment action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assign_user_to_realm** | [**RealmAssignmentOperationResponseAllOfAssignmentOperationConfigurationActionsAssignUserToRealm**](RealmAssignmentOperationResponseAllOfAssignmentOperationConfigurationActionsAssignUserToRealm.md) |  | [optional] 

## Example

```python
from okta.models.realm_assignment_operation_response_all_of_assignment_operation_configuration_actions import RealmAssignmentOperationResponseAllOfAssignmentOperationConfigurationActions

# TODO update the JSON string below
json = "{}"
# create an instance of RealmAssignmentOperationResponseAllOfAssignmentOperationConfigurationActions from a JSON string
realm_assignment_operation_response_all_of_assignment_operation_configuration_actions_instance = RealmAssignmentOperationResponseAllOfAssignmentOperationConfigurationActions.from_json(json)
# print the JSON string representation of the object
print(RealmAssignmentOperationResponseAllOfAssignmentOperationConfigurationActions.to_json())

# convert the object into a dict
realm_assignment_operation_response_all_of_assignment_operation_configuration_actions_dict = realm_assignment_operation_response_all_of_assignment_operation_configuration_actions_instance.to_dict()
# create an instance of RealmAssignmentOperationResponseAllOfAssignmentOperationConfigurationActions from a dict
realm_assignment_operation_response_all_of_assignment_operation_configuration_actions_from_dict = RealmAssignmentOperationResponseAllOfAssignmentOperationConfigurationActions.from_dict(realm_assignment_operation_response_all_of_assignment_operation_configuration_actions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


