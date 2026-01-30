# AttackProtectionAuthenticatorSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verify_knowledge_second_when2fa_required** | **bool** | If true, requires users to verify a possession factor before verifying a knowledge factor when the assurance requires two-factor authentication (2FA). | [optional] [default to False]

## Example

```python
from okta.models.attack_protection_authenticator_settings import AttackProtectionAuthenticatorSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AttackProtectionAuthenticatorSettings from a JSON string
attack_protection_authenticator_settings_instance = AttackProtectionAuthenticatorSettings.from_json(json)
# print the JSON string representation of the object
print(AttackProtectionAuthenticatorSettings.to_json())

# convert the object into a dict
attack_protection_authenticator_settings_dict = attack_protection_authenticator_settings_instance.to_dict()
# create an instance of AttackProtectionAuthenticatorSettings from a dict
attack_protection_authenticator_settings_from_dict = AttackProtectionAuthenticatorSettings.from_dict(attack_protection_authenticator_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


