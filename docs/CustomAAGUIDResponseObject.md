# CustomAAGUIDResponseObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aaguid** | **str** | A unique 128-bit identifier that&#39;s assigned to a specific model of security key or authenticator | [optional] 
**attestation_root_certificates** | [**List[AttestationRootCertificatesResponseInner]**](AttestationRootCertificatesResponseInner.md) |  | [optional] 
**authenticator_characteristics** | [**AAGUIDAuthenticatorCharacteristics**](AAGUIDAuthenticatorCharacteristics.md) |  | [optional] 
**name** | **str** | The product name associated with the AAGUID | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.custom_aaguid_response_object import CustomAAGUIDResponseObject

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAAGUIDResponseObject from a JSON string
custom_aaguid_response_object_instance = CustomAAGUIDResponseObject.from_json(json)
# print the JSON string representation of the object
print(CustomAAGUIDResponseObject.to_json())

# convert the object into a dict
custom_aaguid_response_object_dict = custom_aaguid_response_object_instance.to_dict()
# create an instance of CustomAAGUIDResponseObject from a dict
custom_aaguid_response_object_from_dict = CustomAAGUIDResponseObject.from_dict(custom_aaguid_response_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


