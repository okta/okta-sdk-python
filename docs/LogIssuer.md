# LogIssuer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 

## Example

```python
from okta.models.log_issuer import LogIssuer

# TODO update the JSON string below
json = "{}"
# create an instance of LogIssuer from a JSON string
log_issuer_instance = LogIssuer.from_json(json)
# print the JSON string representation of the object
print(LogIssuer.to_json())

# convert the object into a dict
log_issuer_dict = log_issuer_instance.to_dict()
# create an instance of LogIssuer from a dict
log_issuer_from_dict = LogIssuer.from_dict(log_issuer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


