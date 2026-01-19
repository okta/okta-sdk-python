# Org2OrgApplication

Schema for the Okta Org2Org app (key name: `okta_org2org`)  To create an Org2Org app, use the [Create an Application](/openapi/okta-management/management/tag/Application/#tag/Application/operation/createApplication) request with the following parameters in the request body. > **Notes:** > * The Okta Org2Org (`okta_org2org`) app isn't available in Okta Integrator Free Plan orgs. If you need to test this feature in your Integrator Free Plan org, contact your Okta account team. > * The Okta Org2Org app supports `SAML_2_0` and `AUTO_LOGIN` sign-on modes. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | [**ApplicationAccessibility**](ApplicationAccessibility.md) |  | [optional] 
**credentials** | [**SchemeApplicationCredentials**](SchemeApplicationCredentials.md) |  | [optional] 
**label** | **str** | User-defined display name for app | 
**licensing** | [**ApplicationLicensing**](ApplicationLicensing.md) |  | [optional] 
**name** | **str** |  | 
**profile** | **Dict[str, object]** | Contains any valid JSON schema for specifying properties that can be referenced from a request (only available to OAuth 2.0 client apps) | [optional] 
**sign_on_mode** | **str** |  | [optional] [default to 'SAML_2_0']
**status** | [**ApplicationLifecycleStatus**](ApplicationLifecycleStatus.md) |  | [optional] 
**visibility** | [**ApplicationVisibility**](ApplicationVisibility.md) |  | [optional] 
**settings** | [**Org2OrgApplicationSettings**](Org2OrgApplicationSettings.md) |  | 

## Example

```python
from okta.models.org2_org_application import Org2OrgApplication

# TODO update the JSON string below
json = "{}"
# create an instance of Org2OrgApplication from a JSON string
org2_org_application_instance = Org2OrgApplication.from_json(json)
# print the JSON string representation of the object
print(Org2OrgApplication.to_json())

# convert the object into a dict
org2_org_application_dict = org2_org_application_instance.to_dict()
# create an instance of Org2OrgApplication from a dict
org2_org_application_from_dict = Org2OrgApplication.from_dict(org2_org_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


