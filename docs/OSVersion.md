# OSVersion

Specifies the OS requirement for the policy.  There are two types of OS requirements:  * **Static**: A specific OS version requirement that doesn't change until you update the policy. A static OS requirement is specified with the `osVersion.minimum` property. * **Dynamic**: An OS version requirement that is relative to the latest major OS release and security patch. A dynamic OS requirement is specified with the `osVersion.dynamicVersionRequirement` property. > **Note:** Dynamic OS requirements are available only if the **Dynamic OS version compliance** [self-service EA](/openapi/okta-management/guides/release-lifecycle/#early-access-ea) feature is enabled. You can't specify both `osVersion.minimum` and `osVersion.dynamicVersionRequirement` properties at the same time. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic_version_requirement** | [**OSVersionDynamicVersionRequirement**](OSVersionDynamicVersionRequirement.md) |  | [optional] 
**minimum** | **str** | The device version must be equal to or newer than the specified version string (maximum of three components for iOS and macOS, and maximum of four components for Android) | [optional] 

## Example

```python
from okta.models.os_version import OSVersion

# TODO update the JSON string below
json = "{}"
# create an instance of OSVersion from a JSON string
os_version_instance = OSVersion.from_json(json)
# print the JSON string representation of the object
print(OSVersion.to_json())

# convert the object into a dict
os_version_dict = os_version_instance.to_dict()
# create an instance of OSVersion from a dict
os_version_from_dict = OSVersion.from_dict(os_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


