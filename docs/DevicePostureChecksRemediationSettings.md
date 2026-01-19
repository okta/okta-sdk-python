# DevicePostureChecksRemediationSettings

Represents the remediation instructions shown to the end user when the device posture check fails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link** | [**DevicePostureChecksRemediationSettingsLink**](DevicePostureChecksRemediationSettingsLink.md) |  | [optional] 
**message** | [**DevicePostureChecksRemediationSettingsMessage**](DevicePostureChecksRemediationSettingsMessage.md) |  | [optional] 

## Example

```python
from okta.models.device_posture_checks_remediation_settings import DevicePostureChecksRemediationSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePostureChecksRemediationSettings from a JSON string
device_posture_checks_remediation_settings_instance = DevicePostureChecksRemediationSettings.from_json(json)
# print the JSON string representation of the object
print(DevicePostureChecksRemediationSettings.to_json())

# convert the object into a dict
device_posture_checks_remediation_settings_dict = device_posture_checks_remediation_settings_instance.to_dict()
# create an instance of DevicePostureChecksRemediationSettings from a dict
device_posture_checks_remediation_settings_from_dict = DevicePostureChecksRemediationSettings.from_dict(device_posture_checks_remediation_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


