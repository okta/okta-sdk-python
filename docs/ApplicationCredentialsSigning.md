# ApplicationCredentialsSigning

App signing key properties > **Note:** Only apps with SAML_2_0, SAML_1_1, WS_FEDERATION, or OPENID_CONNECT `signOnMode` support the key rotation feature. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kid** | **str** | Key identifier used for signing assertions &gt; **Note:** Currently, only the X.509 JWK format is supported for apps with SAML_2_0 &#x60;signOnMode&#x60;. | [optional] 
**last_rotated** | **datetime** | Timestamp when the signing key was last rotated | [optional] [readonly] 
**next_rotation** | **datetime** | The scheduled time for the next signing key rotation | [optional] [readonly] 
**rotation_mode** | **str** | The mode of key rotation | [optional] 
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


