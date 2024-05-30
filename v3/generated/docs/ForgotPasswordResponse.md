# ForgotPasswordResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reset_password_url** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.forgot_password_response import ForgotPasswordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ForgotPasswordResponse from a JSON string
forgot_password_response_instance = ForgotPasswordResponse.from_json(json)
# print the JSON string representation of the object
print(ForgotPasswordResponse.to_json())

# convert the object into a dict
forgot_password_response_dict = forgot_password_response_instance.to_dict()
# create an instance of ForgotPasswordResponse from a dict
forgot_password_response_form_dict = forgot_password_response.from_dict(forgot_password_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


