# AuthenticatorEnrollmentLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**user** | [**LinksUserAuthenticatorsUser**](LinksUserAuthenticatorsUser.md) |  | [optional] 
**authenticator** | [**LinksAuthenticatorAuthenticator**](LinksAuthenticatorAuthenticator.md) |  | [optional] 

## Example

```python
from okta.models.authenticator_enrollment_links import AuthenticatorEnrollmentLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorEnrollmentLinks from a JSON string
authenticator_enrollment_links_instance = AuthenticatorEnrollmentLinks.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorEnrollmentLinks.to_json())

# convert the object into a dict
authenticator_enrollment_links_dict = authenticator_enrollment_links_instance.to_dict()
# create an instance of AuthenticatorEnrollmentLinks from a dict
authenticator_enrollment_links_from_dict = AuthenticatorEnrollmentLinks.from_dict(authenticator_enrollment_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


