# WellKnownSSFMetadata

Metadata about Okta as a transmitter and relevant information for configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_schemes** | [**List[WellKnownSSFMetadataSpecUrn]**](WellKnownSSFMetadataSpecUrn.md) | An array of JSON objects that specify the authorization scheme properties supported by the transmitter | [optional] 
**configuration_endpoint** | **str** | The URL of the SSF Stream configuration endpoint | [optional] 
**default_subjects** | **str** | A string that indicates the default behavior of newly created streams | [optional] 
**delivery_methods_supported** | **List[str]** | An array of supported SET delivery methods | [optional] 
**issuer** | **str** | The issuer used in Security Event Tokens. This value is set as &#x60;iss&#x60; in the claim. | [optional] 
**jwks_uri** | **str** | The URL of the JSON Web Key Set (JWKS) that contains the signing keys for validating the signatures of Security Event Tokens (SETs) | [optional] 
**spec_version** | **str** | The version identifying the implementer&#39;s draft or final specification implemented by the transmitter | [optional] 
**verification_endpoint** | **str** | The URL of the SSF Stream verification endpoint | [optional] 

## Example

```python
from okta.models.well_known_ssf_metadata import WellKnownSSFMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of WellKnownSSFMetadata from a JSON string
well_known_ssf_metadata_instance = WellKnownSSFMetadata.from_json(json)
# print the JSON string representation of the object
print(WellKnownSSFMetadata.to_json())

# convert the object into a dict
well_known_ssf_metadata_dict = well_known_ssf_metadata_instance.to_dict()
# create an instance of WellKnownSSFMetadata from a dict
well_known_ssf_metadata_from_dict = WellKnownSSFMetadata.from_dict(well_known_ssf_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


