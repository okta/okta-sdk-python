# CapabilitiesImportRulesUserCreateAndMatchObject

Rules for matching and creating users

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_partial_match** | **bool** | Allows user import upon partial matching. Partial matching occurs when the first and last names of an imported user match those of an existing Okta user, even if the username or email attributes don&#39;t match. | [optional] 
**auto_activate_new_users** | **bool** | If set to &#x60;true&#x60;, imported new users are automatically activated. | [optional] 
**auto_confirm_exact_match** | **bool** | If set to &#x60;true&#x60;, exact-matched users are automatically confirmed on activation. If set to &#x60;false&#x60;, exact-matched users need to be confirmed manually. | [optional] 
**auto_confirm_new_users** | **bool** | If set to &#x60;true&#x60;, imported new users are automatically confirmed on activation. This doesn&#39;t apply to imported users that already exist in Okta. | [optional] 
**auto_confirm_partial_match** | **bool** | If set to &#x60;true&#x60;, partially matched users are automatically confirmed on activation. If set to &#x60;false&#x60;, partially matched users need to be confirmed manually. | [optional] 
**exact_match_criteria** | **str** | Determines the attribute to match users | [optional] 

## Example

```python
from okta.models.capabilities_import_rules_user_create_and_match_object import CapabilitiesImportRulesUserCreateAndMatchObject

# TODO update the JSON string below
json = "{}"
# create an instance of CapabilitiesImportRulesUserCreateAndMatchObject from a JSON string
capabilities_import_rules_user_create_and_match_object_instance = CapabilitiesImportRulesUserCreateAndMatchObject.from_json(json)
# print the JSON string representation of the object
print(CapabilitiesImportRulesUserCreateAndMatchObject.to_json())

# convert the object into a dict
capabilities_import_rules_user_create_and_match_object_dict = capabilities_import_rules_user_create_and_match_object_instance.to_dict()
# create an instance of CapabilitiesImportRulesUserCreateAndMatchObject from a dict
capabilities_import_rules_user_create_and_match_object_from_dict = CapabilitiesImportRulesUserCreateAndMatchObject.from_dict(capabilities_import_rules_user_create_and_match_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


