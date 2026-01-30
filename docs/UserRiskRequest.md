# UserRiskRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risk_level** | **str** | The risk level associated with the user | [optional] 

## Example

```python
from okta.models.user_risk_request import UserRiskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserRiskRequest from a JSON string
user_risk_request_instance = UserRiskRequest.from_json(json)
# print the JSON string representation of the object
print(UserRiskRequest.to_json())

# convert the object into a dict
user_risk_request_dict = user_risk_request_instance.to_dict()
# create an instance of UserRiskRequest from a dict
user_risk_request_from_dict = UserRiskRequest.from_dict(user_risk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


