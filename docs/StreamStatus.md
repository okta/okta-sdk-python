# StreamStatus

Status corresponding to the `stream_id` of the SSF Stream

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the SSF Stream configuration | [optional] 
**stream_id** | **str** | The ID of the SSF Stream configuration. This corresponds to the value in the query parameter of the request. | [optional] 

## Example

```python
from okta.models.stream_status import StreamStatus

# TODO update the JSON string below
json = "{}"
# create an instance of StreamStatus from a JSON string
stream_status_instance = StreamStatus.from_json(json)
# print the JSON string representation of the object
print(StreamStatus.to_json())

# convert the object into a dict
stream_status_dict = stream_status_instance.to_dict()
# create an instance of StreamStatus from a dict
stream_status_from_dict = StreamStatus.from_dict(stream_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


