# PostAuthKeepMeSignedInPrompt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_button_text** | **str** | The label on the accept button when prompting for Stay signed in | [optional] 
**reject_button_text** | **str** | The label on the reject button when prompting for Stay signed in | [optional] 
**subtitle** | **str** | The subtitle on the Sign-In Widget when prompting for Stay signed in | [optional] 
**title** | **str** | The title on the Sign-In Widget when prompting for Stay signed in | [optional] 

## Example

```python
from okta.models.post_auth_keep_me_signed_in_prompt import PostAuthKeepMeSignedInPrompt

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthKeepMeSignedInPrompt from a JSON string
post_auth_keep_me_signed_in_prompt_instance = PostAuthKeepMeSignedInPrompt.from_json(json)
# print the JSON string representation of the object
print(PostAuthKeepMeSignedInPrompt.to_json())

# convert the object into a dict
post_auth_keep_me_signed_in_prompt_dict = post_auth_keep_me_signed_in_prompt_instance.to_dict()
# create an instance of PostAuthKeepMeSignedInPrompt from a dict
post_auth_keep_me_signed_in_prompt_from_dict = PostAuthKeepMeSignedInPrompt.from_dict(post_auth_keep_me_signed_in_prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


