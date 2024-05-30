# PasswordCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | [**PasswordCredentialHash**](PasswordCredentialHash.md) |  | [optional] 
**hook** | [**PasswordCredentialHook**](PasswordCredentialHook.md) |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.password_credential import PasswordCredential

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordCredential from a JSON string
password_credential_instance = PasswordCredential.from_json(json)
# print the JSON string representation of the object
print(PasswordCredential.to_json())

# convert the object into a dict
password_credential_dict = password_credential_instance.to_dict()
# create an instance of PasswordCredential from a dict
password_credential_form_dict = password_credential.from_dict(password_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


