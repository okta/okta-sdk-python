# SecurityEventTokenJwtBody

JSON Web Token body payload for a Security Event Token sent by the SSF Transmitter. For examples and more information, see [SSF Transmitter SET payload structures](https://developer.okta.com/docs/reference/ssf-transmitter-sets).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aud** | **str** | Audience | 
**events** | [**SecurityEventTokenJwtEvents**](SecurityEventTokenJwtEvents.md) |  | 
**iat** | **int** | Token issue time (UNIX timestamp) | 
**iss** | **str** | Token issuer | 
**jti** | **str** | Token ID | 

## Example

```python
from okta.models.security_event_token_jwt_body import SecurityEventTokenJwtBody

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEventTokenJwtBody from a JSON string
security_event_token_jwt_body_instance = SecurityEventTokenJwtBody.from_json(json)
# print the JSON string representation of the object
print(SecurityEventTokenJwtBody.to_json())

# convert the object into a dict
security_event_token_jwt_body_dict = security_event_token_jwt_body_instance.to_dict()
# create an instance of SecurityEventTokenJwtBody from a dict
security_event_token_jwt_body_from_dict = SecurityEventTokenJwtBody.from_dict(security_event_token_jwt_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


