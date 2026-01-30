# SocialAuthToken

The social authentication token object provides the tokens and associated metadata provided by social providers during social authentication.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** | Timestamp when the object expires | [optional] [readonly] 
**id** | **str** | Unique identifier for the token | [optional] [readonly] 
**scopes** | **List[str]** | The scopes that the token is good for | [optional] [readonly] 
**token** | **str** | The raw token | [optional] [readonly] 
**token_auth_scheme** | **str** | The token authentication scheme as defined by the social provider | [optional] [readonly] 
**token_type** | **str** | The type of token defined by the [OAuth Token Exchange Spec](https://tools.ietf.org/html/draft-ietf-oauth-token-exchange-07#section-3) | [optional] [readonly] 

## Example

```python
from okta.models.social_auth_token import SocialAuthToken

# TODO update the JSON string below
json = "{}"
# create an instance of SocialAuthToken from a JSON string
social_auth_token_instance = SocialAuthToken.from_json(json)
# print the JSON string representation of the object
print(SocialAuthToken.to_json())

# convert the object into a dict
social_auth_token_dict = social_auth_token_instance.to_dict()
# create an instance of SocialAuthToken from a dict
social_auth_token_from_dict = SocialAuthToken.from_dict(social_auth_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


