# UserFactorPushTransactionWaitingNMC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**UserFactorPushTransactionRejectedAllOfProfile**](UserFactorPushTransactionRejectedAllOfProfile.md) |  | [optional] 
**embedded** | [**NumberFactorChallengeEmbeddedLinks**](NumberFactorChallengeEmbeddedLinks.md) |  | [optional] 
**links** | [**UserFactorPushTransactionWaitingNMCAllOfLinks**](UserFactorPushTransactionWaitingNMCAllOfLinks.md) |  | [optional] 

## Example

```python
from okta.models.user_factor_push_transaction_waiting_nmc import UserFactorPushTransactionWaitingNMC

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorPushTransactionWaitingNMC from a JSON string
user_factor_push_transaction_waiting_nmc_instance = UserFactorPushTransactionWaitingNMC.from_json(json)
# print the JSON string representation of the object
print(UserFactorPushTransactionWaitingNMC.to_json())

# convert the object into a dict
user_factor_push_transaction_waiting_nmc_dict = user_factor_push_transaction_waiting_nmc_instance.to_dict()
# create an instance of UserFactorPushTransactionWaitingNMC from a dict
user_factor_push_transaction_waiting_nmc_from_dict = UserFactorPushTransactionWaitingNMC.from_dict(user_factor_push_transaction_waiting_nmc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


