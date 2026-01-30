# AdminConsoleSettings

Settings specific to the Okta Admin Console

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_idle_timeout_minutes** | **int** | The maximum idle time before the Okta Admin Console session expires. Must be no more than 12 hours. | [optional] [default to 15]
**session_max_lifetime_minutes** | **int** | The absolute maximum session lifetime of the Okta Admin Console. Must be no more than 7 days. | [optional] [default to 720]

## Example

```python
from okta.models.admin_console_settings import AdminConsoleSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AdminConsoleSettings from a JSON string
admin_console_settings_instance = AdminConsoleSettings.from_json(json)
# print the JSON string representation of the object
print(AdminConsoleSettings.to_json())

# convert the object into a dict
admin_console_settings_dict = admin_console_settings_instance.to_dict()
# create an instance of AdminConsoleSettings from a dict
admin_console_settings_from_dict = AdminConsoleSettings.from_dict(admin_console_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


