# LogGeographicalContext

Geographical context describes a set of geographic coordinates. In addition to containing latitude and longitude data, the `GeographicalContext` object also contains address data of postal code-level granularity. Within the `Client` object, the geographical context refers to the physical location of the client when it sends the request that triggers this event. All `Transaction` events with `type` equal to `WEB` have a geographical context set. `Transaction` events with `type` equal to `JOB` don't have a geographical context set. The geographical context data can be missing if the geographical data for a request can't be resolved.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | The city that encompasses the area that contains the geolocation coordinates, if available (for example, Seattle, San Francisco) | [optional] [readonly] 
**country** | **str** | Full name of the country that encompasses the area that contains the geolocation coordinates (for example, France, Uganda) | [optional] [readonly] 
**geolocation** | [**LogGeolocation**](LogGeolocation.md) |  | [optional] 
**postal_code** | **str** | Postal code of the area that encompasses the geolocation coordinates | [optional] [readonly] 
**state** | **str** | Full name of the state or province that encompasses the area that contains the geolocation coordinates (for example, Montana, Ontario) | [optional] [readonly] 

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


