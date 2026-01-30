# BaseContextSession

Details of the user session

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the user&#39;s session | [optional] 
**user_id** | **str** | The unique identifier for the user | [optional] 
**login** | **str** | The username used to identify the user. This is often the user&#39;s email address. | [optional] 
**created_at** | **datetime** | Timestamp of when the session was created | [optional] 
**expires_at** | **datetime** | Timestamp of when the session expires | [optional] 
**status** | **str** | Represents the current status of the user&#39;s session | [optional] 
**last_password_verification** | **datetime** | Timestamp of when the user was last authenticated | [optional] 
**amr** | **List[str]** | The authentication method reference | [optional] 
**idp** | [**SessionIdentityProvider**](SessionIdentityProvider.md) |  | [optional] 
**mfa_active** | **bool** | Describes whether multifactor authentication was enabled | [optional] 

## Example

```python
from okta.models.base_context_session import BaseContextSession

# TODO update the JSON string below
json = "{}"
# create an instance of BaseContextSession from a JSON string
base_context_session_instance = BaseContextSession.from_json(json)
# print the JSON string representation of the object
print(BaseContextSession.to_json())

# convert the object into a dict
base_context_session_dict = base_context_session_instance.to_dict()
# create an instance of BaseContextSession from a dict
base_context_session_from_dict = BaseContextSession.from_dict(base_context_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


