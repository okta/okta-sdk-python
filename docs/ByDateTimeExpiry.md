# ByDateTimeExpiry

An ISO 8601 formatted date and time for BY_DATE_TIME grace period type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **datetime** | The expiry date and time in ISO 8601 format. | [optional] 

## Example

```python
from okta.models.by_date_time_expiry import ByDateTimeExpiry

# TODO update the JSON string below
json = "{}"
# create an instance of ByDateTimeExpiry from a JSON string
by_date_time_expiry_instance = ByDateTimeExpiry.from_json(json)
# print the JSON string representation of the object
print(ByDateTimeExpiry.to_json())

# convert the object into a dict
by_date_time_expiry_dict = by_date_time_expiry_instance.to_dict()
# create an instance of ByDateTimeExpiry from a dict
by_date_time_expiry_from_dict = ByDateTimeExpiry.from_dict(by_date_time_expiry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


