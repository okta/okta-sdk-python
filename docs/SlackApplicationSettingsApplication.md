# SlackApplicationSettingsApplication

Slack app instance properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The Slack app domain name | 
**user_email_value** | **str** | The &#x60;User.Email&#x60; attribute value | [optional] 

## Example

```python
from okta.models.slack_application_settings_application import SlackApplicationSettingsApplication

# TODO update the JSON string below
json = "{}"
# create an instance of SlackApplicationSettingsApplication from a JSON string
slack_application_settings_application_instance = SlackApplicationSettingsApplication.from_json(json)
# print the JSON string representation of the object
print(SlackApplicationSettingsApplication.to_json())

# convert the object into a dict
slack_application_settings_application_dict = slack_application_settings_application_instance.to_dict()
# create an instance of SlackApplicationSettingsApplication from a dict
slack_application_settings_application_from_dict = SlackApplicationSettingsApplication.from_dict(slack_application_settings_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


