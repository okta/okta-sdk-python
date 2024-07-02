# SignInPageAllOfWidgetCustomizations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_in_label** | **str** |  | [optional] 
**username_label** | **str** |  | [optional] 
**username_info_tip** | **str** |  | [optional] 
**password_label** | **str** |  | [optional] 
**password_info_tip** | **str** |  | [optional] 
**show_password_visibility_toggle** | **bool** |  | [optional] 
**show_user_identifier** | **bool** |  | [optional] 
**forgot_password_label** | **str** |  | [optional] 
**forgot_password_url** | **str** |  | [optional] 
**unlock_account_label** | **str** |  | [optional] 
**unlock_account_url** | **str** |  | [optional] 
**help_label** | **str** |  | [optional] 
**help_url** | **str** |  | [optional] 
**custom_link1_label** | **str** |  | [optional] 
**custom_link1_url** | **str** |  | [optional] 
**custom_link2_label** | **str** |  | [optional] 
**custom_link2_url** | **str** |  | [optional] 
**authenticator_page_custom_link_label** | **str** |  | [optional] 
**authenticator_page_custom_link_url** | **str** |  | [optional] 
**classic_recovery_flow_email_or_username_label** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.sign_in_page_all_of_widget_customizations import SignInPageAllOfWidgetCustomizations

# TODO update the JSON string below
json = "{}"
# create an instance of SignInPageAllOfWidgetCustomizations from a JSON string
sign_in_page_all_of_widget_customizations_instance = SignInPageAllOfWidgetCustomizations.from_json(json)
# print the JSON string representation of the object
print(SignInPageAllOfWidgetCustomizations.to_json())

# convert the object into a dict
sign_in_page_all_of_widget_customizations_dict = sign_in_page_all_of_widget_customizations_instance.to_dict()
# create an instance of SignInPageAllOfWidgetCustomizations from a dict
sign_in_page_all_of_widget_customizations_from_dict = SignInPageAllOfWidgetCustomizations.from_dict(sign_in_page_all_of_widget_customizations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


