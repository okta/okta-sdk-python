# UserFactorCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UserFactorCallProfile**](UserFactorCallProfile.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_call import UserFactorCall

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorCall from a JSON string
user_factor_call_instance = UserFactorCall.from_json(json)
# print the JSON string representation of the object
print(UserFactorCall.to_json())

# convert the object into a dict
user_factor_call_dict = user_factor_call_instance.to_dict()
# create an instance of UserFactorCall from a dict
user_factor_call_from_dict = UserFactorCall.from_dict(user_factor_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


