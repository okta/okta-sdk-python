# SecurityEventTokenError

Error object thrown when parsing the Security Event Token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Describes the error &gt; **Note:** SET claim fields with underscores (snake case) are presented in camelcase. For example, &#x60;previous_status&#x60; appears as &#x60;previousStatus&#x60;.  | [optional] 
**err** | **str** | A code that describes the category of the error | [optional] 

## Example

```python
from okta.models.security_event_token_error import SecurityEventTokenError

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEventTokenError from a JSON string
security_event_token_error_instance = SecurityEventTokenError.from_json(json)
# print the JSON string representation of the object
print(SecurityEventTokenError.to_json())

# convert the object into a dict
security_event_token_error_dict = security_event_token_error_instance.to_dict()
# create an instance of SecurityEventTokenError from a dict
security_event_token_error_from_dict = SecurityEventTokenError.from_dict(security_event_token_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


