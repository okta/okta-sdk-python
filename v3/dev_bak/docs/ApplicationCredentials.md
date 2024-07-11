# ApplicationCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing** | [**ApplicationCredentialsSigning**](ApplicationCredentialsSigning.md) |  | [optional] 
**user_name_template** | [**ApplicationCredentialsUsernameTemplate**](ApplicationCredentialsUsernameTemplate.md) |  | [optional] 

## Example

```python
from openapi_client.models.application_credentials import ApplicationCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCredentials from a JSON string
application_credentials_instance = ApplicationCredentials.from_json(json)
# print the JSON string representation of the object
print(ApplicationCredentials.to_json())

# convert the object into a dict
application_credentials_dict = application_credentials_instance.to_dict()
# create an instance of ApplicationCredentials from a dict
application_credentials_from_dict = ApplicationCredentials.from_dict(application_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


