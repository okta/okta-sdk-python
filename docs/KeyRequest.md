# KeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name for the key | [optional] 

## Example

```python
from okta.models.key_request import KeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KeyRequest from a JSON string
key_request_instance = KeyRequest.from_json(json)
# print the JSON string representation of the object
print(KeyRequest.to_json())

# convert the object into a dict
key_request_dict = key_request_instance.to_dict()
# create an instance of KeyRequest from a dict
key_request_from_dict = KeyRequest.from_dict(key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


