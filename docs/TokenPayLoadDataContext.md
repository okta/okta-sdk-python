# TokenPayLoadDataContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**InlineHookRequestObject**](InlineHookRequestObject.md) |  | [optional] 
**session** | [**BaseContextSession**](BaseContextSession.md) |  | [optional] 
**user** | [**BaseContextUser**](BaseContextUser.md) |  | [optional] 
**protocol** | [**TokenPayLoadDataContextAllOfProtocol**](TokenPayLoadDataContextAllOfProtocol.md) |  | [optional] 
**policy** | [**TokenPayLoadDataContextAllOfPolicy**](TokenPayLoadDataContextAllOfPolicy.md) |  | [optional] 

## Example

```python
from okta.models.token_pay_load_data_context import TokenPayLoadDataContext

# TODO update the JSON string below
json = "{}"
# create an instance of TokenPayLoadDataContext from a JSON string
token_pay_load_data_context_instance = TokenPayLoadDataContext.from_json(json)
# print the JSON string representation of the object
print(TokenPayLoadDataContext.to_json())

# convert the object into a dict
token_pay_load_data_context_dict = token_pay_load_data_context_instance.to_dict()
# create an instance of TokenPayLoadDataContext from a dict
token_pay_load_data_context_from_dict = TokenPayLoadDataContext.from_dict(token_pay_load_data_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


