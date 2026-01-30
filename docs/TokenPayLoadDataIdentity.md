# TokenPayLoadDataIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claims** | **object** | Claims included in the token. Consists of name-value pairs for each included claim. For descriptions of the claims that you can include, see the Okta [OpenID Connect and OAuth 2.0 API reference](/openapi/okta-oauth/guides/overview/#claims). | [optional] 
**token** | [**BaseTokenToken**](BaseTokenToken.md) |  | [optional] 

## Example

```python
from okta.models.token_pay_load_data_identity import TokenPayLoadDataIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of TokenPayLoadDataIdentity from a JSON string
token_pay_load_data_identity_instance = TokenPayLoadDataIdentity.from_json(json)
# print the JSON string representation of the object
print(TokenPayLoadDataIdentity.to_json())

# convert the object into a dict
token_pay_load_data_identity_dict = token_pay_load_data_identity_instance.to_dict()
# create an instance of TokenPayLoadDataIdentity from a dict
token_pay_load_data_identity_from_dict = TokenPayLoadDataIdentity.from_dict(token_pay_load_data_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


