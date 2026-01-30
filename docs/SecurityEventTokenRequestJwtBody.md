# SecurityEventTokenRequestJwtBody

JSON Web Token body payload for a Security Event Token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aud** | **str** | Audience | 
**events** | [**SecurityEventTokenRequestJwtEvents**](SecurityEventTokenRequestJwtEvents.md) |  | 
**iat** | **int** | Token issue time (UNIX timestamp) | 
**iss** | **str** | Token issuer | 
**jti** | **str** | Token ID | 

## Example

```python
from okta.models.security_event_token_request_jwt_body import SecurityEventTokenRequestJwtBody

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEventTokenRequestJwtBody from a JSON string
security_event_token_request_jwt_body_instance = SecurityEventTokenRequestJwtBody.from_json(json)
# print the JSON string representation of the object
print(SecurityEventTokenRequestJwtBody.to_json())

# convert the object into a dict
security_event_token_request_jwt_body_dict = security_event_token_request_jwt_body_instance.to_dict()
# create an instance of SecurityEventTokenRequestJwtBody from a dict
security_event_token_request_jwt_body_from_dict = SecurityEventTokenRequestJwtBody.from_dict(security_event_token_request_jwt_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


