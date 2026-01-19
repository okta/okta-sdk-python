# AuthorizationServerPolicyAllOfLinksAllOfRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**HrefHints**](HrefHints.md) |  | [optional] 
**href** | **str** | Link URI | 
**name** | **str** | Link name | [optional] [readonly] 
**templated** | **bool** | Indicates whether the link object&#39;s &#x60;href&#x60; property is a URI template. | [optional] [readonly] 
**type** | **str** | The media type of the link. If omitted, it is implicitly &#x60;application/json&#x60;. | [optional] [readonly] 

## Example

```python
from okta.models.authorization_server_policy_all_of_links_all_of_rules import AuthorizationServerPolicyAllOfLinksAllOfRules

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerPolicyAllOfLinksAllOfRules from a JSON string
authorization_server_policy_all_of_links_all_of_rules_instance = AuthorizationServerPolicyAllOfLinksAllOfRules.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerPolicyAllOfLinksAllOfRules.to_json())

# convert the object into a dict
authorization_server_policy_all_of_links_all_of_rules_dict = authorization_server_policy_all_of_links_all_of_rules_instance.to_dict()
# create an instance of AuthorizationServerPolicyAllOfLinksAllOfRules from a dict
authorization_server_policy_all_of_links_all_of_rules_from_dict = AuthorizationServerPolicyAllOfLinksAllOfRules.from_dict(authorization_server_policy_all_of_links_all_of_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


