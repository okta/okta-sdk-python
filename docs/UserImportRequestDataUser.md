# UserImportRequestDataUser

Provides information on the Okta user profile currently set to be used for the user who is being imported, based on the matching rules and attribute mappings that were applied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | **Dict[str, str]** | The &#x60;data.user.profile&#x60; contains the name-value pairs of the attributes in the user profile. If the user has been matched to an existing Okta user, a &#x60;data.user.id&#x60; object is included, containing the unique identifier of the Okta user profile.  You can change the values of the attributes by means of the &#x60;commands&#x60; object you return. | [optional] 

## Example

```python
from okta.models.user_import_request_data_user import UserImportRequestDataUser

# TODO update the JSON string below
json = "{}"
# create an instance of UserImportRequestDataUser from a JSON string
user_import_request_data_user_instance = UserImportRequestDataUser.from_json(json)
# print the JSON string representation of the object
print(UserImportRequestDataUser.to_json())

# convert the object into a dict
user_import_request_data_user_dict = user_import_request_data_user_instance.to_dict()
# create an instance of UserImportRequestDataUser from a dict
user_import_request_data_user_from_dict = UserImportRequestDataUser.from_dict(user_import_request_data_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


