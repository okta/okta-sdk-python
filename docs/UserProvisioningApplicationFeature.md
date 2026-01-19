# UserProvisioningApplicationFeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | [**CapabilitiesObject**](CapabilitiesObject.md) |  | [optional] 

## Example

```python
from okta.models.user_provisioning_application_feature import UserProvisioningApplicationFeature

# TODO update the JSON string below
json = "{}"
# create an instance of UserProvisioningApplicationFeature from a JSON string
user_provisioning_application_feature_instance = UserProvisioningApplicationFeature.from_json(json)
# print the JSON string representation of the object
print(UserProvisioningApplicationFeature.to_json())

# convert the object into a dict
user_provisioning_application_feature_dict = user_provisioning_application_feature_instance.to_dict()
# create an instance of UserProvisioningApplicationFeature from a dict
user_provisioning_application_feature_from_dict = UserProvisioningApplicationFeature.from_dict(user_provisioning_application_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


