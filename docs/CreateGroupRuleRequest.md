# CreateGroupRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**GroupRuleAction**](GroupRuleAction.md) |  | [optional] 
**conditions** | [**GroupRuleConditions**](GroupRuleConditions.md) |  | [optional] 
**name** | **str** | Name of the group rule | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from okta.models.create_group_rule_request import CreateGroupRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupRuleRequest from a JSON string
create_group_rule_request_instance = CreateGroupRuleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateGroupRuleRequest.to_json())

# convert the object into a dict
create_group_rule_request_dict = create_group_rule_request_instance.to_dict()
# create an instance of CreateGroupRuleRequest from a dict
create_group_rule_request_from_dict = CreateGroupRuleRequest.from_dict(create_group_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


