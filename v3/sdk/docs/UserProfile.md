# UserProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**cost_center** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**division** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**employee_number** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**honorific_prefix** | **str** |  | [optional] 
**honorific_suffix** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**locale** | **str** | The language specified as an [IETF BCP 47 language tag](https://datatracker.ietf.org/doc/html/rfc5646) | [optional] 
**login** | **str** |  | [optional] 
**manager** | **str** |  | [optional] 
**manager_id** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**mobile_phone** | **str** |  | [optional] 
**nick_name** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**postal_address** | **str** |  | [optional] 
**preferred_language** | **str** |  | [optional] 
**primary_phone** | **str** |  | [optional] 
**profile_url** | **str** |  | [optional] 
**second_email** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**street_address** | **str** |  | [optional] 
**timezone** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**user_type** | **str** |  | [optional] 
**zip_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.user_profile import UserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of UserProfile from a JSON string
user_profile_instance = UserProfile.from_json(json)
# print the JSON string representation of the object
print(UserProfile.to_json())

# convert the object into a dict
user_profile_dict = user_profile_instance.to_dict()
# create an instance of UserProfile from a dict
user_profile_form_dict = user_profile.from_dict(user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


