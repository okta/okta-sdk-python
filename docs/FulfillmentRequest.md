# FulfillmentRequest

Fulfillment request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fulfillment_data** | [**List[FulfillmentDataOrderDetails]**](FulfillmentDataOrderDetails.md) | List of fulfillment order details | [optional] 
**fulfillment_provider** | **str** | Name of the fulfillment provider for the WebAuthn preregistration factor | [optional] 
**user_id** | **str** | ID of an existing Okta user | [optional] 

## Example

```python
from okta.models.fulfillment_request import FulfillmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FulfillmentRequest from a JSON string
fulfillment_request_instance = FulfillmentRequest.from_json(json)
# print the JSON string representation of the object
print(FulfillmentRequest.to_json())

# convert the object into a dict
fulfillment_request_dict = fulfillment_request_instance.to_dict()
# create an instance of FulfillmentRequest from a dict
fulfillment_request_from_dict = FulfillmentRequest.from_dict(fulfillment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


