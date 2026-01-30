# UserRiskPutResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Describes the risk level for the user | [optional] 
**risk_level** | [**UserRiskLevelPut**](UserRiskLevelPut.md) |  | [optional] 
**links** | [**UserRiskGetResponseLinks**](UserRiskGetResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.user_risk_put_response import UserRiskPutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserRiskPutResponse from a JSON string
user_risk_put_response_instance = UserRiskPutResponse.from_json(json)
# print the JSON string representation of the object
print(UserRiskPutResponse.to_json())

# convert the object into a dict
user_risk_put_response_dict = user_risk_put_response_instance.to_dict()
# create an instance of UserRiskPutResponse from a dict
user_risk_put_response_from_dict = UserRiskPutResponse.from_dict(user_risk_put_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


