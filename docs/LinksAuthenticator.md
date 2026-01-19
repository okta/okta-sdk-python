# LinksAuthenticator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticator** | [**LinksAuthenticatorAuthenticator**](LinksAuthenticatorAuthenticator.md) |  | [optional] 

## Example

```python
from okta.models.links_authenticator import LinksAuthenticator

# TODO update the JSON string below
json = "{}"
# create an instance of LinksAuthenticator from a JSON string
links_authenticator_instance = LinksAuthenticator.from_json(json)
# print the JSON string representation of the object
print(LinksAuthenticator.to_json())

# convert the object into a dict
links_authenticator_dict = links_authenticator_instance.to_dict()
# create an instance of LinksAuthenticator from a dict
links_authenticator_from_dict = LinksAuthenticator.from_dict(links_authenticator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


