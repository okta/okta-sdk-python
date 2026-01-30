# OAuth2Settings

OAuth 2.0 configuration used for authType `OAUTH2`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorize_endpoint** | **str** | The URL to the authorization server&#39;s authorization endpoint | 
**client_id** | **str** | The OAuth 2.0 client identifier | 
**client_secret** | **str** | The OAuth 2.0 client secret | 
**scopes** | **List[str]** | List of OAuth 2.0 scopes | [optional] 
**token_endpoint** | **str** | The URL to the authorization server&#39;s token endpoint | 

## Example

```python
from okta.models.o_auth2_settings import OAuth2Settings

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Settings from a JSON string
o_auth2_settings_instance = OAuth2Settings.from_json(json)
# print the JSON string representation of the object
print(OAuth2Settings.to_json())

# convert the object into a dict
o_auth2_settings_dict = o_auth2_settings_instance.to_dict()
# create an instance of OAuth2Settings from a dict
o_auth2_settings_from_dict = OAuth2Settings.from_dict(o_auth2_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


