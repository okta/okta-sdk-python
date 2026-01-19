# OAuth2RefreshTokenLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**app** | [**AppResourceHrefObject**](AppResourceHrefObject.md) | Link to the app resource | [optional] 
**revoke** | [**OAuth2RefreshTokenLinksAllOfRevoke**](OAuth2RefreshTokenLinksAllOfRevoke.md) |  | [optional] 
**client** | [**AppResourceHrefObject**](AppResourceHrefObject.md) | Link to the client resource | [optional] 
**user** | [**UserResourceHrefObject**](UserResourceHrefObject.md) | Link to the user resource | [optional] 
**authorization_server** | [**AuthorizationServerResourceHrefObject**](AuthorizationServerResourceHrefObject.md) | Link to the Token authorization server resource | [optional] 

## Example

```python
from okta.models.o_auth2_refresh_token_links import OAuth2RefreshTokenLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2RefreshTokenLinks from a JSON string
o_auth2_refresh_token_links_instance = OAuth2RefreshTokenLinks.from_json(json)
# print the JSON string representation of the object
print(OAuth2RefreshTokenLinks.to_json())

# convert the object into a dict
o_auth2_refresh_token_links_dict = o_auth2_refresh_token_links_instance.to_dict()
# create an instance of OAuth2RefreshTokenLinks from a dict
o_auth2_refresh_token_links_from_dict = OAuth2RefreshTokenLinks.from_dict(o_auth2_refresh_token_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


