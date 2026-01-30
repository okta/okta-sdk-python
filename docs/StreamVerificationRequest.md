# StreamVerificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | An arbitrary string that Okta as a transmitter must echo back to the Event Receiver in the Verification Event&#39;s payload | [optional] 
**stream_id** | **str** | The ID of the SSF Stream Configuration | 

## Example

```python
from okta.models.stream_verification_request import StreamVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StreamVerificationRequest from a JSON string
stream_verification_request_instance = StreamVerificationRequest.from_json(json)
# print the JSON string representation of the object
print(StreamVerificationRequest.to_json())

# convert the object into a dict
stream_verification_request_dict = stream_verification_request_instance.to_dict()
# create an instance of StreamVerificationRequest from a dict
stream_verification_request_from_dict = StreamVerificationRequest.from_dict(stream_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


