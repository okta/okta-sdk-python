# ResendUserFactor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor_type** | **str** | Type of the factor | [optional] 

## Example

```python
from okta.models.resend_user_factor import ResendUserFactor

# TODO update the JSON string below
json = "{}"
# create an instance of ResendUserFactor from a JSON string
resend_user_factor_instance = ResendUserFactor.from_json(json)
# print the JSON string representation of the object
print(ResendUserFactor.to_json())

# convert the object into a dict
resend_user_factor_dict = resend_user_factor_instance.to_dict()
# create an instance of ResendUserFactor from a dict
resend_user_factor_from_dict = ResendUserFactor.from_dict(resend_user_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


