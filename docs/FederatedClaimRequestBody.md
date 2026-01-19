# FederatedClaimRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | The Okta Expression Language expression to be evaluated at runtime | [optional] 
**name** | **str** | The name of the claim to be used in the produced token | [optional] 

## Example

```python
from okta.models.federated_claim_request_body import FederatedClaimRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of FederatedClaimRequestBody from a JSON string
federated_claim_request_body_instance = FederatedClaimRequestBody.from_json(json)
# print the JSON string representation of the object
print(FederatedClaimRequestBody.to_json())

# convert the object into a dict
federated_claim_request_body_dict = federated_claim_request_body_instance.to_dict()
# create an instance of FederatedClaimRequestBody from a dict
federated_claim_request_body_from_dict = FederatedClaimRequestBody.from_dict(federated_claim_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


