# GracePeriodExpiry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | A time duration in ISO 8601 duration format. | [optional] 

## Example

```python
from okta.models.grace_period_expiry import GracePeriodExpiry

# TODO update the JSON string below
json = "{}"
# create an instance of GracePeriodExpiry from a JSON string
grace_period_expiry_instance = GracePeriodExpiry.from_json(json)
# print the JSON string representation of the object
print(GracePeriodExpiry.to_json())

# convert the object into a dict
grace_period_expiry_dict = grace_period_expiry_instance.to_dict()
# create an instance of GracePeriodExpiry from a dict
grace_period_expiry_from_dict = GracePeriodExpiry.from_dict(grace_period_expiry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


