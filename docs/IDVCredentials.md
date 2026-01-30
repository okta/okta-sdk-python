# IDVCredentials

Credentials for verifying requests to the IDV vendor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bearer** | [**IDVCredentialsBearer**](IDVCredentialsBearer.md) |  | [optional] 
**client** | [**IDVCredentialsClient**](IDVCredentialsClient.md) |  | [optional] 

## Example

```python
from okta.models.idv_credentials import IDVCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of IDVCredentials from a JSON string
idv_credentials_instance = IDVCredentials.from_json(json)
# print the JSON string representation of the object
print(IDVCredentials.to_json())

# convert the object into a dict
idv_credentials_dict = idv_credentials_instance.to_dict()
# create an instance of IDVCredentials from a dict
idv_credentials_from_dict = IDVCredentials.from_dict(idv_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


