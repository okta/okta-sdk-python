# MtlsCredentials

Certificate chain description for verifying assertions from the Smart Card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trust** | [**MtlsTrustCredentials**](MtlsTrustCredentials.md) |  | [optional] 

## Example

```python
from okta.models.mtls_credentials import MtlsCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of MtlsCredentials from a JSON string
mtls_credentials_instance = MtlsCredentials.from_json(json)
# print the JSON string representation of the object
print(MtlsCredentials.to_json())

# convert the object into a dict
mtls_credentials_dict = mtls_credentials_instance.to_dict()
# create an instance of MtlsCredentials from a dict
mtls_credentials_from_dict = MtlsCredentials.from_dict(mtls_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


