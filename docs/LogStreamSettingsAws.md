# LogStreamSettingsAws

Specifies the configuration for the `aws_eventbridge` Log Stream type. This configuration can't be modified after creation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | Your AWS account ID | 
**event_source_name** | **str** | An alphanumeric name (no spaces) to identify this event source in AWS EventBridge | 
**region** | [**AwsRegion**](AwsRegion.md) |  | 

## Example

```python
from okta.models.log_stream_settings_aws import LogStreamSettingsAws

# TODO update the JSON string below
json = "{}"
# create an instance of LogStreamSettingsAws from a JSON string
log_stream_settings_aws_instance = LogStreamSettingsAws.from_json(json)
# print the JSON string representation of the object
print(LogStreamSettingsAws.to_json())

# convert the object into a dict
log_stream_settings_aws_dict = log_stream_settings_aws_instance.to_dict()
# create an instance of LogStreamSettingsAws from a dict
log_stream_settings_aws_from_dict = LogStreamSettingsAws.from_dict(log_stream_settings_aws_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


