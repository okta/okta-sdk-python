# SamlApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**ApplicationCredentials**](ApplicationCredentials.md) |  | [optional] 
**name** | **str** |  | [optional] 
**settings** | [**SamlApplicationSettings**](SamlApplicationSettings.md) |  | [optional] 

## Example

```python
from openapi_client.models.saml_application import SamlApplication

# TODO update the JSON string below
json = "{}"
# create an instance of SamlApplication from a JSON string
saml_application_instance = SamlApplication.from_json(json)
# print the JSON string representation of the object
print(SamlApplication.to_json())

# convert the object into a dict
saml_application_dict = saml_application_instance.to_dict()
# create an instance of SamlApplication from a dict
saml_application_form_dict = saml_application.from_dict(saml_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


