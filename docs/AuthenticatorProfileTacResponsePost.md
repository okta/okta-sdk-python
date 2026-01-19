# AuthenticatorProfileTacResponsePost

Defines the authenticator specific parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** | The time when the TAC enrollment expires in the UTC timezone | [optional] 
**multi_use** | **bool** | Determines whether an enrollment can be used more than once | [optional] 
**tac** | **str** | A temporary access code used for authentication. It can be used one or more times and is valid for a defined period specified by the &#x60;ttl&#x60; property. The &#x60;tac&#x60; is returned in the response when the enrollment is created. It is not returned when the enrollment is retrieved. Issuing a new TAC invalidates any existing TAC for this user. | [optional] 

## Example

```python
from okta.models.authenticator_profile_tac_response_post import AuthenticatorProfileTacResponsePost

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorProfileTacResponsePost from a JSON string
authenticator_profile_tac_response_post_instance = AuthenticatorProfileTacResponsePost.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorProfileTacResponsePost.to_json())

# convert the object into a dict
authenticator_profile_tac_response_post_dict = authenticator_profile_tac_response_post_instance.to_dict()
# create an instance of AuthenticatorProfileTacResponsePost from a dict
authenticator_profile_tac_response_post_from_dict = AuthenticatorProfileTacResponsePost.from_dict(authenticator_profile_tac_response_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


