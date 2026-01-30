# RegistrationResponseErrorErrorCausesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_summary** | **str** | Human-readable summary of the error. | [optional] 
**reason** | **str** | A brief, enum-like string that indicates the nature of the error. For example, &#x60;UNIQUE_CONSTRAINT&#x60; for a property uniqueness violation. | [optional] 
**location_type** | **str** | Where in the request the error was found (&#x60;body&#x60;, &#x60;header&#x60;, &#x60;url&#x60;, or &#x60;query&#x60;). | [optional] 
**location** | **str** | The valid JSON path to the location of the error. For example, if there was an error in the user&#39;s &#x60;login&#x60; field, the &#x60;location&#x60; might be &#x60;data.userProfile.login&#x60;. | [optional] 
**domain** | **str** | Indicates the source of the error. If the error was in the user&#39;s profile, for example, you might use &#x60;end-user&#x60;. If the error occurred in the external service, you might use &#x60;external-service&#x60;. | [optional] 

## Example

```python
from okta.models.registration_response_error_error_causes_inner import RegistrationResponseErrorErrorCausesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationResponseErrorErrorCausesInner from a JSON string
registration_response_error_error_causes_inner_instance = RegistrationResponseErrorErrorCausesInner.from_json(json)
# print the JSON string representation of the object
print(RegistrationResponseErrorErrorCausesInner.to_json())

# convert the object into a dict
registration_response_error_error_causes_inner_dict = registration_response_error_error_causes_inner_instance.to_dict()
# create an instance of RegistrationResponseErrorErrorCausesInner from a dict
registration_response_error_error_causes_inner_from_dict = RegistrationResponseErrorErrorCausesInner.from_dict(registration_response_error_error_causes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


