# ApplicationCredentialsSigning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** |  | [optional] 
**last_rotated** | **datetime** |  | [optional] [readonly] 
**next_rotation** | **datetime** |  | [optional] [readonly] 
**rotation_mode** | **str** |  | [optional] 
**use** | [**ApplicationCredentialsSigningUse**](ApplicationCredentialsSigningUse.md) |  | [optional] 

## Example

```python
from okta.models.application_credentials_signing import ApplicationCredentialsSigning

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationCredentialsSigning from a JSON string
application_credentials_signing_instance = ApplicationCredentialsSigning.from_json(json)
# print the JSON string representation of the object
print(ApplicationCredentialsSigning.to_json())

# convert the object into a dict
application_credentials_signing_dict = application_credentials_signing_instance.to_dict()
# create an instance of ApplicationCredentialsSigning from a dict
application_credentials_signing_from_dict = ApplicationCredentialsSigning.from_dict(application_credentials_signing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


