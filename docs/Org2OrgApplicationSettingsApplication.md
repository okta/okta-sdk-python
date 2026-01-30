# Org2OrgApplicationSettingsApplication

Org2Org app instance properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acs_url** | **str** | The Assertion Consumer Service (ACS) URL of the source org (for &#x60;SAML_2_0&#x60; sign-on mode) | [optional] 
**aud_restriction** | **str** | The entity ID of the SP (for &#x60;SAML_2_0&#x60; sign-on mode) | [optional] 
**base_url** | **str** | The base URL of the target Okta org (for &#x60;SAML_2_0&#x60; sign-on mode) | 
**creation_state** | **str** | Used to track and manage the state of the app&#39;s creation or the provisioning process between two Okta orgs | [optional] 
**prefer_username_over_email** | **bool** | Indicates that you don&#39;t want to use an email address as the username | [optional] 
**token** | **str** | An API token from the target org that&#39;s used to secure the connection between the orgs | [optional] 
**token_encrypted** | **str** | Encrypted token to enhance security | [optional] 

## Example

```python
from okta.models.org2_org_application_settings_application import Org2OrgApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of Org2OrgApplicationSettingsApplication from a JSON string
org2_org_application_settings_application_instance = Org2OrgApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(Org2OrgApplicationSettingsApplication.to_json())

# convert the object into a dict
org2_org_application_settings_application_dict = org2_org_application_settings_application_instance.to_dict()
# create an instance of Org2OrgApplicationSettingsApplication from a dict
org2_org_application_settings_application_from_dict = Org2OrgApplicationSettingsApplication.from_dict(org2_org_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


