# IdPCertificateCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x5c** | **List[str]** | Base64-encoded X.509 certificate chain with DER encoding | 

## Example

```python
from okta.models.id_p_certificate_credential import IdPCertificateCredential

# TODO update the JSON string below
json = "{}"
# create an instance of IdPCertificateCredential from a JSON string
id_p_certificate_credential_instance = IdPCertificateCredential.from_json(json)
# print the JSON string representation of the object
print(IdPCertificateCredential.to_json())

# convert the object into a dict
id_p_certificate_credential_dict = id_p_certificate_credential_instance.to_dict()
# create an instance of IdPCertificateCredential from a dict
id_p_certificate_credential_from_dict = IdPCertificateCredential.from_dict(id_p_certificate_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


