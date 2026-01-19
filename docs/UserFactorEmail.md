# UserFactorEmail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UserFactorEmailProfile**](UserFactorEmailProfile.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_email import UserFactorEmail

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorEmail from a JSON string
user_factor_email_instance = UserFactorEmail.from_json(json)
# print the JSON string representation of the object
print(UserFactorEmail.to_json())

# convert the object into a dict
user_factor_email_dict = user_factor_email_instance.to_dict()
# create an instance of UserFactorEmail from a dict
user_factor_email_from_dict = UserFactorEmail.from_dict(user_factor_email_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


