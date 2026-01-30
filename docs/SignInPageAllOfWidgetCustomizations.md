# SignInPageAllOfWidgetCustomizations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sign_in_label** | **str** | The label for the sign in widget | [optional] 
**username_label** | **str** | The label for the username field | [optional] 
**username_info_tip** | **str** | The label for the username information tip | [optional] 
**password_label** | **str** | The label for the password field | [optional] 
**password_info_tip** | **str** | The label for the password information tip | [optional] 
**show_password_visibility_toggle** | **bool** | Allows users to see their passwords as they type | [optional] 
**show_user_identifier** | **bool** | Allows the user&#39;s identifier to appear on authentication and enrollment pages | [optional] 
**forgot_password_label** | **str** | The label for the forgot password page | [optional] 
**forgot_password_url** | **str** | The forgot password URL | [optional] 
**unlock_account_label** | **str** | The label for the unlock account link | [optional] 
**unlock_account_url** | **str** | The unlock account URL | [optional] 
**help_label** | **str** | The label for the help link | [optional] 
**help_url** | **str** | The help link URL | [optional] 
**custom_link1_label** | **str** | The label for the first custom link | [optional] 
**custom_link1_url** | **str** | The URL for the first custom link | [optional] 
**custom_link2_label** | **str** | The label for the second custom link | [optional] 
**custom_link2_url** | **str** | The URL for the second custom link | [optional] 
**authenticator_page_custom_link_label** | **str** | The label for the authenticator page custom link | [optional] 
**authenticator_page_custom_link_url** | **str** | The URL for the authenticator page custom link | [optional] 
**classic_recovery_flow_email_or_username_label** | **str** | The label for the username field in the classic recovery flow | [optional] 
**widget_generation** | [**WidgetGeneration**](WidgetGeneration.md) |  | [optional] 
**post_auth_keep_me_signed_in_prompt** | [**PostAuthKeepMeSignedInPrompt**](PostAuthKeepMeSignedInPrompt.md) |  | [optional] 
**classic_footer_help_title** | **str** | The title of the footer link on the sign-in page. Only applicable for Classic Engine orgs. | [optional] 

## Example

```python
from okta.models.sign_in_page_all_of_widget_customizations import SignInPageAllOfWidgetCustomizations

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


