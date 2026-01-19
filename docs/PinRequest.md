# PinRequest

Pin request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator_enrollment_id** | **str** | ID for a WebAuthn preregistration factor in Okta | [optional] 
**fulfillment_provider** | **str** | Name of the fulfillment provider for the WebAuthn preregistration factor | [optional] 
**user_id** | **str** | ID of an existing Okta user | [optional] 

## Example

```python
from okta.models.pin_request import PinRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PinRequest from a JSON string
pin_request_instance = PinRequest.from_json(json)
# print the JSON string representation of the object
print(PinRequest.to_json())

# convert the object into a dict
pin_request_dict = pin_request_instance.to_dict()
# create an instance of PinRequest from a dict
pin_request_from_dict = PinRequest.from_dict(pin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


