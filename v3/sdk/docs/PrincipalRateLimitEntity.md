# PrincipalRateLimitEntity



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] [readonly] 
**created_date** | **datetime** |  | [optional] [readonly] 
**default_concurrency_percentage** | **int** |  | [optional] [readonly] 
**default_percentage** | **int** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**last_update** | **datetime** |  | [optional] [readonly] 
**last_updated_by** | **str** |  | [optional] [readonly] 
**org_id** | **str** |  | [optional] [readonly] 
**principal_id** | **str** |  | 
**principal_type** | [**PrincipalType**](PrincipalType.md) |  | 

## Example

```python
from okta.models.principal_rate_limit_entity import PrincipalRateLimitEntity

# TODO update the JSON string below
json = "{}"
# create an instance of PrincipalRateLimitEntity from a JSON string
principal_rate_limit_entity_instance = PrincipalRateLimitEntity.from_json(json)
# print the JSON string representation of the object
print(PrincipalRateLimitEntity.to_json())

# convert the object into a dict
principal_rate_limit_entity_dict = principal_rate_limit_entity_instance.to_dict()
# create an instance of PrincipalRateLimitEntity from a dict
principal_rate_limit_entity_from_dict = PrincipalRateLimitEntity.from_dict(principal_rate_limit_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


