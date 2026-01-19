# RegistrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commands** | [**List[RegistrationResponseCommandsInner]**](RegistrationResponseCommandsInner.md) | The &#x60;commands&#x60; object lets you invoke commands to modify or add values to the attributes in the Okta user profile that are created for this user. The object also lets you control whether or not the registration attempt is allowed to proceed.  This object is an array, allowing you to send multiple commands in your response. Each array element requires a &#x60;type&#x60; property and a &#x60;value&#x60; property. The &#x60;type&#x60; property is where you specify which of the supported commands you wish to execute, and &#x60;value&#x60; is where you supply parameters for that command.  The registration inline hook supports these three commands: * &#x60;com.okta.user.profile.update&#x60;: Change attribute values in the user&#39;s Okta user profile. For SSR only. Invalid if used with a Progressive Profile response. * &#x60;com.okta.action.update&#x60;: Allow or deny the user&#39;s registration. * &#x60;com.okta.user.progressive.profile.update&#x60;: Change attribute values in the user&#39;s Okta Progressive Profile. | [optional] 
**error** | [**RegistrationResponseError**](RegistrationResponseError.md) |  | [optional] 

## Example

```python
from okta.models.registration_response import RegistrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationResponse from a JSON string
registration_response_instance = RegistrationResponse.from_json(json)
# print the JSON string representation of the object
print(RegistrationResponse.to_json())

# convert the object into a dict
registration_response_dict = registration_response_instance.to_dict()
# create an instance of RegistrationResponse from a dict
registration_response_from_dict = RegistrationResponse.from_dict(registration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


