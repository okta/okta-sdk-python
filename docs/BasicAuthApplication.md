# BasicAuthApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**SchemeApplicationCredentials**](SchemeApplicationCredentials.md) |  | [optional] 
**name** | **str** | &#x60;template_basic_auth&#x60; is the key name for a Basic Authentication scheme app instance | 
**settings** | [**BasicApplicationSettings**](BasicApplicationSettings.md) |  | 

## Example

```python
from okta.models.basic_auth_application import BasicAuthApplication

# TODO update the JSON string below
json = "{}"
# create an instance of BasicAuthApplication from a JSON string
basic_auth_application_instance = BasicAuthApplication.from_json(json)
# print the JSON string representation of the object
print(BasicAuthApplication.to_json())

# convert the object into a dict
basic_auth_application_dict = basic_auth_application_instance.to_dict()
# create an instance of BasicAuthApplication from a dict
basic_auth_application_from_dict = BasicAuthApplication.from_dict(basic_auth_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


