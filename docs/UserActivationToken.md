# UserActivationToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_token** | **str** | Token received as part of an activation user request. If a password was set before the user was activated, then user must sign in with their password or the &#x60;activationToken&#x60; and not the activation link. More information about using the &#x60;activationToken&#x60; to login can be found in the [Authentication API](https://developer.okta.com/docs/reference/api/authn/#primary-authentication-with-activation-token). | [optional] [readonly] 
**activation_url** | **str** | If &#x60;sendEmail&#x60; is &#x60;false&#x60;, returns an activation link for the user to set up their account. The activation token can be used to create a custom activation link. | [optional] [readonly] 

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


