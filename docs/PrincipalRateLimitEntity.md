# PrincipalRateLimitEntity



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | The Okta user ID of the user who created the principle rate limit entity | [optional] [readonly] 
**created_date** | **datetime** | The date and time the principle rate limit entity was created | [optional] [readonly] 
**default_concurrency_percentage** | **int** | The default percentage of a given concurrency limit threshold that the owning principal can consume | [optional] 
**default_percentage** | **int** | The default percentage of a given rate limit threshold that the owning principal can consume | [optional] 
**id** | **str** | The unique identifier of the principle rate limit entity | [optional] [readonly] 
**last_update** | **datetime** | The date and time the principle rate limit entity was last updated | [optional] [readonly] 
**last_updated_by** | **str** | The Okta user ID of the user who last updated the principle rate limit entity | [optional] [readonly] 
**org_id** | **str** | The unique identifier of the Okta org | [optional] [readonly] 
**principal_id** | **str** | The unique identifier of the principal. This is the ID of the API token or OAuth 2.0 app. | 
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


