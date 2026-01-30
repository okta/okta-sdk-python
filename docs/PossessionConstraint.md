# PossessionConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_methods** | [**List[AuthenticationMethodObject]**](AuthenticationMethodObject.md) | This property specifies the precise authenticator and method for authentication. &lt;x-lifecycle class&#x3D;\&quot;oie\&quot;&gt;&lt;/x-lifecycle&gt; | [optional] 
**excluded_authentication_methods** | [**List[AuthenticationMethodObject]**](AuthenticationMethodObject.md) | This property specifies the precise authenticator and method to exclude from authentication. &lt;x-lifecycle class&#x3D;\&quot;oie\&quot;&gt;&lt;/x-lifecycle&gt; | [optional] 
**methods** | **List[str]** | The authenticator methods that are permitted | [optional] 
**reauthenticate_in** | **str** | The duration after which the user must re-authenticate regardless of user activity. This re-authentication interval overrides the Verification Method object&#39;s &#x60;reauthenticateIn&#x60; interval. The supported values use ISO 8601 period format for recurring time intervals (for example, &#x60;PT1H&#x60;). | [optional] 
**required** | **bool** | This property indicates whether the knowledge or possession factor is required by the assurance. It&#39;s optional in the request, but is always returned in the response. By default, this field is &#x60;true&#x60;. If the knowledge or possession constraint has values for &#x60;excludedAuthenticationMethods&#x60; the &#x60;required&#x60; value is false. &lt;x-lifecycle class&#x3D;\&quot;oie\&quot;&gt;&lt;/x-lifecycle&gt; | [optional] 
**types** | **List[str]** | The authenticator types that are permitted | [optional] 
**device_bound** | **str** | Indicates if device-bound Factors are required. This property is only set for &#x60;POSSESSION&#x60; constraints. | [optional] [default to 'OPTIONAL']
**hardware_protection** | **str** | Indicates if any secrets or private keys used during authentication must be hardware protected and not exportable. This property is only set for &#x60;POSSESSION&#x60; constraints. | [optional] [default to 'OPTIONAL']
**phishing_resistant** | **str** | Indicates if phishing-resistant Factors are required. This property is only set for &#x60;POSSESSION&#x60; constraints. | [optional] [default to 'OPTIONAL']
**user_presence** | **str** | Indicates if the user needs to approve an Okta Verify prompt or provide biometrics (meets NIST AAL2 requirements). This property is only set for &#x60;POSSESSION&#x60; constraints. | [optional] [default to 'REQUIRED']
**user_verification** | **str** | Indicates the user interaction requirement (PIN or biometrics) to ensure verification of a possession factor | [optional] [default to 'OPTIONAL']
**user_verification_methods** | **List[str]** | Indicates which methods can be used for user verification. &#x60;userVerificationMethods&#x60; can only be used when &#x60;userVerification&#x60; is &#x60;REQUIRED&#x60;. &#x60;BIOMETRICS&#x60; is currently the only supported method. | [optional] 

## Example

```python
from okta.models.possession_constraint import PossessionConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of PossessionConstraint from a JSON string
possession_constraint_instance = PossessionConstraint.from_json(json)
# print the JSON string representation of the object
print(PossessionConstraint.to_json())

# convert the object into a dict
possession_constraint_dict = possession_constraint_instance.to_dict()
# create an instance of PossessionConstraint from a dict
possession_constraint_from_dict = PossessionConstraint.from_dict(possession_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


