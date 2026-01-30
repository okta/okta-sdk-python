# InterclientTrustMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_instance_id** | **str** | The app ID of the target app | [optional] [readonly] 
**created** | **str** | Timestamp when the interclient trust mapping was created | [optional] [readonly] 
**id** | **str** | The unique ID of the interclient trust mapping | [optional] [readonly] 
**last_updated** | **str** | Timestamp when the interclient trust mapping was updated | [optional] [readonly] 
**last_updated_by** | **str** | ID of the user who created the interclient trust mapping | [optional] [readonly] 
**org_id** | **str** | ID of the org | [optional] [readonly] 
**trusted_app_instance_id** | **str** | The app ID of the allowed app | [optional] [readonly] 

## Example

```python
from okta.models.interclient_trust_mapping import InterclientTrustMapping

# TODO update the JSON string below
json = "{}"
# create an instance of InterclientTrustMapping from a JSON string
interclient_trust_mapping_instance = InterclientTrustMapping.from_json(json)
# print the JSON string representation of the object
print(InterclientTrustMapping.to_json())

# convert the object into a dict
interclient_trust_mapping_dict = interclient_trust_mapping_instance.to_dict()
# create an instance of InterclientTrustMapping from a dict
interclient_trust_mapping_from_dict = InterclientTrustMapping.from_dict(interclient_trust_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


