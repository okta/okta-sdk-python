# DevicePostureChecksRemediationSettingsMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_i18n_key** | **str** | Default i18n key for the message. This property is only relevant if type is set to &#x60;BUILTIN&#x60;. If type is set to &#x60;CUSTOM&#x60;, this field is ignored. | [optional] 
**custom_text** | **str** | Custom text for the message | [optional] 

## Example

```python
from okta.models.device_posture_checks_remediation_settings_message import DevicePostureChecksRemediationSettingsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePostureChecksRemediationSettingsMessage from a JSON string
device_posture_checks_remediation_settings_message_instance = DevicePostureChecksRemediationSettingsMessage.from_json(json)
# print the JSON string representation of the object
print(DevicePostureChecksRemediationSettingsMessage.to_json())

# convert the object into a dict
device_posture_checks_remediation_settings_message_dict = device_posture_checks_remediation_settings_message_instance.to_dict()
# create an instance of DevicePostureChecksRemediationSettingsMessage from a dict
device_posture_checks_remediation_settings_message_from_dict = DevicePostureChecksRemediationSettingsMessage.from_dict(device_posture_checks_remediation_settings_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


