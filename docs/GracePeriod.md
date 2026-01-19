# GracePeriod

<x-lifecycle-container><x-lifecycle class=\"ea\"></x-lifecycle></x-lifecycle-container>Represents the Grace Period configuration for the device assurance policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | [**GracePeriodExpiry**](GracePeriodExpiry.md) |  | [optional] 
**type** | **str** | Represents the type of Grace Period configured for the device assurance policy | [optional] 

## Example

```python
from okta.models.grace_period import GracePeriod

# TODO update the JSON string below
json = "{}"
# create an instance of GracePeriod from a JSON string
grace_period_instance = GracePeriod.from_json(json)
# print the JSON string representation of the object
print(GracePeriod.to_json())

# convert the object into a dict
grace_period_dict = grace_period_instance.to_dict()
# create an instance of GracePeriod from a dict
grace_period_from_dict = GracePeriod.from_dict(grace_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


