# IdentitySourceUserProfileForUpsert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**home_address** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**mobile_phone** | **str** |  | [optional] 
**second_email** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 

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


