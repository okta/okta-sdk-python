# SignInPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_content** | **str** | The HTML for the page | [optional] 
**content_security_policy_setting** | [**ContentSecurityPolicySetting**](ContentSecurityPolicySetting.md) |  | [optional] 
**widget_customizations** | [**SignInPageAllOfWidgetCustomizations**](SignInPageAllOfWidgetCustomizations.md) |  | [optional] 
**widget_version** | **str** | The version specified as a [Semantic Version](https://semver.org/). This value can be a wildcard (&#x60;*&#x60;), a major version range (for example, &#x60;^2&#x60;), a major-only version (for example, &#x60;7&#x60;), or a specific &#x60;Major.Minor&#x60; version (for example, &#x60;5.15&#x60;). | [optional] 

## Example

```python
from okta.models.sign_in_page import SignInPage

# TODO update the JSON string below
json = "{}"
# create an instance of SignInPage from a JSON string
sign_in_page_instance = SignInPage.from_json(json)
# print the JSON string representation of the object
print(SignInPage.to_json())

# convert the object into a dict
sign_in_page_dict = sign_in_page_instance.to_dict()
# create an instance of SignInPage from a dict
sign_in_page_from_dict = SignInPage.from_dict(sign_in_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


