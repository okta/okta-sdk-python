# SamlRelayState

Relay state settings for IdP

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | [**SamlRelayStateFormat**](SamlRelayStateFormat.md) |  | [optional] 

## Example

```python
from okta.models.saml_relay_state import SamlRelayState

# TODO update the JSON string below
json = "{}"
# create an instance of SamlRelayState from a JSON string
saml_relay_state_instance = SamlRelayState.from_json(json)
# print the JSON string representation of the object
print(SamlRelayState.to_json())

# convert the object into a dict
saml_relay_state_dict = saml_relay_state_instance.to_dict()
# create an instance of SamlRelayState from a dict
saml_relay_state_from_dict = SamlRelayState.from_dict(saml_relay_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


