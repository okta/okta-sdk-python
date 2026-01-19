# UserFactorVerifyResponseWaiting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** | Timestamp when the verification expires | [optional] [readonly] 
**factor_message** | **str** | Optional display message for factor verification | [optional] [readonly] 
**factor_result** | [**UserFactorVerifyResultWaiting**](UserFactorVerifyResultWaiting.md) |  | [optional] 
**profile** | **Dict[str, object]** |  | [optional] [readonly] 
**embedded** | [**UserFactorVerifyResponseWaitingEmbedded**](UserFactorVerifyResponseWaitingEmbedded.md) |  | [optional] 
**links** | [**UserFactorLinks**](UserFactorLinks.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_verify_response_waiting import UserFactorVerifyResponseWaiting

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorVerifyResponseWaiting from a JSON string
user_factor_verify_response_waiting_instance = UserFactorVerifyResponseWaiting.from_json(json)
# print the JSON string representation of the object
print(UserFactorVerifyResponseWaiting.to_json())

# convert the object into a dict
user_factor_verify_response_waiting_dict = user_factor_verify_response_waiting_instance.to_dict()
# create an instance of UserFactorVerifyResponseWaiting from a dict
user_factor_verify_response_waiting_from_dict = UserFactorVerifyResponseWaiting.from_dict(user_factor_verify_response_waiting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


