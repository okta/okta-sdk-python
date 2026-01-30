# FulfillmentDataOrderDetails

Information about the fulfillment order that includes the factor’s make and model, the custom configuration of the factor, and inventory details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customization_id** | **str** | ID for the set of custom configurations of the requested factor | [optional] 
**inventory_product_id** | **str** | ID for the specific inventory bucket of the requested factor | [optional] 
**product_id** | **str** | ID for the make and model of the requested factor | [optional] 

## Example

```python
from okta.models.fulfillment_data_order_details import FulfillmentDataOrderDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FulfillmentDataOrderDetails from a JSON string
fulfillment_data_order_details_instance = FulfillmentDataOrderDetails.from_json(json)
# print the JSON string representation of the object
print(FulfillmentDataOrderDetails.to_json())

# convert the object into a dict
fulfillment_data_order_details_dict = fulfillment_data_order_details_instance.to_dict()
# create an instance of FulfillmentDataOrderDetails from a dict
fulfillment_data_order_details_from_dict = FulfillmentDataOrderDetails.from_dict(fulfillment_data_order_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


