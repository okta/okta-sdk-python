# DevicePostureChecksRemediationSettingsLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_url** | **str** | Default URL for the link. This property is only relevant if type is set to &#x60;BUILTIN&#x60;. If type is set to &#x60;CUSTOM&#x60;, this field is ignored. | [optional] 
**custom_url** | **str** | Custom URL for the link | [optional] 

## Example

```python
from okta.models.device_posture_checks_remediation_settings_link import DevicePostureChecksRemediationSettingsLink

# TODO update the JSON string below
json = "{}"
# create an instance of DevicePostureChecksRemediationSettingsLink from a JSON string
device_posture_checks_remediation_settings_link_instance = DevicePostureChecksRemediationSettingsLink.from_json(json)
# print the JSON string representation of the object
print(DevicePostureChecksRemediationSettingsLink.to_json())

# convert the object into a dict
device_posture_checks_remediation_settings_link_dict = device_posture_checks_remediation_settings_link_instance.to_dict()
# create an instance of DevicePostureChecksRemediationSettingsLink from a dict
device_posture_checks_remediation_settings_link_from_dict = DevicePostureChecksRemediationSettingsLink.from_dict(device_posture_checks_remediation_settings_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


