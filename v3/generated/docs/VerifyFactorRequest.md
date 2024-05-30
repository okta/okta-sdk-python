# VerifyFactorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_token** | **str** |  | [optional] 
**answer** | **str** |  | [optional] 
**attestation** | **str** |  | [optional] 
**client_data** | **str** |  | [optional] 
**next_pass_code** | **str** |  | [optional] 
**pass_code** | **str** |  | [optional] 
**registration_data** | **str** |  | [optional] 
**state_token** | **str** |  | [optional] 
**authenticator_data** | **str** |  | [optional] 
**signature_data** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.verify_factor_request import VerifyFactorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyFactorRequest from a JSON string
verify_factor_request_instance = VerifyFactorRequest.from_json(json)
# print the JSON string representation of the object
print(VerifyFactorRequest.to_json())

# convert the object into a dict
verify_factor_request_dict = verify_factor_request_instance.to_dict()
# create an instance of VerifyFactorRequest from a dict
verify_factor_request_form_dict = verify_factor_request.from_dict(verify_factor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


