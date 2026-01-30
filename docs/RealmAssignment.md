# RealmAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**Actions**](Actions.md) |  | [optional] 
**conditions** | [**Conditions**](Conditions.md) |  | [optional] 
**created** | **datetime** | Timestamp when the realm assignment was created | [optional] [readonly] 
**domains** | **List[str]** | Array of allowed domains. No user in this realm can be created or updated unless they have a username and email from one of these domains.  The following characters aren&#39;t allowed in the domain name: &#x60;!$%^&amp;()&#x3D;*+,:;&lt;&gt;&#39;[]|/?\\&#x60; | [optional] 
**id** | **str** | Unique ID of the realm assignment | [optional] [readonly] 
**is_default** | **bool** | Indicates the default realm. Existing users will start out in the default realm and can be moved individually to other realms. | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp of when the realm assignment was updated | [optional] [readonly] 
**name** | **str** | Name of the realm | [optional] 
**priority** | **int** | The priority of the realm assignment. The lower the number, the higher the priority. This helps resolve conflicts between realm assignments. &gt; **Note:** When you create realm assignments in bulk, realm assignment priorities must be unique. | [optional] 
**status** | [**LifecycleStatus**](LifecycleStatus.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.realm_assignment import RealmAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of RealmAssignment from a JSON string
realm_assignment_instance = RealmAssignment.from_json(json)
# print the JSON string representation of the object
print(RealmAssignment.to_json())

# convert the object into a dict
realm_assignment_dict = realm_assignment_instance.to_dict()
# create an instance of RealmAssignment from a dict
realm_assignment_from_dict = RealmAssignment.from_dict(realm_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


