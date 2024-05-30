# PasswordPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**PasswordPolicyConditions**](PasswordPolicyConditions.md) |  | [optional] 
**settings** | [**PasswordPolicySettings**](PasswordPolicySettings.md) |  | [optional] 

## Example

```python
from openapi_client.models.password_policy import PasswordPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicy from a JSON string
password_policy_instance = PasswordPolicy.from_json(json)
# print the JSON string representation of the object
print(PasswordPolicy.to_json())

# convert the object into a dict
password_policy_dict = password_policy_instance.to_dict()
# create an instance of PasswordPolicy from a dict
password_policy_form_dict = password_policy.from_dict(password_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


