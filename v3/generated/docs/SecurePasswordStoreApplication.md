# SecurePasswordStoreApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**SchemeApplicationCredentials**](SchemeApplicationCredentials.md) |  | [optional] 
**name** | **str** |  | [optional] [default to 'template_sps']
**settings** | [**SecurePasswordStoreApplicationSettings**](SecurePasswordStoreApplicationSettings.md) |  | [optional] 

## Example

```python
from openapi_client.models.secure_password_store_application import SecurePasswordStoreApplication

# TODO update the JSON string below
json = "{}"
# create an instance of SecurePasswordStoreApplication from a JSON string
secure_password_store_application_instance = SecurePasswordStoreApplication.from_json(json)
# print the JSON string representation of the object
print(SecurePasswordStoreApplication.to_json())

# convert the object into a dict
secure_password_store_application_dict = secure_password_store_application_instance.to_dict()
# create an instance of SecurePasswordStoreApplication from a dict
secure_password_store_application_form_dict = secure_password_store_application.from_dict(secure_password_store_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


