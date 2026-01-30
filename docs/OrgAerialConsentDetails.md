# OrgAerialConsentDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The unique ID of the Aerial account | 
**granted_by** | **str** | Principal ID of the user who granted the permission | [optional] 
**granted_date** | **str** | Date when grant was created | [optional] 
**links** | [**LinksAerialConsentGranted**](LinksAerialConsentGranted.md) |  | [optional] 

## Example

```python
from okta.models.org_aerial_consent_details import OrgAerialConsentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OrgAerialConsentDetails from a JSON string
org_aerial_consent_details_instance = OrgAerialConsentDetails.from_json(json)
# print the JSON string representation of the object
print(OrgAerialConsentDetails.to_json())

# convert the object into a dict
org_aerial_consent_details_dict = org_aerial_consent_details_instance.to_dict()
# create an instance of OrgAerialConsentDetails from a dict
org_aerial_consent_details_from_dict = OrgAerialConsentDetails.from_dict(org_aerial_consent_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


