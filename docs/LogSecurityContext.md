# LogSecurityContext

The `securityContext` object provides security information that is directly related to the evaluation of the event's IP reputation. IP reputation is a trustworthiness rating that evaluates how likely a sender is to be malicious and is based on the sender's IP address. As the name implies, the `securityContext` object is useful for security applications-flagging and inspecting suspicious events.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_number** | **int** | The [Autonomous system](https://docs.telemetry.mozilla.org/datasets/other/asn_aggregates/reference) number that&#39;s associated with the autonomous system the event request was sourced to | [optional] [readonly] 
**as_org** | **str** | The organization that is associated with the autonomous system that the event request is sourced to | [optional] [readonly] 
**domain** | **str** | The domain name that&#39;s associated with the IP address of the inbound event request | [optional] [readonly] 
**isp** | **str** | The Internet service provider that&#39;s used to send the event&#39;s request | [optional] [readonly] 
**is_proxy** | **bool** | Specifies whether an event&#39;s request is from a known proxy | [optional] [readonly] 
**user_behaviors** | **List[str]** | The result of the user behavior detection models associated with the event | [optional] [readonly] 

## Example

```python
from okta.models.log_security_context import LogSecurityContext

# TODO update the JSON string below
json = "{}"
# create an instance of LogSecurityContext from a JSON string
log_security_context_instance = LogSecurityContext.from_json(json)
# print the JSON string representation of the object
print(LogSecurityContext.to_json())

# convert the object into a dict
log_security_context_dict = log_security_context_instance.to_dict()
# create an instance of LogSecurityContext from a dict
log_security_context_from_dict = LogSecurityContext.from_dict(log_security_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


