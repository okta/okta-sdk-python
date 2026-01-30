# IdentityProviderPolicy

Policy settings for the IdP. The following provisioning and account linking actions are supported by each IdP provider: | IdP type                                                           | User provisioning actions | Group provisioning actions            | Account link actions | Account link filters | | -----------------------------------------------------------------  | ------------------------- | ------------------------------------- | -------------------- | -------------------- | | `SAML2`                                                            | `AUTO` or `DISABLED`      | `NONE`, `ASSIGN`, `APPEND`, or `SYNC` | `AUTO`, `DISABLED`   | `groups`, `users`    | | `X509`, `IDV_PERSONA`, `IDV_INCODE`, `IDV_CLEAR` and `IDV_STANDARD`| `DISABLED`                | No support for JIT provisioning       |                      |                      | | All other IdP types                                                | `AUTO`, `DISABLED`        | `NONE` or `ASSIGN`                    | `AUTO`, `DISABLED`   | `groups`, `users`    |

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_link** | [**PolicyAccountLink**](PolicyAccountLink.md) |  | [optional] 
**max_clock_skew** | **int** | Maximum allowable clock skew when processing messages from the IdP | [optional] 
**provisioning** | [**Provisioning**](Provisioning.md) |  | [optional] 
**subject** | [**PolicySubject**](PolicySubject.md) |  | [optional] 

## Example

```python
from okta.models.identity_provider_policy import IdentityProviderPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderPolicy from a JSON string
identity_provider_policy_instance = IdentityProviderPolicy.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderPolicy.to_json())

# convert the object into a dict
identity_provider_policy_dict = identity_provider_policy_instance.to_dict()
# create an instance of IdentityProviderPolicy from a dict
identity_provider_policy_from_dict = IdentityProviderPolicy.from_dict(identity_provider_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


