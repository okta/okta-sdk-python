# WebAuthnRpId

The [RP ID](https://www.w3.org/TR/webauthn/#relying-party-identifier) object for WebAuthn configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | [**WebAuthnRpIdDomain**](WebAuthnRpIdDomain.md) |  | [optional] 
**enabled** | **bool** | Indicates whether the RP ID is active and is used for WebAuthn operations. It can only be set to &#x60;true&#x60; once the &#x60;validationStatus&#x60; of the &#x60;domain&#x60; object is &#x60;VERIFIED&#x60;. &#x60;enabled&#x60; can only be &#x60;true&#x60; for this same &#x60;domain&#x60;. Its value must be &#x60;false&#x60; to be able to configure the &#x60;domain&#x60;. | [optional] [default to False]

## Example

```python
from okta.models.web_authn_rp_id import WebAuthnRpId

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthnRpId from a JSON string
web_authn_rp_id_instance = WebAuthnRpId.from_json(json)
# print the JSON string representation of the object
print(WebAuthnRpId.to_json())

# convert the object into a dict
web_authn_rp_id_dict = web_authn_rp_id_instance.to_dict()
# create an instance of WebAuthnRpId from a dict
web_authn_rp_id_from_dict = WebAuthnRpId.from_dict(web_authn_rp_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


