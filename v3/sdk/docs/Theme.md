# Theme


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_image** | **str** |  | [optional] [readonly] 
**email_template_touch_point_variant** | [**EmailTemplateTouchPointVariant**](EmailTemplateTouchPointVariant.md) |  | [optional] 
**end_user_dashboard_touch_point_variant** | [**EndUserDashboardTouchPointVariant**](EndUserDashboardTouchPointVariant.md) |  | [optional] 
**error_page_touch_point_variant** | [**ErrorPageTouchPointVariant**](ErrorPageTouchPointVariant.md) |  | [optional] 
**loading_page_touch_point_variant** | [**LoadingPageTouchPointVariant**](LoadingPageTouchPointVariant.md) |  | [optional] 
**primary_color_contrast_hex** | **str** |  | [optional] 
**primary_color_hex** | **str** |  | [optional] 
**secondary_color_contrast_hex** | **str** |  | [optional] 
**secondary_color_hex** | **str** |  | [optional] 
**sign_in_page_touch_point_variant** | [**SignInPageTouchPointVariant**](SignInPageTouchPointVariant.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.theme import Theme

# TODO update the JSON string below
json = "{}"
# create an instance of Theme from a JSON string
theme_instance = Theme.from_json(json)
# print the JSON string representation of the object
print(Theme.to_json())

# convert the object into a dict
theme_dict = theme_instance.to_dict()
# create an instance of Theme from a dict
theme_form_dict = theme.from_dict(theme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


