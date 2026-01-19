# PolicySubject

Specifies the behavior for establishing, validating, and matching a username for an IdP user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | Optional [regular expression pattern](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Regular_expressions) used to filter untrusted IdP usernames. * As a best security practice, you should define a regular expression pattern to filter untrusted IdP usernames. This is especially important if multiple IdPs are connected to your org. The filter prevents an IdP from issuing an assertion for any user, including partners or directory users in your Okta org. * For example, the filter pattern &#x60;(\\S+@example\\.com)&#x60; allows only Users that have an &#x60;@example.com&#x60; username suffix. It rejects assertions that have any other suffix such as &#x60;@corp.example.com&#x60; or &#x60;@partner.com&#x60;. * Only &#x60;SAML2&#x60; and &#x60;OIDC&#x60; IdP providers support the &#x60;filter&#x60; property. | [optional] 
**match_attribute** | **str** | Okta user profile attribute for matching a transformed IdP username. Only for matchType &#x60;CUSTOM_ATTRIBUTE&#x60;. The &#x60;matchAttribute&#x60; must be a valid Okta user profile attribute of one of the following types: * String (with no format or &#39;email&#39; format only) * Integer * Number | [optional] 
**match_type** | [**PolicySubjectMatchType**](PolicySubjectMatchType.md) |  | [optional] 
**user_name_template** | [**PolicyUserNameTemplate**](PolicyUserNameTemplate.md) |  | [optional] 

## Example

```python
from okta.models.policy_subject import PolicySubject

# TODO update the JSON string below
json = "{}"
# create an instance of PolicySubject from a JSON string
policy_subject_instance = PolicySubject.from_json(json)
# print the JSON string representation of the object
print(PolicySubject.to_json())

# convert the object into a dict
policy_subject_dict = policy_subject_instance.to_dict()
# create an instance of PolicySubject from a dict
policy_subject_from_dict = PolicySubject.from_dict(policy_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


