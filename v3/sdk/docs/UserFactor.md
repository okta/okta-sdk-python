# UserFactor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] [readonly] 
**factor_type** | [**FactorType**](FactorType.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**profile** | **object** | Factor-specific attributes | [optional] 
**provider** | [**FactorProvider**](FactorProvider.md) |  | [optional] 
**status** | [**FactorStatus**](FactorStatus.md) |  | [optional] 
**verify** | [**VerifyFactorRequest**](VerifyFactorRequest.md) |  | [optional] 
**embedded** | **Dict[str, object]** |  | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.user_factor import UserFactor

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactor from a JSON string
user_factor_instance = UserFactor.from_json(json)
# print the JSON string representation of the object
print(UserFactor.to_json())

# convert the object into a dict
user_factor_dict = user_factor_instance.to_dict()
# create an instance of UserFactor from a dict
user_factor_from_dict = UserFactor.from_dict(user_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


