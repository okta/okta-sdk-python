# AuthenticationMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hardware_protection** | **str** | Indicates if any secrets or private keys used during authentication must be hardware protected and not exportable. This property is only set for &#x60;POSSESSION&#x60; constraints. | [optional] [default to 'OPTIONAL']
**id** | **str** | An ID that identifies the authenticator | [optional] 
**key** | **str** | A label that identifies the authenticator | 
**method** | **str** | Specifies the method used for the authenticator | 
**phishing_resistant** | **str** | Indicates if phishing-resistant Factors are required. This property is only set for &#x60;POSSESSION&#x60; constraints | [optional] [default to 'OPTIONAL']
**user_verification** | **str** | Indicates if a user is required to be verified with a verification method. | [optional] [default to 'OPTIONAL']
**user_verification_methods** | **List[str]** | Indicates which methods can be used for user verification. &#x60;userVerificationMethods&#x60; can only be used when &#x60;userVerification&#x60; is &#x60;REQUIRED&#x60;. &#x60;BIOMETRICS&#x60; is currently the only supported method. | [optional] 

## Example

```python
from okta.models.authentication_method import AuthenticationMethod

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationMethod from a JSON string
authentication_method_instance = AuthenticationMethod.from_json(json)
# print the JSON string representation of the object
print(AuthenticationMethod.to_json())

# convert the object into a dict
authentication_method_dict = authentication_method_instance.to_dict()
# create an instance of AuthenticationMethod from a dict
authentication_method_from_dict = AuthenticationMethod.from_dict(authentication_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


