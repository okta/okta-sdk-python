# LogGeolocation

The latitude and longitude of the geolocation where an action was performed. The object is formatted according to the [ISO 6709](https://www.iso.org/obp/ui/fr/#iso:std:iso:6709:ed-3:v1:en) standard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | Latitude which uses two digits for the [integer part](https://www.iso.org/obp/ui/fr/#iso:std:iso:6709:ed-3:v1:en#Latitude) | [optional] [readonly] 
**lon** | **float** | Longitude which uses three digits for the [integer part](https://www.iso.org/obp/ui/fr/#iso:std:iso:6709:ed-3:v1:en#Longitude) | [optional] [readonly] 

## Example

```python
from okta.models.log_geolocation import LogGeolocation

# TODO update the JSON string below
json = "{}"
# create an instance of LogGeolocation from a JSON string
log_geolocation_instance = LogGeolocation.from_json(json)
# print the JSON string representation of the object
print(LogGeolocation.to_json())

# convert the object into a dict
log_geolocation_dict = log_geolocation_instance.to_dict()
# create an instance of LogGeolocation from a dict
log_geolocation_from_dict = LogGeolocation.from_dict(log_geolocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


