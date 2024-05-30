# SpCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x5c** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.sp_certificate import SpCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of SpCertificate from a JSON string
sp_certificate_instance = SpCertificate.from_json(json)
# print the JSON string representation of the object
print(SpCertificate.to_json())

# convert the object into a dict
sp_certificate_dict = sp_certificate_instance.to_dict()
# create an instance of SpCertificate from a dict
sp_certificate_form_dict = sp_certificate.from_dict(sp_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


