# OidcSettings

Advanced settings for the OpenID Connect protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**participate_slo** | **bool** | Set to &#x60;true&#x60; to have Okta send a logout request to the upstream IdP when a user signs out of Okta or a downstream app. | [optional] 
**send_application_context** | **bool** | Determines if the IdP should send the application context as &#x60;OktaAppInstanceId&#x60; and &#x60;OktaAppName&#x60; params in the request | [optional] [default to False]

## Example

```python
from okta.models.oidc_settings import OidcSettings

# TODO update the JSON string below
json = "{}"
# create an instance of OidcSettings from a JSON string
oidc_settings_instance = OidcSettings.from_json(json)
# print the JSON string representation of the object
print(OidcSettings.to_json())

# convert the object into a dict
oidc_settings_dict = oidc_settings_instance.to_dict()
# create an instance of OidcSettings from a dict
oidc_settings_from_dict = OidcSettings.from_dict(oidc_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


