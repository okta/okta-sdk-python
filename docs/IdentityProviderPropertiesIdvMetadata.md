# IdentityProviderPropertiesIdvMetadata

Metadata about the IDV vendor. Available only for `IDV_STANDARD` IdPs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_display_name** | **str** | The display name of the IDV vendor | [optional] 
**terms_of_use** | **str** | A URL that links to the terms of use for the IDV vendor | [optional] 
**privacy_policy** | **str** | A URL that links to the privacy policy for the IDV vendor | [optional] 

## Example

```python
from okta.models.identity_provider_properties_idv_metadata import IdentityProviderPropertiesIdvMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderPropertiesIdvMetadata from a JSON string
identity_provider_properties_idv_metadata_instance = IdentityProviderPropertiesIdvMetadata.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderPropertiesIdvMetadata.to_json())

# convert the object into a dict
identity_provider_properties_idv_metadata_dict = identity_provider_properties_idv_metadata_instance.to_dict()
# create an instance of IdentityProviderPropertiesIdvMetadata from a dict
identity_provider_properties_idv_metadata_from_dict = IdentityProviderPropertiesIdvMetadata.from_dict(identity_provider_properties_idv_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


