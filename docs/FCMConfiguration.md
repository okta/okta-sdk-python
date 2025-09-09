# FCMConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | (Optional) File name for Admin Console display | [optional] 
**project_id** | **str** | Project ID of FCM configuration | [optional] [readonly] 
**service_account_json** | **object** | JSON containing the private service account key and service account details. See [Creating and managing service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) for more information on creating service account keys in JSON. | [optional] 

## Example

```python
from okta.models.fcm_configuration import FCMConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of FCMConfiguration from a JSON string
fcm_configuration_instance = FCMConfiguration.from_json(json)
# print the JSON string representation of the object
print(FCMConfiguration.to_json())

# convert the object into a dict
fcm_configuration_dict = fcm_configuration_instance.to_dict()
# create an instance of FCMConfiguration from a dict
fcm_configuration_from_dict = FCMConfiguration.from_dict(fcm_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


