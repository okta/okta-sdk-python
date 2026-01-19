# RegistrationResponseError

For the registration inline hook, the `error` object provides a way of displaying an error message to the end user who is trying to register or update their profile.  * If you're using the Okta Sign-In Widget for Profile Enrollment, only the `errorSummary` messages of the `errorCauses` objects that your external service returns appear as inline errors, given the following:   * You don't customize the error handling behavior of the widget.   * The `location` of `errorSummary` in the `errorCauses` object specifies the request object's user profile attribute. * If you don't return a value for the `errorCauses` object, and deny the user's registration attempt through the `commands` object in your response to Okta, one of the following generic messages appears to the end user:   * \"Registration cannot be completed at this time.\" (SSR)   * \"We found some errors. Please review the form and make corrections.\" (Progressive Enrollment) * If you don't return an `error` object at all and the registration is denied, the following generic message appears to the end user:   * \"Registration denied.\" (SSR)   * \"Profile update denied.\" (Progressive Enrollment)  >**Note:** If you include an error object in your response, no commands are executed and the registration fails. This holds true even if the top-level `errorSummary` and the `errorCauses` objects are omitted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_summary** | **str** | Human-readable summary of one or more errors | [optional] 
**error_causes** | [**List[RegistrationResponseErrorErrorCausesInner]**](RegistrationResponseErrorErrorCausesInner.md) |  | [optional] 

## Example

```python
from okta.models.registration_response_error import RegistrationResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationResponseError from a JSON string
registration_response_error_instance = RegistrationResponseError.from_json(json)
# print the JSON string representation of the object
print(RegistrationResponseError.to_json())

# convert the object into a dict
registration_response_error_dict = registration_response_error_instance.to_dict()
# create an instance of RegistrationResponseError from a dict
registration_response_error_from_dict = RegistrationResponseError.from_dict(registration_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


