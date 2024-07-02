# Session


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amr** | [**List[SessionAuthenticationMethod]**](SessionAuthenticationMethod.md) | Authentication method reference | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**expires_at** | **datetime** | A timestamp when the Session expires | [optional] [readonly] 
**id** | **str** | A unique key for the Session | [optional] [readonly] 
**idp** | [**SessionIdentityProvider**](SessionIdentityProvider.md) |  | [optional] 
**last_factor_verification** | **datetime** | A timestamp when the user last performed multifactor authentication | [optional] [readonly] 
**last_password_verification** | **datetime** | A timestamp when the user last performed the primary or step-up authentication with a password | [optional] [readonly] 
**login** | **str** | A unique identifier for the user (username) | [optional] [readonly] 
**status** | [**SessionStatus**](SessionStatus.md) |  | [optional] 
**user_id** | **str** | A unique key for the user | [optional] [readonly] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.session import Session

# TODO update the JSON string below
json = "{}"
# create an instance of Session from a JSON string
session_instance = Session.from_json(json)
# print the JSON string representation of the object
print(Session.to_json())

# convert the object into a dict
session_dict = session_instance.to_dict()
# create an instance of Session from a dict
session_from_dict = Session.from_dict(session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


