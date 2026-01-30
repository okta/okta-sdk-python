# StreamConfigurationAud

The audience used in the SET. This value is set as `aud` in the claim.  A read-only parameter that is set by the transmitter. If this parameter is included in the request, the value must match the expected value from the transmitter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from okta.models.stream_configuration_aud import StreamConfigurationAud

# TODO update the JSON string below
json = "{}"
# create an instance of StreamConfigurationAud from a JSON string
stream_configuration_aud_instance = StreamConfigurationAud.from_json(json)
# print the JSON string representation of the object
print(StreamConfigurationAud.to_json())

# convert the object into a dict
stream_configuration_aud_dict = stream_configuration_aud_instance.to_dict()
# create an instance of StreamConfigurationAud from a dict
stream_configuration_aud_from_dict = StreamConfigurationAud.from_dict(stream_configuration_aud_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


