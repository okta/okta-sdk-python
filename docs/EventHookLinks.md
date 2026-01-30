# EventHookLinks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**deactivate** | [**HrefObject**](HrefObject.md) |  | [optional] 
**verify** | [**HrefObject**](HrefObject.md) |  | [optional] 

## Example

```python
from okta.models.event_hook_links import EventHookLinks

# TODO update the JSON string below
json = "{}"
# create an instance of EventHookLinks from a JSON string
event_hook_links_instance = EventHookLinks.from_json(json)
# print the JSON string representation of the object
print(EventHookLinks.to_json())

# convert the object into a dict
event_hook_links_dict = event_hook_links_instance.to_dict()
# create an instance of EventHookLinks from a dict
event_hook_links_from_dict = EventHookLinks.from_dict(event_hook_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


