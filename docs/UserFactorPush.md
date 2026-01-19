# UserFactorPush


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UserFactorPushProfile**](UserFactorPushProfile.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_push import UserFactorPush

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorPush from a JSON string
user_factor_push_instance = UserFactorPush.from_json(json)
# print the JSON string representation of the object
print(UserFactorPush.to_json())

# convert the object into a dict
user_factor_push_dict = user_factor_push_instance.to_dict()
# create an instance of UserFactorPush from a dict
user_factor_push_from_dict = UserFactorPush.from_dict(user_factor_push_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


