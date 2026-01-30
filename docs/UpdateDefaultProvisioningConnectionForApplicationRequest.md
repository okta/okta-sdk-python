# UpdateDefaultProvisioningConnectionForApplicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** | Only used for the Zscaler 2.0 (&#x60;zscalerbyz&#x60;) app. The base URL for the Zscaler 2.0 target app, which also contains the Zscaler ID. | [optional] 
**profile** | [**ProvisioningConnectionOauthRequestProfile**](ProvisioningConnectionOauthRequestProfile.md) |  | 

## Example

```python
from okta.models.update_default_provisioning_connection_for_application_request import UpdateDefaultProvisioningConnectionForApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDefaultProvisioningConnectionForApplicationRequest from a JSON string
update_default_provisioning_connection_for_application_request_instance = UpdateDefaultProvisioningConnectionForApplicationRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDefaultProvisioningConnectionForApplicationRequest.to_json())

# convert the object into a dict
update_default_provisioning_connection_for_application_request_dict = update_default_provisioning_connection_for_application_request_instance.to_dict()
# create an instance of UpdateDefaultProvisioningConnectionForApplicationRequest from a dict
update_default_provisioning_connection_for_application_request_from_dict = UpdateDefaultProvisioningConnectionForApplicationRequest.from_dict(update_default_provisioning_connection_for_application_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


