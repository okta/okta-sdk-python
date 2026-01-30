# StreamConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aud** | [**StreamConfigurationAud**](StreamConfigurationAud.md) |  | [optional] 
**delivery** | [**StreamConfigurationDelivery**](StreamConfigurationDelivery.md) |  | 
**events_delivered** | **List[str]** | The events (mapped by the array of event type URIs) that the transmitter actually delivers to the SSF Stream.  A read-only parameter that is set by the transmitter. If this parameter is included in the request, the value must match the expected value from the transmitter. | [optional] 
**events_requested** | **List[str]** | The events (mapped by the array of event type URIs) that the receiver wants to receive | 
**events_supported** | **List[str]** | An array of event type URIs that the transmitter supports.  A read-only parameter that is set by the transmitter. If this parameter is included in the request, the value must match the expected value from the transmitter. | [optional] 
**format** | **str** | The Subject Identifier format expected for any SET transmitted. | [optional] 
**iss** | **str** | The issuer used in Security Event Tokens (SETs). This value is set as &#x60;iss&#x60; in the claim.  A read-only parameter that is set by the transmitter. If this parameter is included in the request, the value must match the expected value from the transmitter. | [optional] 
**min_verification_interval** | **int** | The minimum amount of time, in seconds, between two verification requests.  A read-only parameter that is set by the transmitter. If this parameter is included in the request, the value must match the expected value from the transmitter. | [optional] 
**stream_id** | **str** | The ID of the SSF Stream configuration | [optional] 

## Example

```python
from okta.models.stream_configuration import StreamConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of StreamConfiguration from a JSON string
stream_configuration_instance = StreamConfiguration.from_json(json)
# print the JSON string representation of the object
print(StreamConfiguration.to_json())

# convert the object into a dict
stream_configuration_dict = stream_configuration_instance.to_dict()
# create an instance of StreamConfiguration from a dict
stream_configuration_from_dict = StreamConfiguration.from_dict(stream_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


