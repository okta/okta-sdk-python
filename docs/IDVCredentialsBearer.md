# IDVCredentialsBearer

Client credential for `IDV_PERSONA` IdP type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | The API key that you generate in your Persona dashboard | 

## Example

```python
from okta.models.idv_credentials_bearer import IDVCredentialsBearer

# TODO update the JSON string below
json = "{}"
# create an instance of IDVCredentialsBearer from a JSON string
idv_credentials_bearer_instance = IDVCredentialsBearer.from_json(json)
# print the JSON string representation of the object
print(IDVCredentialsBearer.to_json())

# convert the object into a dict
idv_credentials_bearer_dict = idv_credentials_bearer_instance.to_dict()
# create an instance of IDVCredentialsBearer from a dict
idv_credentials_bearer_from_dict = IDVCredentialsBearer.from_dict(idv_credentials_bearer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


