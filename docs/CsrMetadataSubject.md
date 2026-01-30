# CsrMetadataSubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | Common name of the subject | [optional] 
**country_name** | **str** | Country name or code | [optional] 
**locality_name** | **str** | Locality (city) name | [optional] 
**organizational_unit_name** | **str** | Name of the smaller organization, for example, the department or the division | [optional] 
**organization_name** | **str** | Large organization name | [optional] 
**state_or_province_name** | **str** | State or province name | [optional] 

## Example

```python
from okta.models.csr_metadata_subject import CsrMetadataSubject

# TODO update the JSON string below
json = "{}"
# create an instance of CsrMetadataSubject from a JSON string
csr_metadata_subject_instance = CsrMetadataSubject.from_json(json)
# print the JSON string representation of the object
print(CsrMetadataSubject.to_json())

# convert the object into a dict
csr_metadata_subject_dict = csr_metadata_subject_instance.to_dict()
# create an instance of CsrMetadataSubject from a dict
csr_metadata_subject_from_dict = CsrMetadataSubject.from_dict(csr_metadata_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


