# U2fUserFactor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**U2fUserFactorProfile**](U2fUserFactorProfile.md) |  | [optional] 

## Example

```python
from openapi_client.models.u2f_user_factor import U2fUserFactor

# TODO update the JSON string below
json = "{}"
# create an instance of U2fUserFactor from a JSON string
u2f_user_factor_instance = U2fUserFactor.from_json(json)
# print the JSON string representation of the object
print(U2fUserFactor.to_json())

# convert the object into a dict
u2f_user_factor_dict = u2f_user_factor_instance.to_dict()
# create an instance of U2fUserFactor from a dict
u2f_user_factor_form_dict = u2f_user_factor.from_dict(u2f_user_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


