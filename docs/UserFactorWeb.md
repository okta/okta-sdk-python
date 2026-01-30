# UserFactorWeb


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UserFactorWebProfile**](UserFactorWebProfile.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_web import UserFactorWeb

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorWeb from a JSON string
user_factor_web_instance = UserFactorWeb.from_json(json)
# print the JSON string representation of the object
print(UserFactorWeb.to_json())

# convert the object into a dict
user_factor_web_dict = user_factor_web_instance.to_dict()
# create an instance of UserFactorWeb from a dict
user_factor_web_from_dict = UserFactorWeb.from_dict(user_factor_web_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


