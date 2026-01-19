# DRStatusItem

Status whether a domain has been failed over or not

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain for your org | [optional] 
**is_failed_over** | **bool** | Indicates if the domain has been failed over | [optional] 

## Example

```python
from okta.models.dr_status_item import DRStatusItem

# TODO update the JSON string below
json = "{}"
# create an instance of DRStatusItem from a JSON string
dr_status_item_instance = DRStatusItem.from_json(json)
# print the JSON string representation of the object
print(DRStatusItem.to_json())

# convert the object into a dict
dr_status_item_dict = dr_status_item_instance.to_dict()
# create an instance of DRStatusItem from a dict
dr_status_item_from_dict = DRStatusItem.from_dict(dr_status_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


