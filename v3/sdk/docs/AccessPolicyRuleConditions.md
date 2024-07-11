# AccessPolicyRuleConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**AppAndInstancePolicyRuleCondition**](AppAndInstancePolicyRuleCondition.md) |  | [optional] 
**apps** | [**AppInstancePolicyRuleCondition**](AppInstancePolicyRuleCondition.md) |  | [optional] 
**auth_context** | [**PolicyRuleAuthContextCondition**](PolicyRuleAuthContextCondition.md) |  | [optional] 
**auth_provider** | [**PasswordPolicyAuthenticationProviderCondition**](PasswordPolicyAuthenticationProviderCondition.md) |  | [optional] 
**before_scheduled_action** | [**BeforeScheduledActionPolicyRuleCondition**](BeforeScheduledActionPolicyRuleCondition.md) |  | [optional] 
**clients** | [**ClientPolicyCondition**](ClientPolicyCondition.md) |  | [optional] 
**context** | [**ContextPolicyRuleCondition**](ContextPolicyRuleCondition.md) |  | [optional] 
**device** | [**DeviceAccessPolicyRuleCondition**](DeviceAccessPolicyRuleCondition.md) |  | [optional] 
**grant_types** | [**GrantTypePolicyRuleCondition**](GrantTypePolicyRuleCondition.md) |  | [optional] 
**groups** | [**GroupPolicyRuleCondition**](GroupPolicyRuleCondition.md) |  | [optional] 
**identity_provider** | [**IdentityProviderPolicyRuleCondition**](IdentityProviderPolicyRuleCondition.md) |  | [optional] 
**mdm_enrollment** | [**MDMEnrollmentPolicyRuleCondition**](MDMEnrollmentPolicyRuleCondition.md) |  | [optional] 
**network** | [**PolicyNetworkCondition**](PolicyNetworkCondition.md) |  | [optional] 
**people** | [**PolicyPeopleCondition**](PolicyPeopleCondition.md) |  | [optional] 
**platform** | [**PlatformPolicyRuleCondition**](PlatformPolicyRuleCondition.md) |  | [optional] 
**risk** | [**RiskPolicyRuleCondition**](RiskPolicyRuleCondition.md) |  | [optional] 
**risk_score** | [**RiskScorePolicyRuleCondition**](RiskScorePolicyRuleCondition.md) |  | [optional] 
**scopes** | [**OAuth2ScopesMediationPolicyRuleCondition**](OAuth2ScopesMediationPolicyRuleCondition.md) |  | [optional] 
**user_identifier** | [**UserIdentifierPolicyRuleCondition**](UserIdentifierPolicyRuleCondition.md) |  | [optional] 
**users** | [**UserPolicyRuleCondition**](UserPolicyRuleCondition.md) |  | [optional] 
**user_status** | [**UserStatusPolicyRuleCondition**](UserStatusPolicyRuleCondition.md) |  | [optional] 
**el_condition** | [**AccessPolicyRuleCustomCondition**](AccessPolicyRuleCustomCondition.md) |  | [optional] 
**user_type** | [**UserTypeCondition**](UserTypeCondition.md) |  | [optional] 

## Example

```python
from okta.models.access_policy_rule_conditions import AccessPolicyRuleConditions

# TODO update the JSON string below
json = "{}"
# create an instance of AccessPolicyRuleConditions from a JSON string
access_policy_rule_conditions_instance = AccessPolicyRuleConditions.from_json(json)
# print the JSON string representation of the object
print(AccessPolicyRuleConditions.to_json())

# convert the object into a dict
access_policy_rule_conditions_dict = access_policy_rule_conditions_instance.to_dict()
# create an instance of AccessPolicyRuleConditions from a dict
access_policy_rule_conditions_from_dict = AccessPolicyRuleConditions.from_dict(access_policy_rule_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


