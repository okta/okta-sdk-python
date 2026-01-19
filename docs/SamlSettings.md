# SamlSettings

Advanced settings for the SAML 2.0 protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**honor_persistent_name_id** | **bool** | Determines if the IdP should persist account linking when the incoming assertion NameID format is &#x60;urn:oasis:names:tc:SAML:2.0:nameid-format:persistent&#x60; | [optional] [default to True]
**name_format** | [**SamlNameIdFormat**](SamlNameIdFormat.md) |  | [optional] [default to SamlNameIdFormat.ENUM_1_DOT_1_COLON_NAMEID_MINUS_FORMAT_COLON_UNSPECIFIED]
**participate_slo** | **bool** | Set to &#x60;true&#x60; to have Okta send a logout request to the upstream IdP when a user signs out of Okta or a downstream app. | [optional] 
**send_application_context** | **bool** | Determines if the IdP should send the application context as &#x60;&lt;OktaAppInstanceId&gt;&#x60; and &#x60;&lt;OktaAppName&gt;&#x60; in the &#x60;&lt;saml2p:Extensions&gt;&#x60; element of the &#x60;&lt;AuthnRequest&gt;&#x60; message | [optional] [default to False]

## Example

```python
from okta.models.saml_settings import SamlSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SamlSettings from a JSON string
saml_settings_instance = SamlSettings.from_json(json)
# print the JSON string representation of the object
print(SamlSettings.to_json())

# convert the object into a dict
saml_settings_dict = saml_settings_instance.to_dict()
# create an instance of SamlSettings from a dict
saml_settings_from_dict = SamlSettings.from_dict(saml_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


