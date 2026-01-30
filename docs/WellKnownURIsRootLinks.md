# WellKnownURIsRootLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**apple_app_site_association** | [**HrefObject**](HrefObject.md) |  | [optional] 
**assetlinks_json** | [**HrefObject**](HrefObject.md) |  | [optional] 
**webauthn** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from okta.models.well_known_uris_root_links import WellKnownURIsRootLinks

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownURIsRootLinks from a JSON string
well_known_uris_root_links_instance = WellKnownURIsRootLinks.from_json(json)
# print the JSON string representation of the object
print(WellKnownURIsRootLinks.to_json())

# convert the object into a dict
well_known_uris_root_links_dict = well_known_uris_root_links_instance.to_dict()
# create an instance of WellKnownURIsRootLinks from a dict
well_known_uris_root_links_from_dict = WellKnownURIsRootLinks.from_dict(well_known_uris_root_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


