# BrowserPluginApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**SchemeApplicationCredentials**](SchemeApplicationCredentials.md) |  | [optional] 
**name** | **str** | The key name for the app definition | 
**settings** | [**SwaApplicationSettings**](SwaApplicationSettings.md) |  | 

## Example

```python
from okta.models.browser_plugin_application import BrowserPluginApplication

# TODO update the JSON string below
json = "{}"
# create an instance of BrowserPluginApplication from a JSON string
browser_plugin_application_instance = BrowserPluginApplication.from_json(json)
# print the JSON string representation of the object
print(BrowserPluginApplication.to_json())

# convert the object into a dict
browser_plugin_application_dict = browser_plugin_application_instance.to_dict()
# create an instance of BrowserPluginApplication from a dict
browser_plugin_application_from_dict = BrowserPluginApplication.from_dict(browser_plugin_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


