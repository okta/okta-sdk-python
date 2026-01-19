# ByDurationExpiry

A time duration specified as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). Must be between 1 and 180 days inclusive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | A time duration in ISO 8601 duration format. | [optional] 

## Example

```python
from okta.models.by_duration_expiry import ByDurationExpiry

# TODO update the JSON string below
json = "{}"
# create an instance of ByDurationExpiry from a JSON string
by_duration_expiry_instance = ByDurationExpiry.from_json(json)
# print the JSON string representation of the object
print(ByDurationExpiry.to_json())

# convert the object into a dict
by_duration_expiry_dict = by_duration_expiry_instance.to_dict()
# create an instance of ByDurationExpiry from a dict
by_duration_expiry_from_dict = ByDurationExpiry.from_dict(by_duration_expiry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


