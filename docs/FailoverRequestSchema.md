# FailoverRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** | List of Okta domains to failover | [optional] 

## Example

```python
from okta.models.failover_request_schema import FailoverRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FailoverRequestSchema from a JSON string
failover_request_schema_instance = FailoverRequestSchema.from_json(json)
# print the JSON string representation of the object
print(FailoverRequestSchema.to_json())

# convert the object into a dict
failover_request_schema_dict = failover_request_schema_instance.to_dict()
# create an instance of FailoverRequestSchema from a dict
failover_request_schema_from_dict = FailoverRequestSchema.from_dict(failover_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


