# LogGeographicalContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] [readonly] 
**country** | **str** |  | [optional] [readonly] 
**geolocation** | [**LogGeolocation**](LogGeolocation.md) |  | [optional] 
**postal_code** | **str** |  | [optional] [readonly] 
**state** | **str** |  | [optional] [readonly] 

## Example

```python
from okta.models.log_geographical_context import LogGeographicalContext

# TODO update the JSON string below
json = "{}"
# create an instance of LogGeographicalContext from a JSON string
log_geographical_context_instance = LogGeographicalContext.from_json(json)
# print the JSON string representation of the object
print(LogGeographicalContext.to_json())

# convert the object into a dict
log_geographical_context_dict = log_geographical_context_instance.to_dict()
# create an instance of LogGeographicalContext from a dict
log_geographical_context_from_dict = LogGeographicalContext.from_dict(log_geographical_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


