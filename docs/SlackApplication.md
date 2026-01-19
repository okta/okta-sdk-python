# SlackApplication

Schema for the Slack app (key name: `slack`)  To create a Slack app, use the [Create an Application](/openapi/okta-management/management/tag/Application/#tag/Application/operation/createApplication) request with the following parameters in the request body. > **Note:** The Slack app only supports `BROWSER_PLUGIN` and `SAML_2_0` sign-on modes. 

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
**settings** | [**SlackApplicationSettings**](SlackApplicationSettings.md) |  | 

## Example

```python
from okta.models.slack_application import SlackApplication

# TODO update the JSON string below
json = "{}"
# create an instance of SlackApplication from a JSON string
slack_application_instance = SlackApplication.from_json(json)
# print the JSON string representation of the object
print(SlackApplication.to_json())

# convert the object into a dict
slack_application_dict = slack_application_instance.to_dict()
# create an instance of SlackApplication from a dict
slack_application_from_dict = SlackApplication.from_dict(slack_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


