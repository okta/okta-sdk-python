# ProvisioningDetails

Supported provisioning configurations for your integration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**features** | **List[str]** | List of provisioning features supported in this integration | 
**scim** | [**Scim**](Scim.md) |  | 

## Example

```python
from okta.models.provisioning_details import ProvisioningDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisioningDetails from a JSON string
provisioning_details_instance = ProvisioningDetails.from_json(json)
# print the JSON string representation of the object
print(ProvisioningDetails.to_json())

# convert the object into a dict
provisioning_details_dict = provisioning_details_instance.to_dict()
# create an instance of ProvisioningDetails from a dict
provisioning_details_from_dict = ProvisioningDetails.from_dict(provisioning_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


