# SAMLPayLoadDataContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**InlineHookRequestObject**](InlineHookRequestObject.md) |  | [optional] 
**session** | [**BaseContextSession**](BaseContextSession.md) |  | [optional] 
**user** | [**BaseContextUser**](BaseContextUser.md) |  | [optional] 
**protocol** | [**SAMLPayLoadDataContextAllOfProtocol**](SAMLPayLoadDataContextAllOfProtocol.md) |  | [optional] 

## Example

```python
from okta.models.saml_pay_load_data_context import SAMLPayLoadDataContext

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPayLoadDataContext from a JSON string
saml_pay_load_data_context_instance = SAMLPayLoadDataContext.from_json(json)
# print the JSON string representation of the object
print(SAMLPayLoadDataContext.to_json())

# convert the object into a dict
saml_pay_load_data_context_dict = saml_pay_load_data_context_instance.to_dict()
# create an instance of SAMLPayLoadDataContext from a dict
saml_pay_load_data_context_from_dict = SAMLPayLoadDataContext.from_dict(saml_pay_load_data_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


