# OAuth2RefreshTokenLinksAllOfRevoke

Link to revoke the refresh Token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Link URI | [optional] 
**hints** | [**OAuth2RefreshTokenLinksAllOfRevokeAllOfHints**](OAuth2RefreshTokenLinksAllOfRevokeAllOfHints.md) |  | [optional] 

## Example

```python
from okta.models.o_auth2_refresh_token_links_all_of_revoke import OAuth2RefreshTokenLinksAllOfRevoke

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2RefreshTokenLinksAllOfRevoke from a JSON string
o_auth2_refresh_token_links_all_of_revoke_instance = OAuth2RefreshTokenLinksAllOfRevoke.from_json(json)
# print the JSON string representation of the object
print(OAuth2RefreshTokenLinksAllOfRevoke.to_json())

# convert the object into a dict
o_auth2_refresh_token_links_all_of_revoke_dict = o_auth2_refresh_token_links_all_of_revoke_instance.to_dict()
# create an instance of OAuth2RefreshTokenLinksAllOfRevoke from a dict
o_auth2_refresh_token_links_all_of_revoke_from_dict = OAuth2RefreshTokenLinksAllOfRevoke.from_dict(o_auth2_refresh_token_links_all_of_revoke_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


