# StreamConfigurationDelivery

Contains information about the intended SET delivery method by the receiver

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_header** | **str** | The HTTP Authorization header that is included for each HTTP POST request | [optional] 
**endpoint_url** | **str** | The target endpoint URL where the transmitter delivers the SET using HTTP POST requests | 
**method** | **str** | The delivery method that the transmitter uses for delivering a SET | 

## Example

```python
from okta.models.stream_configuration_delivery import StreamConfigurationDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of StreamConfigurationDelivery from a JSON string
stream_configuration_delivery_instance = StreamConfigurationDelivery.from_json(json)
# print the JSON string representation of the object
print(StreamConfigurationDelivery.to_json())

# convert the object into a dict
stream_configuration_delivery_dict = stream_configuration_delivery_instance.to_dict()
# create an instance of StreamConfigurationDelivery from a dict
stream_configuration_delivery_from_dict = StreamConfigurationDelivery.from_dict(stream_configuration_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


