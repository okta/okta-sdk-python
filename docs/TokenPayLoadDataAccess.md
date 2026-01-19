# TokenPayLoadDataAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claims** | **object** | Claims included in the token. Consists of name-value pairs for each included claim. For descriptions of the claims that you can include, see the Okta [OpenID Connect and OAuth 2.0 API reference](/openapi/okta-oauth/guides/overview/#claims). | [optional] 
**token** | [**BaseTokenToken**](BaseTokenToken.md) |  | [optional] 
**scopes** | **object** | The scopes contained in the token. For descriptions of the scopes that you can include, see the Okta [OpenID Connect and OAuth 2.0 API reference](/openapi/okta-oauth/guides/overview/#scopes). | [optional] 

## Example

```python
from okta.models.token_pay_load_data_access import TokenPayLoadDataAccess

# TODO update the JSON string below
json = "{}"
# create an instance of TokenPayLoadDataAccess from a JSON string
token_pay_load_data_access_instance = TokenPayLoadDataAccess.from_json(json)
# print the JSON string representation of the object
print(TokenPayLoadDataAccess.to_json())

# convert the object into a dict
token_pay_load_data_access_dict = token_pay_load_data_access_instance.to_dict()
# create an instance of TokenPayLoadDataAccess from a dict
token_pay_load_data_access_from_dict = TokenPayLoadDataAccess.from_dict(token_pay_load_data_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


