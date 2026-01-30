# UserFactorSupported


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollment** | **str** | Indicates if the factor is required for the specified user | [optional] 
**factor_type** | [**UserFactorType**](UserFactorType.md) |  | [optional] 
**provider** | [**UserFactorProvider**](UserFactorProvider.md) |  | [optional] 
**status** | [**UserFactorStatus**](UserFactorStatus.md) |  | [optional] 
**vendor_name** | **str** | Name of the factor vendor. This is usually the same as the provider except for On-Prem MFA, which depends on admin settings. | [optional] [readonly] 
**embedded** | **Dict[str, object]** | Embedded resources related to the factor | [optional] [readonly] 
**links** | [**UserFactorLinks**](UserFactorLinks.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_supported import UserFactorSupported

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorSupported from a JSON string
user_factor_supported_instance = UserFactorSupported.from_json(json)
# print the JSON string representation of the object
print(UserFactorSupported.to_json())

# convert the object into a dict
user_factor_supported_dict = user_factor_supported_instance.to_dict()
# create an instance of UserFactorSupported from a dict
user_factor_supported_from_dict = UserFactorSupported.from_dict(user_factor_supported_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


