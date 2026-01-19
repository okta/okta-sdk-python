# AAGUIDAuthenticatorCharacteristics

Contains additional properties about custom AAGUID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fips_compliant** | **bool** | Indicates whether the authenticator meets Federal Information Processing Standards (FIPS) compliance requirements | [optional] 
**hardware_protected** | **bool** | Indicates whether the authenticator stores the private key on a hardware component | [optional] 
**platform_attached** | **bool** | Indicates whether the custom AAGUID is built into the authenticator (&#x60;true&#x60;) or if it&#39;s a separate, external authenticator | [optional] 

## Example

```python
from okta.models.aaguid_authenticator_characteristics import AAGUIDAuthenticatorCharacteristics

# TODO update the JSON string below
json = "{}"
# create an instance of AAGUIDAuthenticatorCharacteristics from a JSON string
aaguid_authenticator_characteristics_instance = AAGUIDAuthenticatorCharacteristics.from_json(json)
# print the JSON string representation of the object
print(AAGUIDAuthenticatorCharacteristics.to_json())

# convert the object into a dict
aaguid_authenticator_characteristics_dict = aaguid_authenticator_characteristics_instance.to_dict()
# create an instance of AAGUIDAuthenticatorCharacteristics from a dict
aaguid_authenticator_characteristics_from_dict = AAGUIDAuthenticatorCharacteristics.from_dict(aaguid_authenticator_characteristics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


