# VerificationMethod

The method used to verify a user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PolicyRuleVerificationMethodType**](PolicyRuleVerificationMethodType.md) |  | [optional] 

## Example

```python
from okta.models.verification_method import VerificationMethod

# TODO update the JSON string below
json = "{}"
# create an instance of VerificationMethod from a JSON string
verification_method_instance = VerificationMethod.from_json(json)
# print the JSON string representation of the object
print(VerificationMethod.to_json())

# convert the object into a dict
verification_method_dict = verification_method_instance.to_dict()
# create an instance of VerificationMethod from a dict
verification_method_from_dict = VerificationMethod.from_dict(verification_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


