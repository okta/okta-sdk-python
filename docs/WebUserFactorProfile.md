# WebUserFactorProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** |  | [optional] 

## Example

```python
from okta.models.web_user_factor_profile import WebUserFactorProfile

# TODO update the JSON string below
json = "{}"
# create an instance of WebUserFactorProfile from a JSON string
web_user_factor_profile_instance = WebUserFactorProfile.from_json(json)
# print the JSON string representation of the object
print(WebUserFactorProfile.to_json())

# convert the object into a dict
web_user_factor_profile_dict = web_user_factor_profile_instance.to_dict()
# create an instance of WebUserFactorProfile from a dict
web_user_factor_profile_from_dict = WebUserFactorProfile.from_dict(web_user_factor_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


