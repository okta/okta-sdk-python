# SAMLPayloadExecute

SAML assertion inline hook request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_event_version** | **str** | The inline hook cloud version | [optional] 
**content_type** | **str** | The inline hook request header content | [optional] 
**event_id** | **str** | The individual inline hook request ID | [optional] 
**event_time** | **str** | The time the inline hook request was sent | [optional] 
**event_type_version** | **str** | The inline hook version | [optional] 
**data** | [**SAMLPayLoadData**](SAMLPayLoadData.md) |  | [optional] 
**event_type** | **str** | The type of inline hook. The SAML assertion inline hook type is &#x60;com.okta.saml.tokens.transform&#x60;. | [optional] 
**source** | **str** | The ID and URL of the SAML assertion inline hook | [optional] 

## Example

```python
from okta.models.saml_payload_execute import SAMLPayloadExecute

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayloadExecute from a JSON string
saml_payload_execute_instance = SAMLPayloadExecute.from_json(json)
# print the JSON string representation of the object
print(SAMLPayloadExecute.to_json())

# convert the object into a dict
saml_payload_execute_dict = saml_payload_execute_instance.to_dict()
# create an instance of SAMLPayloadExecute from a dict
saml_payload_execute_from_dict = SAMLPayloadExecute.from_dict(saml_payload_execute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


