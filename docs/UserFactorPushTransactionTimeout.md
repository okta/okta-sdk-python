# UserFactorPushTransactionTimeout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UserFactorPushTransactionRejectedAllOfProfile**](UserFactorPushTransactionRejectedAllOfProfile.md) |  | [optional] 
**links** | [**UserFactorPushTransactionTimeoutAllOfLinks**](UserFactorPushTransactionTimeoutAllOfLinks.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_push_transaction_timeout import UserFactorPushTransactionTimeout

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorPushTransactionTimeout from a JSON string
user_factor_push_transaction_timeout_instance = UserFactorPushTransactionTimeout.from_json(json)
# print the JSON string representation of the object
print(UserFactorPushTransactionTimeout.to_json())

# convert the object into a dict
user_factor_push_transaction_timeout_dict = user_factor_push_transaction_timeout_instance.to_dict()
# create an instance of UserFactorPushTransactionTimeout from a dict
user_factor_push_transaction_timeout_from_dict = UserFactorPushTransactionTimeout.from_dict(user_factor_push_transaction_timeout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


