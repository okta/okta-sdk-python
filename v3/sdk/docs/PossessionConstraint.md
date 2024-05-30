# PossessionConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**methods** | **List[str]** | The Authenticator methods that are permitted | [optional] 
**reauthenticate_in** | **str** | The duration after which the user must re-authenticate regardless of user activity. This re-authentication interval overrides the Verification Method object&#39;s &#x60;reauthenticateIn&#x60; interval. The supported values use ISO 8601 period format for recurring time intervals (for example, &#x60;PT1H&#x60;). | [optional] 
**types** | **List[str]** | The Authenticator types that are permitted | [optional] 
**authentication_methods** | [**List[AuthenticationMethodObject]**](AuthenticationMethodObject.md) | This property specifies the precise authenticator and method for authentication. | [optional] 
**excluded_authentication_methods** | [**List[AuthenticationMethodObject]**](AuthenticationMethodObject.md) | This property specifies the precise authenticator and method to exclude from authentication. | [optional] 
**required** | **bool** | This property indicates whether the knowledge or possession factor is required by the assurance. It&#39;s optional in the request, but is always returned in the response. By default, this field is &#x60;true&#x60;. If the knowledge or possession constraint has values for&#x60;excludedAuthenticationMethods&#x60; the &#x60;required&#x60; value is false. | [optional] 
**device_bound** | **str** | Indicates if device-bound Factors are required. This property is only set for &#x60;POSSESSION&#x60; constraints. | [optional] [default to 'OPTIONAL']
**hardware_protection** | **str** | Indicates if any secrets or private keys used during authentication must be hardware protected and not exportable. This property is only set for &#x60;POSSESSION&#x60; constraints. | [optional] [default to 'OPTIONAL']
**phishing_resistant** | **str** | Indicates if phishing-resistant Factors are required. This property is only set for &#x60;POSSESSION&#x60; constraints. | [optional] [default to 'OPTIONAL']
**user_presence** | **str** | Indicates if the user needs to approve an Okta Verify prompt or provide biometrics (meets NIST AAL2 requirements). This property is only set for &#x60;POSSESSION&#x60; constraints. | [optional] [default to 'REQUIRED']
**user_verification** | **str** | Indicates the user interaction requirement (PIN or biometrics) to ensure verification of a possession factor | [optional] [default to 'OPTIONAL']

## Example

```python
from openapi_client.models.possession_constraint import PossessionConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of PossessionConstraint from a JSON string
possession_constraint_instance = PossessionConstraint.from_json(json)
# print the JSON string representation of the object
print(PossessionConstraint.to_json())

# convert the object into a dict
possession_constraint_dict = possession_constraint_instance.to_dict()
# create an instance of PossessionConstraint from a dict
possession_constraint_form_dict = possession_constraint.from_dict(possession_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


