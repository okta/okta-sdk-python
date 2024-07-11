# LogTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **Dict[str, object]** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 

## Example

```python
from okta.models.log_transaction import LogTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of LogTransaction from a JSON string
log_transaction_instance = LogTransaction.from_json(json)
# print the JSON string representation of the object
print(LogTransaction.to_json())

# convert the object into a dict
log_transaction_dict = log_transaction_instance.to_dict()
# create an instance of LogTransaction from a dict
log_transaction_from_dict = LogTransaction.from_dict(log_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


