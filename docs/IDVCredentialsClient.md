# IDVCredentialsClient

<x-lifecycle-container><x-lifecycle class=\"oie\"></x-lifecycle></x-lifecycle-container>Client credentials for `IDV_CLEAR` and `IDV_INCODE` IdP types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | The client ID that you generate in your IDV vendor | 
**client_secret** | **str** | The client secret that you generate in your IDV vendor | 

## Example

```python
from okta.models.idv_credentials_client import IDVCredentialsClient

# TODO update the JSON string below
json = "{}"
# create an instance of IDVCredentialsClient from a JSON string
idv_credentials_client_instance = IDVCredentialsClient.from_json(json)
# print the JSON string representation of the object
print(IDVCredentialsClient.to_json())

# convert the object into a dict
idv_credentials_client_dict = idv_credentials_client_instance.to_dict()
# create an instance of IDVCredentialsClient from a dict
idv_credentials_client_from_dict = IDVCredentialsClient.from_dict(idv_credentials_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


