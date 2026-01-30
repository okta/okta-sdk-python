# RealmProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** | Array of allowed domains. No user in this realm can be created or updated unless they have a username and email from one of these domains.  The following characters aren&#39;t allowed in the domain name: &#x60;!$%^&amp;()&#x3D;*+,:;&lt;&gt;&#39;[]|/?\\&#x60; | [optional] 
**name** | **str** | Name of a realm | 
**realm_type** | **str** | Used to store partner users. This property must be set to &#x60;PARTNER&#x60; to access Okta&#39;s external partner portal. | [optional] 

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


