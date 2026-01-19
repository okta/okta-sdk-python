# UserFactorU2F


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UserFactorU2FProfile**](UserFactorU2FProfile.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_u2_f import UserFactorU2F

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorU2F from a JSON string
user_factor_u2_f_instance = UserFactorU2F.from_json(json)
# print the JSON string representation of the object
print(UserFactorU2F.to_json())

# convert the object into a dict
user_factor_u2_f_dict = user_factor_u2_f_instance.to_dict()
# create an instance of UserFactorU2F from a dict
user_factor_u2_f_from_dict = UserFactorU2F.from_dict(user_factor_u2_f_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


