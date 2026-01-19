# WellKnownURIsRootEmbedded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apple_app_site_association** | [**WellKnownURIsRootEmbeddedAppleAppSiteAssociation**](WellKnownURIsRootEmbeddedAppleAppSiteAssociation.md) |  | [optional] 
**assetlinks_json** | [**WellKnownURIsRootEmbeddedAssetlinksJson**](WellKnownURIsRootEmbeddedAssetlinksJson.md) |  | [optional] 
**webauthn** | [**WellKnownURIsRootEmbeddedAppleAppSiteAssociation**](WellKnownURIsRootEmbeddedAppleAppSiteAssociation.md) |  | [optional] 

## Example

```python
from okta.models.well_known_uris_root_embedded import WellKnownURIsRootEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownURIsRootEmbedded from a JSON string
well_known_uris_root_embedded_instance = WellKnownURIsRootEmbedded.from_json(json)
# print the JSON string representation of the object
print(WellKnownURIsRootEmbedded.to_json())

# convert the object into a dict
well_known_uris_root_embedded_dict = well_known_uris_root_embedded_instance.to_dict()
# create an instance of WellKnownURIsRootEmbedded from a dict
well_known_uris_root_embedded_from_dict = WellKnownURIsRootEmbedded.from_dict(well_known_uris_root_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


