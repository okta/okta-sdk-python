# Realm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the Realm was created | [optional] [readonly] 
**id** | **str** | Unique key for the Realm | [optional] [readonly] 
**is_default** | **bool** | Conveys whether the Realm is the default | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the Realm was last updated | [optional] [readonly] 
**profile** | [**RealmProfile**](RealmProfile.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.realm import Realm

# TODO update the JSON string below
json = "{}"
# create an instance of Realm from a JSON string
realm_instance = Realm.from_json(json)
# print the JSON string representation of the object
print(Realm.to_json())

# convert the object into a dict
realm_dict = realm_instance.to_dict()
# create an instance of Realm from a dict
realm_form_dict = realm.from_dict(realm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


