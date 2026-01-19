# ZscalerbyzApplication

Schema for the Zscaler 2.0 app (key name: `zscalerbyz`)  To create a Zscaler 2.0 app, use the [Create an Application](/openapi/okta-management/management/tag/Application/#tag/Application/operation/createApplication) request with the following parameters in the request body. > **Note:** The Zscaler 2.0 app only supports `BROWSER_PLUGIN` and `SAML_2_0` sign-on modes. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibility** | [**ApplicationAccessibility**](ApplicationAccessibility.md) |  | [optional] 
**credentials** | [**SchemeApplicationCredentials**](SchemeApplicationCredentials.md) |  | [optional] 
**label** | **str** | User-defined display name for app | 
**licensing** | [**ApplicationLicensing**](ApplicationLicensing.md) |  | [optional] 
**name** | **str** |  | 
**profile** | **Dict[str, object]** | Contains any valid JSON schema for specifying properties that can be referenced from a request (only available to OAuth 2.0 client apps) | [optional] 
**sign_on_mode** | **str** |  | [optional] 
**status** | [**ApplicationLifecycleStatus**](ApplicationLifecycleStatus.md) |  | [optional] 
**visibility** | [**ApplicationVisibility**](ApplicationVisibility.md) |  | [optional] 
**settings** | [**ZscalerbyzApplicationSettings**](ZscalerbyzApplicationSettings.md) |  | 

## Example

```python
from okta.models.zscalerbyz_application import ZscalerbyzApplication

# TODO update the JSON string below
json = "{}"
# create an instance of ZscalerbyzApplication from a JSON string
zscalerbyz_application_instance = ZscalerbyzApplication.from_json(json)
# print the JSON string representation of the object
print(ZscalerbyzApplication.to_json())

# convert the object into a dict
zscalerbyz_application_dict = zscalerbyz_application_instance.to_dict()
# create an instance of ZscalerbyzApplication from a dict
zscalerbyz_application_from_dict = ZscalerbyzApplication.from_dict(zscalerbyz_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


