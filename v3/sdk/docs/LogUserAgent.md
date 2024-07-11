# LogUserAgent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser** | **str** |  | [optional] [readonly] 
**os** | **str** |  | [optional] [readonly] 
**raw_user_agent** | **str** |  | [optional] [readonly] 

## Example

```python
from okta.models.log_user_agent import LogUserAgent

# TODO update the JSON string below
json = "{}"
# create an instance of LogUserAgent from a JSON string
log_user_agent_instance = LogUserAgent.from_json(json)
# print the JSON string representation of the object
print(LogUserAgent.to_json())

# convert the object into a dict
log_user_agent_dict = log_user_agent_instance.to_dict()
# create an instance of LogUserAgent from a dict
log_user_agent_from_dict = LogUserAgent.from_dict(log_user_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


