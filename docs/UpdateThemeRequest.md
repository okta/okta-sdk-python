# UpdateThemeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_template_touch_point_variant** | [**EmailTemplateTouchPointVariant**](EmailTemplateTouchPointVariant.md) |  | [default to EmailTemplateTouchPointVariant.OKTA_DEFAULT]
**end_user_dashboard_touch_point_variant** | [**EndUserDashboardTouchPointVariant**](EndUserDashboardTouchPointVariant.md) |  | [default to EndUserDashboardTouchPointVariant.OKTA_DEFAULT]
**error_page_touch_point_variant** | [**ErrorPageTouchPointVariant**](ErrorPageTouchPointVariant.md) |  | [default to ErrorPageTouchPointVariant.OKTA_DEFAULT]
**loading_page_touch_point_variant** | [**LoadingPageTouchPointVariant**](LoadingPageTouchPointVariant.md) |  | [optional] [default to LoadingPageTouchPointVariant.OKTA_DEFAULT]
**primary_color_contrast_hex** | **str** | Primary color contrast hex code | [optional] 
**primary_color_hex** | **str** | Primary color hex code | 
**secondary_color_contrast_hex** | **str** | Secondary color contrast hex code | [optional] 
**secondary_color_hex** | **str** | Secondary color hex code | 
**sign_in_page_touch_point_variant** | [**SignInPageTouchPointVariant**](SignInPageTouchPointVariant.md) |  | 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from okta.models.update_theme_request import UpdateThemeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateThemeRequest from a JSON string
update_theme_request_instance = UpdateThemeRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateThemeRequest.to_json())

# convert the object into a dict
update_theme_request_dict = update_theme_request_instance.to_dict()
# create an instance of UpdateThemeRequest from a dict
update_theme_request_from_dict = UpdateThemeRequest.from_dict(update_theme_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


