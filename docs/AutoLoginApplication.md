# AutoLoginApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**SchemeApplicationCredentials**](SchemeApplicationCredentials.md) |  | [optional] 
**name** | **str** | A unique key is generated for the custom SWA app instance when you use AUTO_LOGIN &#x60;signOnMode&#x60;. | [optional] [readonly] 
**settings** | [**AutoLoginApplicationSettings**](AutoLoginApplicationSettings.md) |  | [optional] 

## Example

```python
from okta.models.auto_login_application import AutoLoginApplication

# TODO update the JSON string below
json = "{}"
# create an instance of AutoLoginApplication from a JSON string
auto_login_application_instance = AutoLoginApplication.from_json(json)
# print the JSON string representation of the object
print(AutoLoginApplication.to_json())

# convert the object into a dict
auto_login_application_dict = auto_login_application_instance.to_dict()
# create an instance of AutoLoginApplication from a dict
auto_login_application_from_dict = AutoLoginApplication.from_dict(auto_login_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


