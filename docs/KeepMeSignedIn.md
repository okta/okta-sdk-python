# KeepMeSignedIn

<x-lifecycle-container><x-lifecycle class=\"oie\"></x-lifecycle></x-lifecycle-container>Controls how often the post-authentication prompt is presented to users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**post_auth** | **str** | Whether the post-authentication [Keep Me Signed In (KMSI)](https://help.okta.com/oie/en-us/content/topics/security/stay-signed-in.htm) flow is allowed | [optional] 
**post_auth_prompt_frequency** | **str** | A time duration specified as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations). | [optional] 

## Example

```python
from okta.models.keep_me_signed_in import KeepMeSignedIn

# TODO update the JSON string below
json = "{}"
# create an instance of KeepMeSignedIn from a JSON string
keep_me_signed_in_instance = KeepMeSignedIn.from_json(json)
# print the JSON string representation of the object
print(KeepMeSignedIn.to_json())

# convert the object into a dict
keep_me_signed_in_dict = keep_me_signed_in_instance.to_dict()
# create an instance of KeepMeSignedIn from a dict
keep_me_signed_in_from_dict = KeepMeSignedIn.from_dict(keep_me_signed_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


