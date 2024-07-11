# CsrMetadataSubjectAltNames


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_names** | **List[str]** |  | [optional] 

## Example

```python
from okta.models.csr_metadata_subject_alt_names import CsrMetadataSubjectAltNames

# TODO update the JSON string below
json = "{}"
# create an instance of CsrMetadataSubjectAltNames from a JSON string
csr_metadata_subject_alt_names_instance = CsrMetadataSubjectAltNames.from_json(json)
# print the JSON string representation of the object
print(CsrMetadataSubjectAltNames.to_json())

# convert the object into a dict
csr_metadata_subject_alt_names_dict = csr_metadata_subject_alt_names_instance.to_dict()
# create an instance of CsrMetadataSubjectAltNames from a dict
csr_metadata_subject_alt_names_from_dict = CsrMetadataSubjectAltNames.from_dict(csr_metadata_subject_alt_names_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


