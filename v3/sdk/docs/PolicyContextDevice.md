# PolicyContextDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | **str** | The platform of the device, for example, IOS. | [optional] 
**registered** | **bool** | If the device is registered | [optional] 
**managed** | **bool** | If the device is managed | [optional] 

## Example

```python
from openapi_client.models.policy_context_device import PolicyContextDevice

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyContextDevice from a JSON string
policy_context_device_instance = PolicyContextDevice.from_json(json)
# print the JSON string representation of the object
print(PolicyContextDevice.to_json())

# convert the object into a dict
policy_context_device_dict = policy_context_device_instance.to_dict()
# create an instance of PolicyContextDevice from a dict
policy_context_device_form_dict = policy_context_device.from_dict(policy_context_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


