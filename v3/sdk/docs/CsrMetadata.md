# CsrMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | [**CsrMetadataSubject**](CsrMetadataSubject.md) |  | [optional] 
**subject_alt_names** | [**CsrMetadataSubjectAltNames**](CsrMetadataSubjectAltNames.md) |  | [optional] 

## Example

```python
from openapi_client.models.csr_metadata import CsrMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CsrMetadata from a JSON string
csr_metadata_instance = CsrMetadata.from_json(json)
# print the JSON string representation of the object
print(CsrMetadata.to_json())

# convert the object into a dict
csr_metadata_dict = csr_metadata_instance.to_dict()
# create an instance of CsrMetadata from a dict
csr_metadata_form_dict = csr_metadata.from_dict(csr_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


