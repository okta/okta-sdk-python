# AuthorizationServerPolicyAllOfLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**activate** | [**HrefObjectActivateLink**](HrefObjectActivateLink.md) |  | [optional] 
**deactivate** | [**HrefObjectDeactivateLink**](HrefObjectDeactivateLink.md) |  | [optional] 
**rules** | [**AuthorizationServerPolicyAllOfLinksAllOfRules**](AuthorizationServerPolicyAllOfLinksAllOfRules.md) |  | [optional] 

## Example

```python
from okta.models.authorization_server_policy_all_of_links import AuthorizationServerPolicyAllOfLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationServerPolicyAllOfLinks from a JSON string
authorization_server_policy_all_of_links_instance = AuthorizationServerPolicyAllOfLinks.from_json(json)
# print the JSON string representation of the object
print(AuthorizationServerPolicyAllOfLinks.to_json())

# convert the object into a dict
authorization_server_policy_all_of_links_dict = authorization_server_policy_all_of_links_instance.to_dict()
# create an instance of AuthorizationServerPolicyAllOfLinks from a dict
authorization_server_policy_all_of_links_from_dict = AuthorizationServerPolicyAllOfLinks.from_dict(authorization_server_policy_all_of_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


