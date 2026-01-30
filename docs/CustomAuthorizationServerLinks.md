# CustomAuthorizationServerLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObject**](HrefObject.md) |  | 
**web** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from okta.models.custom_authorization_server_links import CustomAuthorizationServerLinks

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAuthorizationServerLinks from a JSON string
custom_authorization_server_links_instance = CustomAuthorizationServerLinks.from_json(json)
# print the JSON string representation of the object
print(CustomAuthorizationServerLinks.to_json())

# convert the object into a dict
custom_authorization_server_links_dict = custom_authorization_server_links_instance.to_dict()
# create an instance of CustomAuthorizationServerLinks from a dict
custom_authorization_server_links_from_dict = CustomAuthorizationServerLinks.from_dict(custom_authorization_server_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


