# UserGetSingletonAllOfEmbedded

The embedded resources related to the object if the `expand` query parameter is specified

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocks** | [**List[UserBlock]**](UserBlock.md) | A list of access block details for the user account | [optional] 

## Example

```python
from okta.models.user_get_singleton_all_of_embedded import UserGetSingletonAllOfEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of UserGetSingletonAllOfEmbedded from a JSON string
user_get_singleton_all_of_embedded_instance = UserGetSingletonAllOfEmbedded.from_json(json)
# print the JSON string representation of the object
print(UserGetSingletonAllOfEmbedded.to_json())

# convert the object into a dict
user_get_singleton_all_of_embedded_dict = user_get_singleton_all_of_embedded_instance.to_dict()
# create an instance of UserGetSingletonAllOfEmbedded from a dict
user_get_singleton_all_of_embedded_from_dict = UserGetSingletonAllOfEmbedded.from_dict(user_get_singleton_all_of_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


