# UserRiskGetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risk_level** | [**UserRiskLevelAll**](UserRiskLevelAll.md) |  | [optional] 
**links** | [**UserRiskGetResponseLinks**](UserRiskGetResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.user_risk_get_response import UserRiskGetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserRiskGetResponse from a JSON string
user_risk_get_response_instance = UserRiskGetResponse.from_json(json)
# print the JSON string representation of the object
print(UserRiskGetResponse.to_json())

# convert the object into a dict
user_risk_get_response_dict = user_risk_get_response_instance.to_dict()
# create an instance of UserRiskGetResponse from a dict
user_risk_get_response_from_dict = UserRiskGetResponse.from_dict(user_risk_get_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


