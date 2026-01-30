# StreamConfigurationCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery** | [**StreamConfigurationDelivery**](StreamConfigurationDelivery.md) |  | 
**events_requested** | **List[str]** | The events (mapped by the array of event type URIs) that the receiver wants to receive | 
**format** | **str** | The Subject Identifier format expected for any SET transmitted. | [optional] 

## Example

```python
from okta.models.stream_configuration_create_request import StreamConfigurationCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StreamConfigurationCreateRequest from a JSON string
stream_configuration_create_request_instance = StreamConfigurationCreateRequest.from_json(json)
# print the JSON string representation of the object
print(StreamConfigurationCreateRequest.to_json())

# convert the object into a dict
stream_configuration_create_request_dict = stream_configuration_create_request_instance.to_dict()
# create an instance of StreamConfigurationCreateRequest from a dict
stream_configuration_create_request_from_dict = StreamConfigurationCreateRequest.from_dict(stream_configuration_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


