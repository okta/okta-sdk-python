# Saml11Application


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**ApplicationCredentials**](ApplicationCredentials.md) |  | [optional] 
**name** | **str** | The key name for the SAML 1.1 app definition. You can&#39;t create a custom SAML 1.1 app integration instance. Only existing OIN SAML 1.1 app integrations are supported. | 
**settings** | [**Saml11ApplicationSettings**](Saml11ApplicationSettings.md) |  | [optional] 

## Example

```python
from okta.models.saml11_application import Saml11Application

# TODO update the JSON string below
json = "{}"
# create an instance of Saml11Application from a JSON string
saml11_application_instance = Saml11Application.from_json(json)
# print the JSON string representation of the object
print(Saml11Application.to_json())

# convert the object into a dict
saml11_application_dict = saml11_application_instance.to_dict()
# create an instance of Saml11Application from a dict
saml11_application_from_dict = Saml11Application.from_dict(saml11_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


