# Sso

Supported SSO protocol configurations. You must configure at least one protocol: `oidc` or `saml`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oidc** | [**Oidc**](Oidc.md) |  | [optional] 
**saml** | [**Saml**](Saml.md) |  | [optional] 

## Example

```python
from okta.models.sso import Sso

# TODO update the JSON string below
json = "{}"
# create an instance of Sso from a JSON string
sso_instance = Sso.from_json(json)
# print the JSON string representation of the object
print(Sso.to_json())

# convert the object into a dict
sso_dict = sso_instance.to_dict()
# create an instance of Sso from a dict
sso_from_dict = Sso.from_dict(sso_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


