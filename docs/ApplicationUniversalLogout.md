# ApplicationUniversalLogout

<div class=\"x-lifecycle-container\"><x-lifecycle class=\"oie\"></x-lifecycle></div> Universal Logout properties for the app. These properties are only returned and can't be updated.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_stack** | **str** | Indicates whether the app uses a shared identity stack that may cause the user to sign out of other apps by the same company | [optional] 
**protocol** | **str** | The protocol used for Universal Logout | [optional] 
**status** | **str** | Universal Logout status for the app instance | [optional] 
**support_type** | **str** | Indicates whether the app supports full or partial Universal Logout (UL). | [optional] 

## Example

```python
from okta.models.application_universal_logout import ApplicationUniversalLogout

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationUniversalLogout from a JSON string
application_universal_logout_instance = ApplicationUniversalLogout.from_json(json)
# print the JSON string representation of the object
print(ApplicationUniversalLogout.to_json())

# convert the object into a dict
application_universal_logout_dict = application_universal_logout_instance.to_dict()
# create an instance of ApplicationUniversalLogout from a dict
application_universal_logout_from_dict = ApplicationUniversalLogout.from_dict(application_universal_logout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


