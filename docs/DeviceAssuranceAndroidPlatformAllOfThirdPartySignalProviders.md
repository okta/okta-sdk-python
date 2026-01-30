# DeviceAssuranceAndroidPlatformAllOfThirdPartySignalProviders

Settings for third-party signal providers (based on the `ANDROID` platform)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**android_device_trust** | [**AndroidDeviceTrust**](AndroidDeviceTrust.md) |  | [optional] 
**device_posture_id_p** | [**DevicePostureIdP**](DevicePostureIdP.md) |  | [optional] 

## Example

```python
from okta.models.device_assurance_android_platform_all_of_third_party_signal_providers import DeviceAssuranceAndroidPlatformAllOfThirdPartySignalProviders

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAssuranceAndroidPlatformAllOfThirdPartySignalProviders from a JSON string
device_assurance_android_platform_all_of_third_party_signal_providers_instance = DeviceAssuranceAndroidPlatformAllOfThirdPartySignalProviders.from_json(json)
# print the JSON string representation of the object
print(DeviceAssuranceAndroidPlatformAllOfThirdPartySignalProviders.to_json())

# convert the object into a dict
device_assurance_android_platform_all_of_third_party_signal_providers_dict = device_assurance_android_platform_all_of_third_party_signal_providers_instance.to_dict()
# create an instance of DeviceAssuranceAndroidPlatformAllOfThirdPartySignalProviders from a dict
device_assurance_android_platform_all_of_third_party_signal_providers_from_dict = DeviceAssuranceAndroidPlatformAllOfThirdPartySignalProviders.from_dict(device_assurance_android_platform_all_of_third_party_signal_providers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


