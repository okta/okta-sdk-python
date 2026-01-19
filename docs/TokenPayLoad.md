# TokenPayLoad


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TokenPayLoadData**](TokenPayLoadData.md) |  | [optional] 
**event_type** | **str** | The type of inline hook. The token inline hook type is &#x60;com.okta.oauth2.tokens.transform&#x60;. | [optional] 
**source** | **str** | The URL of the token inline hook | [optional] 

## Example

```python
from okta.models.token_pay_load import TokenPayLoad

# TODO update the JSON string below
json = "{}"
# create an instance of TokenPayLoad from a JSON string
token_pay_load_instance = TokenPayLoad.from_json(json)
# print the JSON string representation of the object
print(TokenPayLoad.to_json())

# convert the object into a dict
token_pay_load_dict = token_pay_load_instance.to_dict()
# create an instance of TokenPayLoad from a dict
token_pay_load_from_dict = TokenPayLoad.from_dict(token_pay_load_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


