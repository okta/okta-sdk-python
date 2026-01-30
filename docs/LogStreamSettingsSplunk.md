# LogStreamSettingsSplunk

Specifies the configuration for the `splunk_cloud_logstreaming` log stream type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edition** | [**SplunkEdition**](SplunkEdition.md) |  | 
**host** | **str** | The domain name for your Splunk Cloud instance. Don&#39;t include &#x60;http&#x60; or &#x60;https&#x60; in the string. For example: &#x60;acme.splunkcloud.com&#x60; | 
**token** | **str** | The HEC token for your Splunk Cloud HTTP Event Collector. The token value is set at object creation, but isn&#39;t returned. | 

## Example

```python
from okta.models.log_stream_settings_splunk import LogStreamSettingsSplunk

# TODO update the JSON string below
json = "{}"
# create an instance of LogStreamSettingsSplunk from a JSON string
log_stream_settings_splunk_instance = LogStreamSettingsSplunk.from_json(json)
# print the JSON string representation of the object
print(LogStreamSettingsSplunk.to_json())

# convert the object into a dict
log_stream_settings_splunk_dict = log_stream_settings_splunk_instance.to_dict()
# create an instance of LogStreamSettingsSplunk from a dict
log_stream_settings_splunk_from_dict = LogStreamSettingsSplunk.from_dict(log_stream_settings_splunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


