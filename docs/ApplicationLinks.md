# ApplicationLinks

Discoverable resources related to the app

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_policy** | [**AccessPolicyLink**](AccessPolicyLink.md) |  | [optional] 
**activate** | [**HrefObjectActivateLink**](HrefObjectActivateLink.md) |  | [optional] 
**app_links** | [**List[HrefObject]**](HrefObject.md) | List of app link resources | [optional] 
**deactivate** | [**HrefObjectDeactivateLink**](HrefObjectDeactivateLink.md) |  | [optional] 
**groups** | [**GroupsLink**](GroupsLink.md) |  | [optional] 
**help** | [**HelpLink**](HelpLink.md) |  | [optional] 
**logo** | [**List[HrefObject]**](HrefObject.md) | List of app logo resources | [optional] 
**metadata** | [**MetadataLink**](MetadataLink.md) |  | [optional] 
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**users** | [**UsersLink**](UsersLink.md) |  | [optional] 

## Example

```python
from okta.models.application_links import ApplicationLinks

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationLinks from a JSON string
application_links_instance = ApplicationLinks.from_json(json)
# print the JSON string representation of the object
print(ApplicationLinks.to_json())

# convert the object into a dict
application_links_dict = application_links_instance.to_dict()
# create an instance of ApplicationLinks from a dict
application_links_from_dict = ApplicationLinks.from_dict(application_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


