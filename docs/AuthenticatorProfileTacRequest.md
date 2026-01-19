# AuthenticatorProfileTacRequest

Defines the authenticator specific parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multi_use** | **bool** | Determines whether the enrollment can be used more than once. To enable multi-use, the org-level authenticator’s configuration must allow multi-use. | [optional] 
**ttl** | **str** | Time-to-live (TTL) in minutes.  Specifies how long the TAC enrollment is valid after it&#39;s created and activated. The configured value must be between 10 minutes (&#x60;10&#x60;) and 10 days (&#x60;14400&#x60;), inclusive. The actual allowed range depends on the org-level authenticator configuration. | [optional] 

## Example

```python
from okta.models.authenticator_profile_tac_request import AuthenticatorProfileTacRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorProfileTacRequest from a JSON string
authenticator_profile_tac_request_instance = AuthenticatorProfileTacRequest.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorProfileTacRequest.to_json())

# convert the object into a dict
authenticator_profile_tac_request_dict = authenticator_profile_tac_request_instance.to_dict()
# create an instance of AuthenticatorProfileTacRequest from a dict
authenticator_profile_tac_request_from_dict = AuthenticatorProfileTacRequest.from_dict(authenticator_profile_tac_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


