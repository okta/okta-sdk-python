# LinksPoll


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**poll** | [**LinksPollPoll**](LinksPollPoll.md) |  | [optional] 

## Example

```python
from okta.models.links_poll import LinksPoll

# TODO update the JSON string below
json = "{}"
# create an instance of LinksPoll from a JSON string
links_poll_instance = LinksPoll.from_json(json)
# print the JSON string representation of the object
print(LinksPoll.to_json())

# convert the object into a dict
links_poll_dict = links_poll_instance.to_dict()
# create an instance of LinksPoll from a dict
links_poll_from_dict = LinksPoll.from_dict(links_poll_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


