# CsrMetadataSubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**locality_name** | **str** |  | [optional] 
**organizational_unit_name** | **str** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**state_or_province_name** | **str** |  | [optional] 

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


