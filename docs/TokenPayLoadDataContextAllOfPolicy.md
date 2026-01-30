# TokenPayLoadDataContextAllOfPolicy

The authorization server policy used to mint the token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the policy | [optional] 
**rule** | [**TokenPayLoadDataContextAllOfPolicyRule**](TokenPayLoadDataContextAllOfPolicyRule.md) |  | [optional] 

## Example

```python
from okta.models.token_pay_load_data_context_all_of_policy import TokenPayLoadDataContextAllOfPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of TokenPayLoadDataContextAllOfPolicy from a JSON string
token_pay_load_data_context_all_of_policy_instance = TokenPayLoadDataContextAllOfPolicy.from_json(json)
# print the JSON string representation of the object
print(TokenPayLoadDataContextAllOfPolicy.to_json())

# convert the object into a dict
token_pay_load_data_context_all_of_policy_dict = token_pay_load_data_context_all_of_policy_instance.to_dict()
# create an instance of TokenPayLoadDataContextAllOfPolicy from a dict
token_pay_load_data_context_all_of_policy_from_dict = TokenPayLoadDataContextAllOfPolicy.from_dict(token_pay_load_data_context_all_of_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


