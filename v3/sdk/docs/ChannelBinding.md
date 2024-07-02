# ChannelBinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | [**RequiredEnum**](RequiredEnum.md) |  | [optional] 
**style** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.channel_binding import ChannelBinding

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelBinding from a JSON string
channel_binding_instance = ChannelBinding.from_json(json)
# print the JSON string representation of the object
print(ChannelBinding.to_json())

# convert the object into a dict
channel_binding_dict = channel_binding_instance.to_dict()
# create an instance of ChannelBinding from a dict
channel_binding_from_dict = ChannelBinding.from_dict(channel_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


