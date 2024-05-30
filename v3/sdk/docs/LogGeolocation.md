# LogGeolocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** |  | [optional] [readonly] 
**lon** | **float** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.log_geolocation import LogGeolocation

# TODO update the JSON string below
json = "{}"
# create an instance of LogGeolocation from a JSON string
log_geolocation_instance = LogGeolocation.from_json(json)
# print the JSON string representation of the object
print(LogGeolocation.to_json())

# convert the object into a dict
log_geolocation_dict = log_geolocation_instance.to_dict()
# create an instance of LogGeolocation from a dict
log_geolocation_form_dict = log_geolocation.from_dict(log_geolocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


