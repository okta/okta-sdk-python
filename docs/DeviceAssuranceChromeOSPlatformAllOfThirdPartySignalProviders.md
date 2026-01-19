# DeviceAssuranceChromeOSPlatformAllOfThirdPartySignalProviders

Settings for third-party signal providers (based on the `CHROMEOS` platform)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dtc** | [**DTCChromeOS**](DTCChromeOS.md) |  | [optional] 
**device_posture_id_p** | [**DevicePostureIdP**](DevicePostureIdP.md) |  | [optional] 

## Example

```python
from okta.models.device_assurance_chrome_os_platform_all_of_third_party_signal_providers import DeviceAssuranceChromeOSPlatformAllOfThirdPartySignalProviders

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAssuranceChromeOSPlatformAllOfThirdPartySignalProviders from a JSON string
device_assurance_chrome_os_platform_all_of_third_party_signal_providers_instance = DeviceAssuranceChromeOSPlatformAllOfThirdPartySignalProviders.from_json(json)
# print the JSON string representation of the object
print(DeviceAssuranceChromeOSPlatformAllOfThirdPartySignalProviders.to_json())

# convert the object into a dict
device_assurance_chrome_os_platform_all_of_third_party_signal_providers_dict = device_assurance_chrome_os_platform_all_of_third_party_signal_providers_instance.to_dict()
# create an instance of DeviceAssuranceChromeOSPlatformAllOfThirdPartySignalProviders from a dict
device_assurance_chrome_os_platform_all_of_third_party_signal_providers_from_dict = DeviceAssuranceChromeOSPlatformAllOfThirdPartySignalProviders.from_dict(device_assurance_chrome_os_platform_all_of_third_party_signal_providers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


