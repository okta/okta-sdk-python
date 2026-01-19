# EventHookFilters

The optional filter defined on a specific event type  > **Note:** Event hook filters is a [self-service Early Access (EA)](/openapi/okta-management/guides/release-lifecycle/#early-access-ea) to enable. If you want to disable this feature, it's recommended to first remove all event filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_filter_map** | [**List[EventHookFilterMapObject]**](EventHookFilterMapObject.md) | The object that maps the filter to the event type | [optional] 
**type** | **str** | The type of filter. Currently only supports &#x60;EXPRESSION_LANGUAGE&#x60; | [optional] [readonly] 

## Example

```python
from okta.models.event_hook_filters import EventHookFilters

# TODO update the JSON string below
json = "{}"
# create an instance of EventHookFilters from a JSON string
event_hook_filters_instance = EventHookFilters.from_json(json)
# print the JSON string representation of the object
print(EventHookFilters.to_json())

# convert the object into a dict
event_hook_filters_dict = event_hook_filters_instance.to_dict()
# create an instance of EventHookFilters from a dict
event_hook_filters_from_dict = EventHookFilters.from_dict(event_hook_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


