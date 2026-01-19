# OptInStatusResponseLinks

Link relations available

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opt_in_status** | [**OptInStatusResponseLinksOptInStatus**](OptInStatusResponseLinksOptInStatus.md) |  | [optional] 

## Example

```python
from okta.models.opt_in_status_response_links import OptInStatusResponseLinks

# TODO update the JSON string below
json = "{}"
# create an instance of OptInStatusResponseLinks from a JSON string
opt_in_status_response_links_instance = OptInStatusResponseLinks.from_json(json)
# print the JSON string representation of the object
print(OptInStatusResponseLinks.to_json())

# convert the object into a dict
opt_in_status_response_links_dict = opt_in_status_response_links_instance.to_dict()
# create an instance of OptInStatusResponseLinks from a dict
opt_in_status_response_links_from_dict = OptInStatusResponseLinks.from_dict(opt_in_status_response_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


