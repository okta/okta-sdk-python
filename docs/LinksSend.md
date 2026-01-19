# LinksSend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**send** | [**LinksSendSend**](LinksSendSend.md) |  | [optional] 

## Example

```python
from okta.models.links_send import LinksSend

# TODO update the JSON string below
json = "{}"
# create an instance of LinksSend from a JSON string
links_send_instance = LinksSend.from_json(json)
# print the JSON string representation of the object
print(LinksSend.to_json())

# convert the object into a dict
links_send_dict = links_send_instance.to_dict()
# create an instance of LinksSend from a dict
links_send_from_dict = LinksSend.from_dict(links_send_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


