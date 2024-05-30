# AuthenticationMethodObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A label that identifies the authenticator | [optional] 
**method** | **str** | Specifies the method used for the authenticator | [optional] 

## Example

```python
from openapi_client.models.authentication_method_object import AuthenticationMethodObject

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationMethodObject from a JSON string
authentication_method_object_instance = AuthenticationMethodObject.from_json(json)
# print the JSON string representation of the object
print(AuthenticationMethodObject.to_json())

# convert the object into a dict
authentication_method_object_dict = authentication_method_object_instance.to_dict()
# create an instance of AuthenticationMethodObject from a dict
authentication_method_object_form_dict = authentication_method_object.from_dict(authentication_method_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


