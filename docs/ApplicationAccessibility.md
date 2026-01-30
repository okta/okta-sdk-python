# ApplicationAccessibility

Specifies access settings for the app

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_redirect_url** | **str** | Custom error page URL for the app | [optional] 
**login_redirect_url** | **str** | Custom login page URL for the app &gt; **Note:** The &#x60;loginRedirectUrl&#x60; property is deprecated in Identity Engine. This property is used with the custom app login feature. Orgs that actively use this feature can continue to do so. See [Okta-hosted sign-in (redirect authentication)](https://developer.okta.com/docs/guides/redirect-authentication/) or [configure IdP routing rules](https://help.okta.com/okta_help.htm?type&#x3D;oie&amp;id&#x3D;ext-cfg-routing-rules) to redirect users to the appropriate sign-in app for orgs that don&#39;t use the custom app login feature. | [optional] 
**self_service** | **bool** | Represents whether the app can be self-assignable by users | [optional] 

## Example

```python
from okta.models.application_accessibility import ApplicationAccessibility

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationAccessibility from a JSON string
application_accessibility_instance = ApplicationAccessibility.from_json(json)
# print the JSON string representation of the object
print(ApplicationAccessibility.to_json())

# convert the object into a dict
application_accessibility_dict = application_accessibility_instance.to_dict()
# create an instance of ApplicationAccessibility from a dict
application_accessibility_from_dict = ApplicationAccessibility.from_dict(application_accessibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


