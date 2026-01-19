# IdentitySourceUserProfileForUpsert

Contains a set of external user attributes and their values that are mapped to Okta standard and custom profile properties. See the [`profile` object](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/User/#tag/User/operation/getUser!c=200&path=profile&t=response) and Declaration of a Custom Identity Source Schema in [Using anything as a source](https://help.okta.com/okta_help.htm?type=oie&id=ext-anything-as-a-source). > **Note:** Profile attributes can only be of the string type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address of the user | [optional] 
**first_name** | **str** | First name of the user | [optional] 
**home_address** | **str** | Home address of the user | [optional] 
**last_name** | **str** | Last name of the user | [optional] 
**mobile_phone** | **str** | Mobile phone number of the user | [optional] 
**second_email** | **str** | Alternative email address of the user | [optional] 
**user_name** | **str** | Username of the user | [optional] 

## Example

```python
from okta.models.identity_source_user_profile_for_upsert import IdentitySourceUserProfileForUpsert

# TODO update the JSON string below
json = "{}"
# create an instance of IdentitySourceUserProfileForUpsert from a JSON string
identity_source_user_profile_for_upsert_instance = IdentitySourceUserProfileForUpsert.from_json(json)
# print the JSON string representation of the object
print(IdentitySourceUserProfileForUpsert.to_json())

# convert the object into a dict
identity_source_user_profile_for_upsert_dict = identity_source_user_profile_for_upsert_instance.to_dict()
# create an instance of IdentitySourceUserProfileForUpsert from a dict
identity_source_user_profile_for_upsert_from_dict = IdentitySourceUserProfileForUpsert.from_dict(identity_source_user_profile_for_upsert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


