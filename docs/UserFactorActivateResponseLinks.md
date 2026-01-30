# UserFactorActivateResponseLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**user** | [**LinksUserFactorsUser**](LinksUserFactorsUser.md) |  | [optional] 
**verify** | [**LinksVerifyVerify**](LinksVerifyVerify.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_activate_response_links import UserFactorActivateResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorActivateResponseLinks from a JSON string
user_factor_activate_response_links_instance = UserFactorActivateResponseLinks.from_json(json)
# print the JSON string representation of the object
print(UserFactorActivateResponseLinks.to_json())

# convert the object into a dict
user_factor_activate_response_links_dict = user_factor_activate_response_links_instance.to_dict()
# create an instance of UserFactorActivateResponseLinks from a dict
user_factor_activate_response_links_from_dict = UserFactorActivateResponseLinks.from_dict(user_factor_activate_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


