# LogSecurityContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_number** | **int** |  | [optional] [readonly] 
**as_org** | **str** |  | [optional] [readonly] 
**domain** | **str** |  | [optional] [readonly] 
**isp** | **str** |  | [optional] [readonly] 
**is_proxy** | **bool** |  | [optional] [readonly] 

## Example

```python
from okta.models.log_security_context import LogSecurityContext

# TODO update the JSON string below
json = "{}"
# create an instance of LogSecurityContext from a JSON string
log_security_context_instance = LogSecurityContext.from_json(json)
# print the JSON string representation of the object
print(LogSecurityContext.to_json())

# convert the object into a dict
log_security_context_dict = log_security_context_instance.to_dict()
# create an instance of LogSecurityContext from a dict
log_security_context_from_dict = LogSecurityContext.from_dict(log_security_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


