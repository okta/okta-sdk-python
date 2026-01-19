# EventHookChannelConfigAuthScheme

The authentication scheme used for this request.  To use Basic Auth for authentication, set `type` to `HEADER`, `key` to `Authorization`, and `value` to the Base64-encoded string of \"username:password\". Ensure that you include the scheme (including space) as part of the `value` parameter. For example, `Basic YWRtaW46c3VwZXJzZWNyZXQ=`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The name for the authorization header | [optional] 
**type** | [**EventHookChannelConfigAuthSchemeType**](EventHookChannelConfigAuthSchemeType.md) |  | [optional] 
**value** | **str** | The header value. This secret key is passed to your external service endpoint for security verification. This property is not returned in the response. | [optional] 

## Example

```python
from okta.models.event_hook_channel_config_auth_scheme import EventHookChannelConfigAuthScheme

# TODO update the JSON string below
json = "{}"
# create an instance of EventHookChannelConfigAuthScheme from a JSON string
event_hook_channel_config_auth_scheme_instance = EventHookChannelConfigAuthScheme.from_json(json)
# print the JSON string representation of the object
print(EventHookChannelConfigAuthScheme.to_json())

# convert the object into a dict
event_hook_channel_config_auth_scheme_dict = event_hook_channel_config_auth_scheme_instance.to_dict()
# create an instance of EventHookChannelConfigAuthScheme from a dict
event_hook_channel_config_auth_scheme_from_dict = EventHookChannelConfigAuthScheme.from_dict(event_hook_channel_config_auth_scheme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


