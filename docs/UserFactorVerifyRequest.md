# UserFactorVerifyRequest

Sends an asynchronous push notification to the device for approval by the user. A successful request returns an HTTP 201 response, unlike other factors. You must poll the transaction to determine the state of the verification. See [Retrieve a factor transaction status](./#tag/UserFactor/operation/getFactorTransactionStatus).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_number_matching_challenge** | **bool** | Select whether to use a number matching challenge for a &#x60;push&#x60; factor.  &gt; **Note:** Sending a request with a body is required when you verify a &#x60;push&#x60; factor with a number matching challenge. | [optional] 

## Example

```python
from okta.models.user_factor_verify_request import UserFactorVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorVerifyRequest from a JSON string
user_factor_verify_request_instance = UserFactorVerifyRequest.from_json(json)
# print the JSON string representation of the object
print(UserFactorVerifyRequest.to_json())

# convert the object into a dict
user_factor_verify_request_dict = user_factor_verify_request_instance.to_dict()
# create an instance of UserFactorVerifyRequest from a dict
user_factor_verify_request_from_dict = UserFactorVerifyRequest.from_dict(user_factor_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


