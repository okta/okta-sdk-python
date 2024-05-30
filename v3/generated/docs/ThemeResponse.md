# ThemeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_image** | **str** |  | [optional] [readonly] 
**email_template_touch_point_variant** | [**EmailTemplateTouchPointVariant**](EmailTemplateTouchPointVariant.md) |  | [optional] 
**end_user_dashboard_touch_point_variant** | [**EndUserDashboardTouchPointVariant**](EndUserDashboardTouchPointVariant.md) |  | [optional] 
**error_page_touch_point_variant** | [**ErrorPageTouchPointVariant**](ErrorPageTouchPointVariant.md) |  | [optional] 
**favicon** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**loading_page_touch_point_variant** | [**LoadingPageTouchPointVariant**](LoadingPageTouchPointVariant.md) |  | [optional] 
**logo** | **str** |  | [optional] [readonly] 
**primary_color_contrast_hex** | **str** |  | [optional] 
**primary_color_hex** | **str** |  | [optional] 
**secondary_color_contrast_hex** | **str** |  | [optional] 
**secondary_color_hex** | **str** |  | [optional] 
**sign_in_page_touch_point_variant** | [**SignInPageTouchPointVariant**](SignInPageTouchPointVariant.md) |  | [optional] 
**links** | [**LinksSelf**](LinksSelf.md) |  | [optional] 

## Example

```python
from openapi_client.models.theme_response import ThemeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ThemeResponse from a JSON string
theme_response_instance = ThemeResponse.from_json(json)
# print the JSON string representation of the object
print(ThemeResponse.to_json())

# convert the object into a dict
theme_response_dict = theme_response_instance.to_dict()
# create an instance of ThemeResponse from a dict
theme_response_form_dict = theme_response.from_dict(theme_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


