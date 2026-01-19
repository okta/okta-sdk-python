# RegistrationResponseCommandsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The location where you specify the command. To set attributes in the user&#39;s Okta profile, supply a &#x60;type&#x60; property set to &#x60;com.okta.user.profile.update&#x60;, together with a &#x60;value&#x60; property set to a list of key-value pairs corresponding to the Okta user profile attributes you want to set. The attributes must already exist in your user profile schema.  To explicitly allow or deny registration to the user, supply a type property set to &#x60;com.okta.action.update&#x60;, together with a value property set to &#x60;{\&quot;registration\&quot;: \&quot;ALLOW\&quot;}&#x60; or &#x60;{\&quot;registration\&quot;: \&quot;DENY\&quot;}&#x60;. The default is to allow registration.  In Okta Identity Engine, to set attributes in the user&#39;s profile, supply a &#x60;type&#x60; property set to &#x60;com.okta.user.progressive.profile.update&#x60;, together with a &#x60;value&#x60; property set to a list of key-value pairs corresponding to the Progressive Enrollment attributes that you want to set. See [Registration inline hook - Send response](https://developer.okta.com/docs/guides/registration-inline-hook/nodejs/main/#send-response).  Commands are applied in the order that they appear in the array. Within a single &#x60;com.okta.user.profile.update&#x60; or &#x60;com.okta.user.progressive.profile.update command&#x60;, attributes are updated in the order that they appear in the &#x60;value&#x60; object.  You can never use a command to update the user&#39;s password, but you are allowed to set the values of attributes other than password that are designated sensitive in your Okta user schema. However, the values of those sensitive attributes, if included as fields in the Profile Enrollment form, aren&#39;t included in the &#x60;data.userProfile&#x60; object sent to your external service by Okta. See [data.userProfile](/openapi/okta-management/management/tag/InlineHook/#tag/InlineHook/operation/create-registration-hook!path&#x3D;0/data/userProfile&amp;t&#x3D;request). | [optional] 
**value** | **Dict[str, object]** | The &#x60;value&#x60; object is the parameter to pass to the command.  For &#x60;com.okta.user.profile.update&#x60; commands, &#x60;value&#x60; should be an object containing one or more name-value pairs for the attributes you wish to update.  For &#x60;com.okta.action.update&#x60; commands, the value should be an object containing the attribute &#x60;action&#x60; set to a value of either &#x60;ALLOW&#x60; or &#x60;DENY&#x60;, indicating whether the registration should be permitted or not.  Registrations are allowed by default, so setting a value of &#x60;ALLOW&#x60; for the action field is valid but superfluous. | [optional] 

## Example

```python
from okta.models.registration_response_commands_inner import RegistrationResponseCommandsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationResponseCommandsInner from a JSON string
registration_response_commands_inner_instance = RegistrationResponseCommandsInner.from_json(json)
# print the JSON string representation of the object
print(RegistrationResponseCommandsInner.to_json())

# convert the object into a dict
registration_response_commands_inner_dict = registration_response_commands_inner_instance.to_dict()
# create an instance of RegistrationResponseCommandsInner from a dict
registration_response_commands_inner_from_dict = RegistrationResponseCommandsInner.from_dict(registration_response_commands_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


