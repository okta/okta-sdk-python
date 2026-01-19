# OrgOktaSupportSettingsObjLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the Okta Support Settings object using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extend** | [**OrgOktaSupportSettingsObjLinksExtend**](OrgOktaSupportSettingsObjLinksExtend.md) |  | [optional] 
**revoke** | [**OrgOktaSupportSettingsObjLinksRevoke**](OrgOktaSupportSettingsObjLinksRevoke.md) |  | [optional] 
**grant** | [**OrgOktaSupportSettingsObjLinksGrant**](OrgOktaSupportSettingsObjLinksGrant.md) |  | [optional] 
**case** | [**OrgOktaSupportSettingsObjLinksCase**](OrgOktaSupportSettingsObjLinksCase.md) |  | [optional] 
**cases** | [**OrgOktaSupportSettingsObjLinksCases**](OrgOktaSupportSettingsObjLinksCases.md) |  | [optional] 

## Example

```python
from okta.models.org_okta_support_settings_obj_links import OrgOktaSupportSettingsObjLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OrgOktaSupportSettingsObjLinks from a JSON string
org_okta_support_settings_obj_links_instance = OrgOktaSupportSettingsObjLinks.from_json(json)
# print the JSON string representation of the object
print(OrgOktaSupportSettingsObjLinks.to_json())

# convert the object into a dict
org_okta_support_settings_obj_links_dict = org_okta_support_settings_obj_links_instance.to_dict()
# create an instance of OrgOktaSupportSettingsObjLinks from a dict
org_okta_support_settings_obj_links_from_dict = OrgOktaSupportSettingsObjLinks.from_dict(org_okta_support_settings_obj_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


