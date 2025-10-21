# IdentityProviderPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_link** | [**PolicyAccountLink**](PolicyAccountLink.md) |  | [optional] 
**map_amr_claims** | **bool** | Enable mapping AMR from IdP to Okta to downstream apps | [optional] [default to False]
**max_clock_skew** | **int** |  | [optional] 
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


