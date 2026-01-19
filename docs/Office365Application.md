# Office365Application

Schema for the Microsoft Office 365 app (key name: `office365`)  To create a Microsoft Office 365 app, use the [Create an Application](/openapi/okta-management/management/tag/Application/#tag/Application/operation/createApplication) request with the following parameters in the request body. > **Note:** The Office 365 app only supports `BROWSER_PLUGIN` and `SAML_1_1` sign-on modes. 

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
**settings** | [**Office365ApplicationSettings**](Office365ApplicationSettings.md) |  | 

## Example

```python
from okta.models.office365_application import Office365Application

# TODO update the JSON string below
json = "{}"
# create an instance of Office365Application from a JSON string
office365_application_instance = Office365Application.from_json(json)
# print the JSON string representation of the object
print(Office365Application.to_json())

# convert the object into a dict
office365_application_dict = office365_application_instance.to_dict()
# create an instance of Office365Application from a dict
office365_application_from_dict = Office365Application.from_dict(office365_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


