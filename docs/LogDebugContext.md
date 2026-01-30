# LogDebugContext

For some kinds of events (for example, OLM provisioning, sign-in request, second factor SMS, and so on), the fields that are provided in other response objects aren't sufficient to adequately describe the operations that the event has performed. In such cases, the `debugContext` object provides a way to store additional information.  For example, an event where a second factor SMS token is sent to a user may have a `debugContext` that looks like the following: ``` {     \"debugData\": {         \"requestUri\": \"/api/v1/users/00u3gjksoiRGRAZHLSYV/factors/smsf8luacpZJAva10x45/verify\",         \"smsProvider\": \"TELESIGN\",         \"transactionId\": \"268632458E3C100F5F5F594C6DC689D4\"     } } ``` By inspecting the debugData field, you can find the URI that is used to trigger the second factor SMS (`/api/v1/users/00u3gjksoiRGRAZHLSYV/factors/smsf8luacpZJAva10x45/verify`), the SMS provider (`TELESIGN`), and the ID used by Telesign to identify this transaction (`268632458E3C100F5F5F594C6DC689D4`).  If for some reason the information that is needed to implement a feature isn't provided in other response objects, you should scan the `debugContext.debugData` field for potentially useful fields. > **Important:** The information contained in `debugContext.debugData` is intended to add context when troubleshooting customer platform issues. Both key names and values may change from release to release and aren't guaranteed to be stable. Therefore, they shouldn't be viewed as a data contract but as a debugging aid instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debug_data** | **Dict[str, object]** | A dynamic field that contains miscellaneous information that is dependent on the event type. | [optional] [readonly] 

## Example

```python
from okta.models.log_debug_context import LogDebugContext

# TODO update the JSON string below
json = "{}"
# create an instance of LogDebugContext from a JSON string
log_debug_context_instance = LogDebugContext.from_json(json)
# print the JSON string representation of the object
print(LogDebugContext.to_json())

# convert the object into a dict
log_debug_context_dict = log_debug_context_instance.to_dict()
# create an instance of LogDebugContext from a dict
log_debug_context_from_dict = LogDebugContext.from_dict(log_debug_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


