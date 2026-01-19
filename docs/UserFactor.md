# UserFactor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | Timestamp when the factor was enrolled | [optional] [readonly] 
**factor_type** | [**UserFactorType**](UserFactorType.md) |  | [optional] 
**id** | **str** | ID of the factor | [optional] [readonly] 
**last_updated** | **datetime** | Timestamp when the factor was last updated | [optional] [readonly] 
**profile** | **object** | Specific attributes related to the factor | [optional] 
**provider** | **str** | Provider for the factor. Each provider can support a subset of factor types. | [optional] 
**status** | [**UserFactorStatus**](UserFactorStatus.md) |  | [optional] 
**vendor_name** | **str** | Name of the factor vendor. This is usually the same as the provider except for On-Prem MFA, which depends on admin settings. | [optional] [readonly] 
**embedded** | **Dict[str, object]** |  | [optional] [readonly] 
**links** | [**UserFactorLinks**](UserFactorLinks.md) |  | [optional] 

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


