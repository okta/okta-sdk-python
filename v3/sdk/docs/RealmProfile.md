# RealmProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of a Realm | [optional] 

## Example

```python
from okta.models.realm_profile import RealmProfile

# TODO update the JSON string below
json = "{}"
# create an instance of RealmProfile from a JSON string
realm_profile_instance = RealmProfile.from_json(json)
# print the JSON string representation of the object
print(RealmProfile.to_json())

# convert the object into a dict
realm_profile_dict = realm_profile_instance.to_dict()
# create an instance of RealmProfile from a dict
realm_profile_from_dict = RealmProfile.from_dict(realm_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


