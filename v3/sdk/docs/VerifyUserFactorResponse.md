# VerifyUserFactorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** |  | [optional] [readonly] 
**factor_result** | [**VerifyUserFactorResult**](VerifyUserFactorResult.md) |  | [optional] 
**factor_result_message** | **str** |  | [optional] 
**embedded** | **Dict[str, object]** |  | [optional] [readonly] 
**links** | [**VerifyUserFactorResponseLinks**](VerifyUserFactorResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.verify_user_factor_response import VerifyUserFactorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyUserFactorResponse from a JSON string
verify_user_factor_response_instance = VerifyUserFactorResponse.from_json(json)
# print the JSON string representation of the object
print(VerifyUserFactorResponse.to_json())

# convert the object into a dict
verify_user_factor_response_dict = verify_user_factor_response_instance.to_dict()
# create an instance of VerifyUserFactorResponse from a dict
verify_user_factor_response_from_dict = VerifyUserFactorResponse.from_dict(verify_user_factor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


