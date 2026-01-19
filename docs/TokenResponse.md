# TokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | An access token. | [optional] 
**device_secret** | **str** | An opaque device secret. This is returned if the &#x60;device_sso&#x60; scope is granted. | [optional] 
**expires_in** | **int** | The expiration time of the access token in seconds. | [optional] 
**id_token** | **str** | An ID token. This is returned if the &#x60;openid&#x60; scope is granted. | [optional] 
**issued_token_type** | [**TokenType**](TokenType.md) |  | [optional] 
**refresh_token** | **str** | An opaque refresh token. This is returned if the &#x60;offline_access&#x60; scope is granted. | [optional] 
**scope** | **str** | The scopes contained in the access token. | [optional] 
**token_type** | [**TokenResponseTokenType**](TokenResponseTokenType.md) |  | [optional] 

## Example

```python
from okta.models.token_response import TokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenResponse from a JSON string
token_response_instance = TokenResponse.from_json(json)
# print the JSON string representation of the object
print(TokenResponse.to_json())

# convert the object into a dict
token_response_dict = token_response_instance.to_dict()
# create an instance of TokenResponse from a dict
token_response_from_dict = TokenResponse.from_dict(token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


