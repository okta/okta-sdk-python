# FailbackRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** | List of Okta domains to failback | [optional] 

## Example

```python
from okta.models.failback_request_schema import FailbackRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FailbackRequestSchema from a JSON string
failback_request_schema_instance = FailbackRequestSchema.from_json(json)
# print the JSON string representation of the object
print(FailbackRequestSchema.to_json())

# convert the object into a dict
failback_request_schema_dict = failback_request_schema_instance.to_dict()
# create an instance of FailbackRequestSchema from a dict
failback_request_schema_from_dict = FailbackRequestSchema.from_dict(failback_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


