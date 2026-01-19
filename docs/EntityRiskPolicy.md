# EntityRiskPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | **str** | Policy conditions aren&#39;t supported for this policy type. | [optional] 

## Example

```python
from okta.models.entity_risk_policy import EntityRiskPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of EntityRiskPolicy from a JSON string
entity_risk_policy_instance = EntityRiskPolicy.from_json(json)
# print the JSON string representation of the object
print(EntityRiskPolicy.to_json())

# convert the object into a dict
entity_risk_policy_dict = entity_risk_policy_instance.to_dict()
# create an instance of EntityRiskPolicy from a dict
entity_risk_policy_from_dict = EntityRiskPolicy.from_dict(entity_risk_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


