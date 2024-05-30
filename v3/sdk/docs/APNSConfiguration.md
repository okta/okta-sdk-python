# APNSConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | (Optional) File name for Admin Console display | [optional] 
**key_id** | **str** | 10-character Key ID obtained from the Apple developer account | [optional] 
**team_id** | **str** | 10-character Team ID used to develop the iOS app | [optional] 
**token_signing_key** | **str** | APNs private authentication token signing key | [optional] 

## Example

```python
from openapi_client.models.apns_configuration import APNSConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of APNSConfiguration from a JSON string
apns_configuration_instance = APNSConfiguration.from_json(json)
# print the JSON string representation of the object
print(APNSConfiguration.to_json())

# convert the object into a dict
apns_configuration_dict = apns_configuration_instance.to_dict()
# create an instance of APNSConfiguration from a dict
apns_configuration_form_dict = apns_configuration.from_dict(apns_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


