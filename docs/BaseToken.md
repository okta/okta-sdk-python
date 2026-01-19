# BaseToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claims** | **object** | Claims included in the token. Consists of name-value pairs for each included claim. For descriptions of the claims that you can include, see the Okta [OpenID Connect and OAuth 2.0 API reference](/openapi/okta-oauth/guides/overview/#claims). | [optional] 
**token** | [**BaseTokenToken**](BaseTokenToken.md) |  | [optional] 

## Example

```python
from okta.models.base_token import BaseToken

# TODO update the JSON string below
json = "{}"
# create an instance of BaseToken from a JSON string
base_token_instance = BaseToken.from_json(json)
# print the JSON string representation of the object
print(BaseToken.to_json())

# convert the object into a dict
base_token_dict = base_token_instance.to_dict()
# create an instance of BaseToken from a dict
base_token_from_dict = BaseToken.from_dict(base_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


