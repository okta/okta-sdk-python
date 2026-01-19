# UserFactorActivateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor_type** | **str** | Type of the factor | [optional] 
**links** | [**UserFactorActivateResponseLinks**](UserFactorActivateResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_activate_response import UserFactorActivateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorActivateResponse from a JSON string
user_factor_activate_response_instance = UserFactorActivateResponse.from_json(json)
# print the JSON string representation of the object
print(UserFactorActivateResponse.to_json())

# convert the object into a dict
user_factor_activate_response_dict = user_factor_activate_response_instance.to_dict()
# create an instance of UserFactorActivateResponse from a dict
user_factor_activate_response_from_dict = UserFactorActivateResponse.from_dict(user_factor_activate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


