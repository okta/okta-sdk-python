# LinksAuthenticatorAuthenticator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**HrefHints**](HrefHints.md) |  | [optional] 
**href** | **str** | Link URI | 
**name** | **str** | Link name | [optional] [readonly] 
**templated** | **bool** | Indicates whether the link object&#39;s &#x60;href&#x60; property is a URI template. | [optional] [readonly] 
**type** | **str** | The media type of the link. If omitted, it is implicitly &#x60;application/json&#x60;. | [optional] [readonly] 

## Example

```python
from okta.models.links_authenticator_authenticator import LinksAuthenticatorAuthenticator

# TODO update the JSON string below
json = "{}"
# create an instance of LinksAuthenticatorAuthenticator from a JSON string
links_authenticator_authenticator_instance = LinksAuthenticatorAuthenticator.from_json(json)
# print the JSON string representation of the object
print(LinksAuthenticatorAuthenticator.to_json())

# convert the object into a dict
links_authenticator_authenticator_dict = links_authenticator_authenticator_instance.to_dict()
# create an instance of LinksAuthenticatorAuthenticator from a dict
links_authenticator_authenticator_from_dict = LinksAuthenticatorAuthenticator.from_dict(links_authenticator_authenticator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


