# DeviceAssuranceWindowsPlatform


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk_encryption_type** | [**DeviceAssuranceMacOSPlatformAllOfDiskEncryptionType**](DeviceAssuranceMacOSPlatformAllOfDiskEncryptionType.md) |  | [optional] 
**os_version** | [**OSVersionFourComponents**](OSVersionFourComponents.md) |  | [optional] 
**os_version_constraints** | [**List[OSVersionConstraint]**](OSVersionConstraint.md) | &lt;x-lifecycle-container&gt;&lt;x-lifecycle class&#x3D;\&quot;ea\&quot;&gt;&lt;/x-lifecycle&gt;&lt;/x-lifecycle-container&gt;Specifies the Windows version requirements for the assurance policy. Each requirement must correspond to a different major version (Windows 11 or Windows 10). If a requirement isn&#39;t specified for a major version, then devices on that major version satisfy the condition.  There are two types of OS requirements: * **Static**: A specific Windows version requirement that doesn&#39;t change until you update the policy. A static OS Windows requirement is specified with &#x60;majorVersionConstraint&#x60; and &#x60;minimum&#x60;. * **Dynamic**: A Windows version requirement that is relative to the latest major release and security patch. A dynamic OS Windows requirement is specified with &#x60;majorVersionConstraint&#x60; and &#x60;dynamicVersionRequirement&#x60;.  &gt; **Note:** Dynamic OS requirements are available only if the **Dynamic OS version compliance** [self-service EA](/openapi/okta-management/guides/release-lifecycle/#early-access-ea) feature is enabled. The &#x60;osVersionConstraints&#x60; property is only supported for the Windows platform. You can&#39;t specify both &#x60;osVersion.minimum&#x60; and &#x60;osVersionConstraints&#x60; properties at the same time.  | [optional] 
**screen_lock_type** | [**DeviceAssuranceAndroidPlatformAllOfScreenLockType**](DeviceAssuranceAndroidPlatformAllOfScreenLockType.md) |  | [optional] 
**secure_hardware_present** | **bool** |  | [optional] 
**third_party_signal_providers** | [**DeviceAssuranceWindowsPlatformAllOfThirdPartySignalProviders**](DeviceAssuranceWindowsPlatformAllOfThirdPartySignalProviders.md) |  | [optional] 

## Example

```python
from okta.models.device_assurance_windows_platform import DeviceAssuranceWindowsPlatform

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceAssuranceWindowsPlatform from a JSON string
device_assurance_windows_platform_instance = DeviceAssuranceWindowsPlatform.from_json(json)
# print the JSON string representation of the object
print(DeviceAssuranceWindowsPlatform.to_json())

# convert the object into a dict
device_assurance_windows_platform_dict = device_assurance_windows_platform_instance.to_dict()
# create an instance of DeviceAssuranceWindowsPlatform from a dict
device_assurance_windows_platform_from_dict = DeviceAssuranceWindowsPlatform.from_dict(device_assurance_windows_platform_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


