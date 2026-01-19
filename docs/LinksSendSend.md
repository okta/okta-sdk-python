# LinksSendSend


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hints** | [**HrefHints**](HrefHints.md) |  | [optional] 
**href** | **str** | Link URI | 
**name** | **str** | Link name | [optional] [readonly] 
**templated** | **bool** | Indicates whether the link object&#39;s &#x60;href&#x60; property is a URI template. | [optional] [readonly] 
**type** | **str** | The media type of the link. If omitted, it is implicitly &#x60;application/json&#x60;. | [optional] [readonly] 

## Example

```python
from okta.models.links_send_send import LinksSendSend

# TODO update the JSON string below
json = "{}"
# create an instance of LinksSendSend from a JSON string
links_send_send_instance = LinksSendSend.from_json(json)
# print the JSON string representation of the object
print(LinksSendSend.to_json())

# convert the object into a dict
links_send_send_dict = links_send_send_instance.to_dict()
# create an instance of LinksSendSend from a dict
links_send_send_from_dict = LinksSendSend.from_dict(links_send_send_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


