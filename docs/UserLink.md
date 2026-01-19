# UserLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**HrefObjectUserLink**](HrefObjectUserLink.md) |  | [optional] 

## Example

```python
from okta.models.user_link import UserLink

# TODO update the JSON string below
json = "{}"
# create an instance of UserLink from a JSON string
user_link_instance = UserLink.from_json(json)
# print the JSON string representation of the object
print(UserLink.to_json())

# convert the object into a dict
user_link_dict = user_link_instance.to_dict()
# create an instance of UserLink from a dict
user_link_from_dict = UserLink.from_dict(user_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


