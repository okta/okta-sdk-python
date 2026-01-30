# LogUserAgent

\"A user agent is software (a software agent) that is acting on behalf of a user.\" ([Definition of User Agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent))  In the Okta event data object, the `UserAgent` object provides specifications about the client software that makes event-triggering HTTP requests. User agent identification is often useful for identifying interoperability problems between servers and clients, and also for browser and operating system usage analytics. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**browser** | **str** | If the client is a web browser, this field identifies the type of web browser (for example, CHROME, FIREFOX) | [optional] [readonly] 
**os** | **str** | The operating system that the client runs on (for example, Windows 10) | [optional] [readonly] 
**raw_user_agent** | **str** | A raw string representation of the user agent that is formatted according to [section 5.5.3 of HTTP/1.1 Semantics and Content](https://datatracker.ietf.org/doc/html/rfc7231#section-5.5.3). Both the &#x60;browser&#x60; and the &#x60;OS&#x60; fields can be derived from this field. | [optional] [readonly] 

## Example

```python
from okta.models.log_user_agent import LogUserAgent

# TODO update the JSON string below
json = "{}"
# create an instance of LogUserAgent from a JSON string
log_user_agent_instance = LogUserAgent.from_json(json)
# print the JSON string representation of the object
print(LogUserAgent.to_json())

# convert the object into a dict
log_user_agent_dict = log_user_agent_instance.to_dict()
# create an instance of LogUserAgent from a dict
log_user_agent_from_dict = LogUserAgent.from_dict(log_user_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


