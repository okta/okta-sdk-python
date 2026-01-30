# OAuth2ClientSecretRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret** | **str** | The OAuth 2.0 client secret string | [optional] 
**status** | **str** | Status of the OAuth 2.0 Client Secret | [optional] 

## Example

```python
from okta.models.o_auth2_client_secret_request_body import OAuth2ClientSecretRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ClientSecretRequestBody from a JSON string
o_auth2_client_secret_request_body_instance = OAuth2ClientSecretRequestBody.from_json(json)
# print the JSON string representation of the object
print(OAuth2ClientSecretRequestBody.to_json())

# convert the object into a dict
o_auth2_client_secret_request_body_dict = o_auth2_client_secret_request_body_instance.to_dict()
# create an instance of OAuth2ClientSecretRequestBody from a dict
o_auth2_client_secret_request_body_from_dict = OAuth2ClientSecretRequestBody.from_dict(o_auth2_client_secret_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


