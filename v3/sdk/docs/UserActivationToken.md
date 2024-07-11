# UserActivationToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_token** | **str** |  | [optional] [readonly] 
**activation_url** | **str** |  | [optional] [readonly] 

## Example

```python
from okta.models.user_activation_token import UserActivationToken

# TODO update the JSON string below
json = "{}"
# create an instance of UserActivationToken from a JSON string
user_activation_token_instance = UserActivationToken.from_json(json)
# print the JSON string representation of the object
print(UserActivationToken.to_json())

# convert the object into a dict
user_activation_token_dict = user_activation_token_instance.to_dict()
# create an instance of UserActivationToken from a dict
user_activation_token_from_dict = UserActivationToken.from_dict(user_activation_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


