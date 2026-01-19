# UserFactorPushTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor_result** | **str** | Result of the verification transaction | [optional] 

## Example

```python
from okta.models.user_factor_push_transaction import UserFactorPushTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of UserFactorPushTransaction from a JSON string
user_factor_push_transaction_instance = UserFactorPushTransaction.from_json(json)
# print the JSON string representation of the object
print(UserFactorPushTransaction.to_json())

# convert the object into a dict
user_factor_push_transaction_dict = user_factor_push_transaction_instance.to_dict()
# create an instance of UserFactorPushTransaction from a dict
user_factor_push_transaction_from_dict = UserFactorPushTransaction.from_dict(user_factor_push_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


