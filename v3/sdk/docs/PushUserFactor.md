# PushUserFactor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** |  | [optional] 
**factor_result** | [**FactorResultType**](FactorResultType.md) |  | [optional] 
**profile** | [**PushUserFactorProfile**](PushUserFactorProfile.md) |  | [optional] 

## Example

```python
from openapi_client.models.push_user_factor import PushUserFactor

# TODO update the JSON string below
json = "{}"
# create an instance of PushUserFactor from a JSON string
push_user_factor_instance = PushUserFactor.from_json(json)
# print the JSON string representation of the object
print(PushUserFactor.to_json())

# convert the object into a dict
push_user_factor_dict = push_user_factor_instance.to_dict()
# create an instance of PushUserFactor from a dict
push_user_factor_form_dict = push_user_factor.from_dict(push_user_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


