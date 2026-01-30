# OptInStatusResponseLinksOptInStatus


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
from okta.models.opt_in_status_response_links_opt_in_status import OptInStatusResponseLinksOptInStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OptInStatusResponseLinksOptInStatus from a JSON string
opt_in_status_response_links_opt_in_status_instance = OptInStatusResponseLinksOptInStatus.from_json(json)
# print the JSON string representation of the object
print(OptInStatusResponseLinksOptInStatus.to_json())

# convert the object into a dict
opt_in_status_response_links_opt_in_status_dict = opt_in_status_response_links_opt_in_status_instance.to_dict()
# create an instance of OptInStatusResponseLinksOptInStatus from a dict
opt_in_status_response_links_opt_in_status_from_dict = OptInStatusResponseLinksOptInStatus.from_dict(opt_in_status_response_links_opt_in_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


