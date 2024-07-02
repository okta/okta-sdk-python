# ActivateFactorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attestation** | **str** |  | [optional] 
**client_data** | **str** |  | [optional] 
**pass_code** | **str** |  | [optional] 
**registration_data** | **str** |  | [optional] 
**state_token** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.activate_factor_request import ActivateFactorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateFactorRequest from a JSON string
activate_factor_request_instance = ActivateFactorRequest.from_json(json)
# print the JSON string representation of the object
print(ActivateFactorRequest.to_json())

# convert the object into a dict
activate_factor_request_dict = activate_factor_request_instance.to_dict()
# create an instance of ActivateFactorRequest from a dict
activate_factor_request_from_dict = ActivateFactorRequest.from_dict(activate_factor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


