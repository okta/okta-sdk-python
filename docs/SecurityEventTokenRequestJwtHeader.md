# SecurityEventTokenRequestJwtHeader

JSON Web Token header for a Security Event Token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alg** | **str** | Algorithm used to sign or encrypt the JWT | 
**kid** | **str** | Key ID used to sign or encrypt the JWT | 
**typ** | **str** | The type of content being signed or encrypted | 

## Example

```python
from okta.models.security_event_token_request_jwt_header import SecurityEventTokenRequestJwtHeader

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityEventTokenRequestJwtHeader from a JSON string
security_event_token_request_jwt_header_instance = SecurityEventTokenRequestJwtHeader.from_json(json)
# print the JSON string representation of the object
print(SecurityEventTokenRequestJwtHeader.to_json())

# convert the object into a dict
security_event_token_request_jwt_header_dict = security_event_token_request_jwt_header_instance.to_dict()
# create an instance of SecurityEventTokenRequestJwtHeader from a dict
security_event_token_request_jwt_header_from_dict = SecurityEventTokenRequestJwtHeader.from_dict(security_event_token_request_jwt_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


