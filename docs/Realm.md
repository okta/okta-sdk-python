# Realm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the realm was created | [optional] [readonly] 
**id** | **str** | Unique ID for the realm | [optional] [readonly] 
**is_default** | **bool** | Indicates the default realm. Existing users will start out in the default realm and can be moved to other realms individually or through realm assignments. See [Realms Assignments API](/openapi/okta-management/management/tag/RealmAssignment/). | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the realm was updated | [optional] [readonly] 
**profile** | [**RealmProfile**](RealmProfile.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.realm import Realm

# TODO update the JSON string below
json = "{}"
# create an instance of Realm from a JSON string
realm_instance = Realm.from_json(json)
# print the JSON string representation of the object
print(Realm.to_json())

# convert the object into a dict
realm_dict = realm_instance.to_dict()
# create an instance of Realm from a dict
realm_from_dict = Realm.from_dict(realm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


