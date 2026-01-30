# UserFactorActivatePush

Activation requests have a short lifetime and expire if the activation isn't completed before the indicated timestamp. If the activation expires, use the returned `activate` link to restart the process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** | Timestamp when the factor verification attempt expires | [optional] [readonly] 
**factor_result** | [**UserFactorActivatePushResult**](UserFactorActivatePushResult.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_activate_push import UserFactorActivatePush

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorActivatePush from a JSON string
user_factor_activate_push_instance = UserFactorActivatePush.from_json(json)
# print the JSON string representation of the object
print(UserFactorActivatePush.to_json())

# convert the object into a dict
user_factor_activate_push_dict = user_factor_activate_push_instance.to_dict()
# create an instance of UserFactorActivatePush from a dict
user_factor_activate_push_from_dict = UserFactorActivatePush.from_dict(user_factor_activate_push_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


