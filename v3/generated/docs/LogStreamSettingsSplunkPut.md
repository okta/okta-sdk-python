# LogStreamSettingsSplunkPut

Specifies the configuration for the `splunk_cloud_logstreaming` Log Stream type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edition** | [**SplunkEdition**](SplunkEdition.md) |  | 
**host** | **str** | The domain name for your Splunk Cloud instance. Don&#39;t include &#x60;http&#x60; or &#x60;https&#x60; in the string. For example: &#x60;acme.splunkcloud.com&#x60; | 

## Example

```python
from openapi_client.models.log_stream_settings_splunk_put import LogStreamSettingsSplunkPut

# TODO update the JSON string below
json = "{}"
# create an instance of LogStreamSettingsSplunkPut from a JSON string
log_stream_settings_splunk_put_instance = LogStreamSettingsSplunkPut.from_json(json)
# print the JSON string representation of the object
print(LogStreamSettingsSplunkPut.to_json())

# convert the object into a dict
log_stream_settings_splunk_put_dict = log_stream_settings_splunk_put_instance.to_dict()
# create an instance of LogStreamSettingsSplunkPut from a dict
log_stream_settings_splunk_put_form_dict = log_stream_settings_splunk_put.from_dict(log_stream_settings_splunk_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


