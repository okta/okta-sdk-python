# UserFactorVerifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** | Timestamp when the verification expires | [optional] [readonly] 
**factor_message** | **str** | Optional display message for factor verification | [optional] [readonly] 
**factor_result** | [**UserFactorVerifyResult**](UserFactorVerifyResult.md) |  | [optional] 
**profile** | **Dict[str, object]** |  | [optional] [readonly] 
**embedded** | **Dict[str, Optional[object]]** |  | [optional] 
**links** | [**UserFactorLinks**](UserFactorLinks.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_verify_response import UserFactorVerifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorVerifyResponse from a JSON string
user_factor_verify_response_instance = UserFactorVerifyResponse.from_json(json)
# print the JSON string representation of the object
print(UserFactorVerifyResponse.to_json())

# convert the object into a dict
user_factor_verify_response_dict = user_factor_verify_response_instance.to_dict()
# create an instance of UserFactorVerifyResponse from a dict
user_factor_verify_response_from_dict = UserFactorVerifyResponse.from_dict(user_factor_verify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


