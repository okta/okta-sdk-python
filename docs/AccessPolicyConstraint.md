# AccessPolicyConstraint

Consists of a `POSSESSION` constraint, a `KNOWLEDGE` constraint, or both. You can't configure an `INHERENCE` constraint, but an inherence factor can satisfy the second part of a 2FA assurance if no other constraints are specified. Constraints are logically evaluated such that only one `constraint` object needs to be satisfied, but within a `constraint` object, each `constraint` property must be satisfied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_methods** | [**List[AuthenticationMethodObject]**](AuthenticationMethodObject.md) | This property specifies the precise authenticator and method for authentication. &lt;x-lifecycle class&#x3D;\&quot;oie\&quot;&gt;&lt;/x-lifecycle&gt; | [optional] 
**excluded_authentication_methods** | [**List[AuthenticationMethodObject]**](AuthenticationMethodObject.md) | This property specifies the precise authenticator and method to exclude from authentication. &lt;x-lifecycle class&#x3D;\&quot;oie\&quot;&gt;&lt;/x-lifecycle&gt; | [optional] 
**methods** | **List[str]** | The authenticator methods that are permitted | [optional] 
**reauthenticate_in** | **str** | The duration after which the user must re-authenticate regardless of user activity. This re-authentication interval overrides the Verification Method object&#39;s &#x60;reauthenticateIn&#x60; interval. The supported values use ISO 8601 period format for recurring time intervals (for example, &#x60;PT1H&#x60;). | [optional] 
**required** | **bool** | This property indicates whether the knowledge or possession factor is required by the assurance. It&#39;s optional in the request, but is always returned in the response. By default, this field is &#x60;true&#x60;. If the knowledge or possession constraint has values for &#x60;excludedAuthenticationMethods&#x60; the &#x60;required&#x60; value is false. &lt;x-lifecycle class&#x3D;\&quot;oie\&quot;&gt;&lt;/x-lifecycle&gt; | [optional] 
**types** | **List[str]** | The authenticator types that are permitted | [optional] 

## Example

```python
from okta.models.access_policy_constraint import AccessPolicyConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyConstraint from a JSON string
access_policy_constraint_instance = AccessPolicyConstraint.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyConstraint.to_json())

# convert the object into a dict
access_policy_constraint_dict = access_policy_constraint_instance.to_dict()
# create an instance of AccessPolicyConstraint from a dict
access_policy_constraint_from_dict = AccessPolicyConstraint.from_dict(access_policy_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


