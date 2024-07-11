# WsFederationApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**ApplicationCredentials**](ApplicationCredentials.md) |  | [optional] 
**name** | **str** |  | [optional] [default to 'template_wsfed']
**settings** | [**WsFederationApplicationSettings**](WsFederationApplicationSettings.md) |  | [optional] 

## Example

```python
from okta.models.ws_federation_application import WsFederationApplication

# TODO update the JSON string below
json = "{}"
# create an instance of WsFederationApplication from a JSON string
ws_federation_application_instance = WsFederationApplication.from_json(json)
# print the JSON string representation of the object
print(WsFederationApplication.to_json())

# convert the object into a dict
ws_federation_application_dict = ws_federation_application_instance.to_dict()
# create an instance of WsFederationApplication from a dict
ws_federation_application_from_dict = WsFederationApplication.from_dict(ws_federation_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


