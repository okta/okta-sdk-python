# CreateRealmAssignmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**Actions**](Actions.md) |  | [optional] 
**conditions** | [**Conditions**](Conditions.md) |  | [optional] 
**name** | **str** | Name of the realm | [optional] 
**priority** | **int** | The priority of the realm assignment. The lower the number, the higher the priority. This helps resolve conflicts between realm assignments. &gt; **Note:** When you create realm assignments in bulk, realm assignment priorities must be unique. | [optional] 

## Example

```python
from okta.models.create_realm_assignment_request import CreateRealmAssignmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRealmAssignmentRequest from a JSON string
create_realm_assignment_request_instance = CreateRealmAssignmentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRealmAssignmentRequest.to_json())

# convert the object into a dict
create_realm_assignment_request_dict = create_realm_assignment_request_instance.to_dict()
# create an instance of CreateRealmAssignmentRequest from a dict
create_realm_assignment_request_from_dict = CreateRealmAssignmentRequest.from_dict(create_realm_assignment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


