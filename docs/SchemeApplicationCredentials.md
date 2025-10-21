# SchemeApplicationCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing** | [**ApplicationCredentialsSigning**](ApplicationCredentialsSigning.md) |  | [optional] 
**user_name_template** | [**ApplicationCredentialsUsernameTemplate**](ApplicationCredentialsUsernameTemplate.md) |  | [optional] 
**password** | [**PasswordCredential**](PasswordCredential.md) |  | [optional] 
**reveal_password** | **bool** |  | [optional] 
**scheme** | [**ApplicationCredentialsScheme**](ApplicationCredentialsScheme.md) |  | [optional] 
**user_name** | **str** |  | [optional] 

## Example

```python
from okta.models.scheme_application_credentials import SchemeApplicationCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of SchemeApplicationCredentials from a JSON string
scheme_application_credentials_instance = SchemeApplicationCredentials.from_json(json)
# print the JSON string representation of the object
print(SchemeApplicationCredentials.to_json())

# convert the object into a dict
scheme_application_credentials_dict = scheme_application_credentials_instance.to_dict()
# create an instance of SchemeApplicationCredentials from a dict
scheme_application_credentials_from_dict = SchemeApplicationCredentials.from_dict(scheme_application_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


