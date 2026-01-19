# GoogleApplication

Schema for the Google Workspace app (key name: `google`)  To create a Google Workspace app, use the [Create an Application](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Application/#tag/Application/operation/createApplication) request with the following parameters in the request body. > **Note:** The Google Workspace app only supports `BROWSER_PLUGIN` and `SAML_2_0` sign-on modes. 

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
**settings** | [**GoogleApplicationSettings**](GoogleApplicationSettings.md) |  | 

## Example

```python
from okta.models.google_application import GoogleApplication

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleApplication from a JSON string
google_application_instance = GoogleApplication.from_json(json)
# print the JSON string representation of the object
print(GoogleApplication.to_json())

# convert the object into a dict
google_application_dict = google_application_instance.to_dict()
# create an instance of GoogleApplication from a dict
google_application_from_dict = GoogleApplication.from_dict(google_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


