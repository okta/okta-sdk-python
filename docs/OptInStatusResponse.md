# OptInStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opt_in_status** | **str** | The entitlement management opt-in status for the Admin Console | [optional] 
**links** | [**OptInStatusResponseLinks**](OptInStatusResponseLinks.md) |  | [optional] 

## Example

```python
from okta.models.opt_in_status_response import OptInStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OptInStatusResponse from a JSON string
opt_in_status_response_instance = OptInStatusResponse.from_json(json)
# print the JSON string representation of the object
print(OptInStatusResponse.to_json())

# convert the object into a dict
opt_in_status_response_dict = opt_in_status_response_instance.to_dict()
# create an instance of OptInStatusResponse from a dict
opt_in_status_response_from_dict = OptInStatusResponse.from_dict(opt_in_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


