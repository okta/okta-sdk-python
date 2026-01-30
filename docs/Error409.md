# Error409

Conflict error object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_causes** | **List[str]** | Another request has already been received for the settings for this email template | [optional] [readonly] 
**error_code** | **str** | E0000254 | [optional] [readonly] 
**error_id** | **str** | sampleH3iLB6bpBcbnV9E09Fy | [optional] [readonly] 
**error_link** | **str** | E0000254 | [optional] [readonly] 
**error_summary** | **str** | Another request has already been received for the settings for this email template | [optional] [readonly] 

## Example

```python
from okta.models.error409 import Error409

# TODO update the JSON string below
json = "{}"
# create an instance of Error409 from a JSON string
error409_instance = Error409.from_json(json)
# print the JSON string representation of the object
print(Error409.to_json())

# convert the object into a dict
error409_dict = error409_instance.to_dict()
# create an instance of Error409 from a dict
error409_from_dict = Error409.from_dict(error409_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


