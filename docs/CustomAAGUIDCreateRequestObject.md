# CustomAAGUIDCreateRequestObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aaguid** | **str** | An Authenticator Attestation Global Unique Identifier (AAGUID) is a 128-bit identifier indicating the model. | [optional] 
**attestation_root_certificates** | [**List[AttestationRootCertificatesRequestInner]**](AttestationRootCertificatesRequestInner.md) | Contains the certificate and information about it | [optional] 
**authenticator_characteristics** | [**AAGUIDAuthenticatorCharacteristics**](AAGUIDAuthenticatorCharacteristics.md) |  | [optional] 

## Example

```python
from okta.models.custom_aaguid_create_request_object import CustomAAGUIDCreateRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAAGUIDCreateRequestObject from a JSON string
custom_aaguid_create_request_object_instance = CustomAAGUIDCreateRequestObject.from_json(json)
# print the JSON string representation of the object
print(CustomAAGUIDCreateRequestObject.to_json())

# convert the object into a dict
custom_aaguid_create_request_object_dict = custom_aaguid_create_request_object_instance.to_dict()
# create an instance of CustomAAGUIDCreateRequestObject from a dict
custom_aaguid_create_request_object_from_dict = CustomAAGUIDCreateRequestObject.from_dict(custom_aaguid_create_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


