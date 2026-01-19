# UserFactorActivateRequest

Sends an asynchronous push notification to the device for approval by the user. You must poll the transaction to determine the state of the verification. See [Retrieve a factor transaction status](./#tag/UserFactor/operation/getFactorTransactionStatus).  Activations have a short lifetime of several minutes and return a `TIMEOUT` if not completed before the timestamp specified in the `expiresAt` param. Use the published activate link to restart the activation process if the activation expires.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_number_matching_challenge** | **bool** | Select whether to use a number matching challenge for a &#x60;push&#x60; factor.  &gt; **Note:** Sending a request with a body is required when you verify a &#x60;push&#x60; factor with a number matching challenge. | [optional] 

## Example

```python
from okta.models.user_factor_activate_request import UserFactorActivateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorActivateRequest from a JSON string
user_factor_activate_request_instance = UserFactorActivateRequest.from_json(json)
# print the JSON string representation of the object
print(UserFactorActivateRequest.to_json())

# convert the object into a dict
user_factor_activate_request_dict = user_factor_activate_request_instance.to_dict()
# create an instance of UserFactorActivateRequest from a dict
user_factor_activate_request_from_dict = UserFactorActivateRequest.from_dict(user_factor_activate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


