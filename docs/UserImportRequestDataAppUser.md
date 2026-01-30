# UserImportRequestDataAppUser

The app user profile being imported

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | **Dict[str, str]** | Provides the name-value pairs of the attributes contained in the app user profile of the user who is being imported. You can change the values of attributes in the user&#39;s app profile by means of the &#x60;commands&#x60; object you return. If you change attributes in the app profile, they then flow through to the Okta user profile, based on matching and mapping rules. | [optional] 

## Example

```python
from okta.models.user_import_request_data_app_user import UserImportRequestDataAppUser

# TODO update the JSON string below
json = "{}"
# create an instance of UserImportRequestDataAppUser from a JSON string
user_import_request_data_app_user_instance = UserImportRequestDataAppUser.from_json(json)
# print the JSON string representation of the object
print(UserImportRequestDataAppUser.to_json())

# convert the object into a dict
user_import_request_data_app_user_dict = user_import_request_data_app_user_instance.to_dict()
# create an instance of UserImportRequestDataAppUser from a dict
user_import_request_data_app_user_from_dict = UserImportRequestDataAppUser.from_dict(user_import_request_data_app_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


