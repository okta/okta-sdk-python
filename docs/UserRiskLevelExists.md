# UserRiskLevelExists


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Describes the risk level for the user | [optional] 

## Example

```python
from okta.models.user_risk_level_exists import UserRiskLevelExists

# TODO update the JSON string below
json = "{}"
# create an instance of UserRiskLevelExists from a JSON string
user_risk_level_exists_instance = UserRiskLevelExists.from_json(json)
# print the JSON string representation of the object
print(UserRiskLevelExists.to_json())

# convert the object into a dict
user_risk_level_exists_dict = user_risk_level_exists_instance.to_dict()
# create an instance of UserRiskLevelExists from a dict
user_risk_level_exists_from_dict = UserRiskLevelExists.from_dict(user_risk_level_exists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


