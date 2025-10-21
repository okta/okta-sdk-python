# LogStreamAws


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**LogStreamSettingsAws**](LogStreamSettingsAws.md) |  | 

## Example

```python
from okta.models.log_stream_aws import LogStreamAws

# TODO update the JSON string below
json = "{}"
# create an instance of LogStreamAws from a JSON string
log_stream_aws_instance = LogStreamAws.from_json(json)
# print the JSON string representation of the object
print(LogStreamAws.to_json())

# convert the object into a dict
log_stream_aws_dict = log_stream_aws_instance.to_dict()
# create an instance of LogStreamAws from a dict
log_stream_aws_from_dict = LogStreamAws.from_dict(log_stream_aws_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


