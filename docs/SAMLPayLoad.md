# SAMLPayLoad


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SAMLPayLoadData**](SAMLPayLoadData.md) |  | [optional] 
**event_type** | **str** | The type of inline hook. The SAML assertion inline hook type is &#x60;com.okta.saml.tokens.transform&#x60;. | [optional] 
**source** | **str** | The ID and URL of the SAML assertion inline hook | [optional] 

## Example

```python
from okta.models.saml_pay_load import SAMLPayLoad

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoad from a JSON string
saml_pay_load_instance = SAMLPayLoad.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoad.to_json())

# convert the object into a dict
saml_pay_load_dict = saml_pay_load_instance.to_dict()
# create an instance of SAMLPayLoad from a dict
saml_pay_load_from_dict = SAMLPayLoad.from_dict(saml_pay_load_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


