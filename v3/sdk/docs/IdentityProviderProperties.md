# IdentityProviderProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_amr** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.identity_provider_properties import IdentityProviderProperties

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityProviderProperties from a JSON string
identity_provider_properties_instance = IdentityProviderProperties.from_json(json)
# print the JSON string representation of the object
print(IdentityProviderProperties.to_json())

# convert the object into a dict
identity_provider_properties_dict = identity_provider_properties_instance.to_dict()
# create an instance of IdentityProviderProperties from a dict
identity_provider_properties_form_dict = identity_provider_properties.from_dict(identity_provider_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


