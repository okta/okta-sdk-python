# WsFederationApplicationSettingsApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_statements** | **str** | You can federate user attributes such as Okta profile fields, LDAP, Active Directory, and Workday values. The SP uses the federated WS-Fed attribute values accordingly. | [optional] 
**audience_restriction** | **str** | The entity ID of the SP. Use the entity ID value exactly as provided by the SP. | 
**authn_context_class_ref** | **str** | Identifies the SAML authentication context class for the assertion&#39;s authentication statement | 
**group_filter** | **str** | A regular expression that filters for the User Groups you want included with the &#x60;groupName&#x60; attribute. If the matching User Group has a corresponding AD group, then the attribute statement includes the value of the attribute specified by &#x60;groupValueFormat&#x60;. If the matching User Group doesn&#39;t contain a corresponding AD group, then the &#x60;groupName&#x60; is used in the attribute statement. | [optional] 
**group_name** | **str** | The group name to include in the WS-Fed response attribute statement. This property is used in conjunction with the &#x60;groupFilter&#x60; property.  Groups that are filtered through the &#x60;groupFilter&#x60; expression are included with the &#x60;groupName&#x60; in the attribute statement. Any users that belong to the group you&#39;ve filtered are included in the WS-Fed response attribute statement. | [optional] 
**group_value_format** | **str** | Specifies the WS-Fed assertion attribute value for filtered groups. This attribute is only applied to Active Directory groups. | 
**name_id_format** | **str** | The username format that you send in the WS-Fed response | 
**realm** | **str** | The uniform resource identifier (URI) of the WS-Fed app that&#39;s used to share resources securely within a domain. It&#39;s the identity that&#39;s sent to the Okta IdP when signing in. See [Realm name](https://help.okta.com/okta_help.htm?type&#x3D;oie&amp;id&#x3D;ext_Apps_Configure_Okta_Template_WS_Federation#Realm). | [optional] 
**site_url** | **str** | Launch URL for the web app | 
**username_attribute** | **str** | Specifies additional username attribute statements to include in the WS-Fed assertion | 
**w_reply_override** | **bool** | Enables a web app to override the &#x60;wReplyURL&#x60; URL with a reply parameter. | [optional] 
**w_reply_url** | **str** | The WS-Fed SP endpoint where your users sign in | 

## Example

```python
from okta.models.ws_federation_application_settings_application import WsFederationApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of WsFederationApplicationSettingsApplication from a JSON string
ws_federation_application_settings_application_instance = WsFederationApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(WsFederationApplicationSettingsApplication.to_json())

# convert the object into a dict
ws_federation_application_settings_application_dict = ws_federation_application_settings_application_instance.to_dict()
# create an instance of WsFederationApplicationSettingsApplication from a dict
ws_federation_application_settings_application_from_dict = WsFederationApplicationSettingsApplication.from_dict(ws_federation_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


