# PasswordImportRequestDataContextCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The &#x60;username&#x60; that the user supplied when attempting to sign in to Okta. | [optional] 
**password** | **str** | The &#x60;password&#x60; that the user supplied when attempting to sign in to Okta. | [optional] 

## Example

```python
from okta.models.password_import_request_data_context_credential import PasswordImportRequestDataContextCredential

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordImportRequestDataContextCredential from a JSON string
password_import_request_data_context_credential_instance = PasswordImportRequestDataContextCredential.from_json(json)
# print the JSON string representation of the object
print(PasswordImportRequestDataContextCredential.to_json())

# convert the object into a dict
password_import_request_data_context_credential_dict = password_import_request_data_context_credential_instance.to_dict()
# create an instance of PasswordImportRequestDataContextCredential from a dict
password_import_request_data_context_credential_from_dict = PasswordImportRequestDataContextCredential.from_dict(password_import_request_data_context_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


