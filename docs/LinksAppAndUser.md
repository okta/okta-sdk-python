# LinksAppAndUser

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available using the [JSON Hypertext Application Language](https://datatracker.ietf.org/doc/html/draft-kelly-json-hal-06) specification. This object is used for dynamic discovery of resources related to the App User.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**HrefObjectAppLink**](HrefObjectAppLink.md) |  | [optional] 
**user** | [**HrefObjectUserLink**](HrefObjectUserLink.md) |  | [optional] 

## Example

```python
from okta.models.links_app_and_user import LinksAppAndUser

# TODO update the JSON string below
json = "{}"
# create an instance of LinksAppAndUser from a JSON string
links_app_and_user_instance = LinksAppAndUser.from_json(json)
# print the JSON string representation of the object
print(LinksAppAndUser.to_json())

# convert the object into a dict
links_app_and_user_dict = links_app_and_user_instance.to_dict()
# create an instance of LinksAppAndUser from a dict
links_app_and_user_from_dict = LinksAppAndUser.from_dict(links_app_and_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


