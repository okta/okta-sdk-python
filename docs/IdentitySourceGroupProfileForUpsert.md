# IdentitySourceGroupProfileForUpsert

Contains a set of external group attributes and their values that are mapped to Okta standard properties. See the group [`profile` object](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Group/#tag/Group/operation/getGroup!c=200&path=profile&t=response) and Declaration of a Custom Identity Source Schema in [Using anything as a source](https://help.okta.com/okta_help.htm?type=oie&id=ext-anything-as-a-source). > **Note:** Profile attributes can only be of the string type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the group | [optional] 
**display_name** | **str** | Name of the group | [optional] 

## Example

```python
from okta.models.identity_source_group_profile_for_upsert import IdentitySourceGroupProfileForUpsert

# TODO update the JSON string below
json = "{}"
# create an instance of IdentitySourceGroupProfileForUpsert from a JSON string
identity_source_group_profile_for_upsert_instance = IdentitySourceGroupProfileForUpsert.from_json(json)
# print the JSON string representation of the object
print(IdentitySourceGroupProfileForUpsert.to_json())

# convert the object into a dict
identity_source_group_profile_for_upsert_dict = identity_source_group_profile_for_upsert_instance.to_dict()
# create an instance of IdentitySourceGroupProfileForUpsert from a dict
identity_source_group_profile_for_upsert_from_dict = IdentitySourceGroupProfileForUpsert.from_dict(identity_source_group_profile_for_upsert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


