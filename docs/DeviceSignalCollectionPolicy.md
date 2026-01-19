# DeviceSignalCollectionPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | **str** | Policy conditions aren&#39;t supported. Conditions are applied at the rule level for this policy type. | [optional] 

## Example

```python
from okta.models.device_signal_collection_policy import DeviceSignalCollectionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSignalCollectionPolicy from a JSON string
device_signal_collection_policy_instance = DeviceSignalCollectionPolicy.from_json(json)
# print the JSON string representation of the object
print(DeviceSignalCollectionPolicy.to_json())

# convert the object into a dict
device_signal_collection_policy_dict = device_signal_collection_policy_instance.to_dict()
# create an instance of DeviceSignalCollectionPolicy from a dict
device_signal_collection_policy_from_dict = DeviceSignalCollectionPolicy.from_dict(device_signal_collection_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


