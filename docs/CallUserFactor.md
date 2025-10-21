# CallUserFactor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**CallUserFactorProfile**](CallUserFactorProfile.md) |  | [optional] 

## Example

```python
from okta.models.call_user_factor import CallUserFactor

# TODO update the JSON string below
json = "{}"
# create an instance of CallUserFactor from a JSON string
call_user_factor_instance = CallUserFactor.from_json(json)
# print the JSON string representation of the object
print(CallUserFactor.to_json())

# convert the object into a dict
call_user_factor_dict = call_user_factor_instance.to_dict()
# create an instance of CallUserFactor from a dict
call_user_factor_from_dict = CallUserFactor.from_dict(call_user_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


