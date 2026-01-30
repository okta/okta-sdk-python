# UserFactorEmailProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address of the user. This must be either the primary or secondary email address associated with the Okta user account.  &gt; **Note:** For Identity Engine orgs, you can only enroll the primary email address of the user. | [optional] 

## Example

```python
from okta.models.user_factor_email_profile import UserFactorEmailProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorEmailProfile from a JSON string
user_factor_email_profile_instance = UserFactorEmailProfile.from_json(json)
# print the JSON string representation of the object
print(UserFactorEmailProfile.to_json())

# convert the object into a dict
user_factor_email_profile_dict = user_factor_email_profile_instance.to_dict()
# create an instance of UserFactorEmailProfile from a dict
user_factor_email_profile_from_dict = UserFactorEmailProfile.from_dict(user_factor_email_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


