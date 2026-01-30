# FederatedClaim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** | Timestamp when the federated claim was created | [optional] [readonly] 
**expression** | **str** | The Okta Expression Language expression to be evaluated at runtime | [optional] 
**id** | **str** | The unique ID of the federated claim | [optional] [readonly] 
**last_updated** | **str** | Timestamp when the federated claim was updated | [optional] [readonly] 
**name** | **str** | The name of the claim to be used in the produced token | [optional] 

## Example

```python
from okta.models.federated_claim import FederatedClaim

# TODO update the JSON string below
json = "{}"
# create an instance of FederatedClaim from a JSON string
federated_claim_instance = FederatedClaim.from_json(json)
# print the JSON string representation of the object
print(FederatedClaim.to_json())

# convert the object into a dict
federated_claim_dict = federated_claim_instance.to_dict()
# create an instance of FederatedClaim from a dict
federated_claim_from_dict = FederatedClaim.from_dict(federated_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


