# OAuth2ClientLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**grants** | [**GrantResourcesHrefObject**](GrantResourcesHrefObject.md) | Link to the grant resources | [optional] 
**tokens** | [**TokenResourcesHrefObject**](TokenResourcesHrefObject.md) | Link to the token resources | [optional] 

## Example

```python
from okta.models.o_auth2_client_links import OAuth2ClientLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2ClientLinks from a JSON string
o_auth2_client_links_instance = OAuth2ClientLinks.from_json(json)
# print the JSON string representation of the object
print(OAuth2ClientLinks.to_json())

# convert the object into a dict
o_auth2_client_links_dict = o_auth2_client_links_instance.to_dict()
# create an instance of OAuth2ClientLinks from a dict
o_auth2_client_links_from_dict = OAuth2ClientLinks.from_dict(o_auth2_client_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


