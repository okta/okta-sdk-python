# ProtocolSaml

Protocol settings for the [SAML 2.0 Authentication Request Protocol](http://docs.oasis-open.org/security/saml/v2.0/saml-core-2.0-os.pdf)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithms** | [**SamlAlgorithms**](SamlAlgorithms.md) |  | [optional] 
**credentials** | [**SamlCredentials**](SamlCredentials.md) |  | [optional] 
**endpoints** | [**SamlEndpoints**](SamlEndpoints.md) |  | [optional] 
**relay_state** | [**SamlRelayState**](SamlRelayState.md) |  | [optional] 
**settings** | [**SamlSettings**](SamlSettings.md) |  | [optional] 
**type** | **str** | SAML 2.0 protocol | [optional] 

## Example

```python
from okta.models.protocol_saml import ProtocolSaml

# TODO update the JSON string below
json = "{}"
# create an instance of ProtocolSaml from a JSON string
protocol_saml_instance = ProtocolSaml.from_json(json)
# print the JSON string representation of the object
print(ProtocolSaml.to_json())

# convert the object into a dict
protocol_saml_dict = protocol_saml_instance.to_dict()
# create an instance of ProtocolSaml from a dict
protocol_saml_from_dict = ProtocolSaml.from_dict(protocol_saml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


