# AppAccountContainerLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | [**HrefObjectAppLink**](HrefObjectAppLink.md) |  | [optional] 
**logo** | [**HrefObjectLogoLink**](HrefObjectLogoLink.md) |  | [optional] 

## Example

```python
from okta.models.app_account_container_link import AppAccountContainerLink

# TODO update the JSON string below
json = "{}"
# create an instance of AppAccountContainerLink from a JSON string
app_account_container_link_instance = AppAccountContainerLink.from_json(json)
# print the JSON string representation of the object
print(AppAccountContainerLink.to_json())

# convert the object into a dict
app_account_container_link_dict = app_account_container_link_instance.to_dict()
# create an instance of AppAccountContainerLink from a dict
app_account_container_link_from_dict = AppAccountContainerLink.from_dict(app_account_container_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


