# TokenPayLoadData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**TokenPayLoadDataContext**](TokenPayLoadDataContext.md) |  | [optional] 
**identity** | [**TokenPayLoadDataIdentity**](TokenPayLoadDataIdentity.md) |  | [optional] 
**access** | [**TokenPayLoadDataAccess**](TokenPayLoadDataAccess.md) |  | [optional] 
**refresh_token** | [**RefreshToken**](RefreshToken.md) |  | [optional] 

## Example

```python
from okta.models.token_pay_load_data import TokenPayLoadData

# TODO update the JSON string below
json = "{}"
# create an instance of TokenPayLoadData from a JSON string
token_pay_load_data_instance = TokenPayLoadData.from_json(json)
# print the JSON string representation of the object
print(TokenPayLoadData.to_json())

# convert the object into a dict
token_pay_load_data_dict = token_pay_load_data_instance.to_dict()
# create an instance of TokenPayLoadData from a dict
token_pay_load_data_from_dict = TokenPayLoadData.from_dict(token_pay_load_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


