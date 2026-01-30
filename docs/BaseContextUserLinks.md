# BaseContextUserLinks

Specifies link relations (see [Web Linking](https://www.rfc-editor.org/rfc/rfc8288)) available for the current status of the user. These links are used to discover what groups the user is a part of and what factors they have enrolled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**HrefObject**](HrefObject.md) | URL to retrieve the individual user&#39;s group memberships | [optional] 
**factors** | [**HrefObject**](HrefObject.md) | URL to retrieve individual user&#39;s factor enrollments | [optional] 

## Example

```python
from okta.models.base_context_user_links import BaseContextUserLinks

# TODO update the JSON string below
json = "{}"
# create an instance of BaseContextUserLinks from a JSON string
base_context_user_links_instance = BaseContextUserLinks.from_json(json)
# print the JSON string representation of the object
print(BaseContextUserLinks.to_json())

# convert the object into a dict
base_context_user_links_dict = base_context_user_links_instance.to_dict()
# create an instance of BaseContextUserLinks from a dict
base_context_user_links_from_dict = BaseContextUserLinks.from_dict(base_context_user_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


