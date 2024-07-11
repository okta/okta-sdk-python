# AuthorizationServerPolicyRuleConditions


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
**device** | [**DevicePolicyRuleCondition**](DevicePolicyRuleCondition.md) |  | [optional] 
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

## Example

```python
from okta.models.authorization_server_policy_rule_conditions import AuthorizationServerPolicyRuleConditions

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerPolicyRuleConditions from a JSON string
authorization_server_policy_rule_conditions_instance = AuthorizationServerPolicyRuleConditions.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerPolicyRuleConditions.to_json())

# convert the object into a dict
authorization_server_policy_rule_conditions_dict = authorization_server_policy_rule_conditions_instance.to_dict()
# create an instance of AuthorizationServerPolicyRuleConditions from a dict
authorization_server_policy_rule_conditions_from_dict = AuthorizationServerPolicyRuleConditions.from_dict(authorization_server_policy_rule_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


