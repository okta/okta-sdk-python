# CustomAAGUIDUpdateRequestObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attestation_root_certificates** | [**List[AttestationRootCertificatesRequestInner]**](AttestationRootCertificatesRequestInner.md) | Contains the certificate and information about it | [optional] 
**authenticator_characteristics** | [**AAGUIDAuthenticatorCharacteristics**](AAGUIDAuthenticatorCharacteristics.md) |  | [optional] 
**name** | **str** | The product name associated with this AAGUID. | [optional] 

## Example

```python
from okta.models.custom_aaguid_update_request_object import CustomAAGUIDUpdateRequestObject

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAAGUIDUpdateRequestObject from a JSON string
custom_aaguid_update_request_object_instance = CustomAAGUIDUpdateRequestObject.from_json(json)
# print the JSON string representation of the object
print(CustomAAGUIDUpdateRequestObject.to_json())

# convert the object into a dict
custom_aaguid_update_request_object_dict = custom_aaguid_update_request_object_instance.to_dict()
# create an instance of CustomAAGUIDUpdateRequestObject from a dict
custom_aaguid_update_request_object_from_dict = CustomAAGUIDUpdateRequestObject.from_dict(custom_aaguid_update_request_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


