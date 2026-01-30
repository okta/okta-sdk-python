# LinksUserAuthenticators


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**LinksUserAuthenticatorsUser**](LinksUserAuthenticatorsUser.md) |  | [optional] 

## Example

```python
from okta.models.links_user_authenticators import LinksUserAuthenticators

# TODO update the JSON string below
json = "{}"
# create an instance of LinksUserAuthenticators from a JSON string
links_user_authenticators_instance = LinksUserAuthenticators.from_json(json)
# print the JSON string representation of the object
print(LinksUserAuthenticators.to_json())

# convert the object into a dict
links_user_authenticators_dict = links_user_authenticators_instance.to_dict()
# create an instance of LinksUserAuthenticators from a dict
links_user_authenticators_from_dict = LinksUserAuthenticators.from_dict(links_user_authenticators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


