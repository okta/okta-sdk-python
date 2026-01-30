# OrgAerialGrantNotFound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The unique ID of the Aerial account | [optional] 
**granted_by** | **str** | Principal ID of the user who granted the permission | [optional] 
**granted_date** | **str** | Date when grant was created | [optional] 
**links** | [**LinksAerialConsentGranted**](LinksAerialConsentGranted.md) |  | [optional] 

## Example

```python
from okta.models.org_aerial_grant_not_found import OrgAerialGrantNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of OrgAerialGrantNotFound from a JSON string
org_aerial_grant_not_found_instance = OrgAerialGrantNotFound.from_json(json)
# print the JSON string representation of the object
print(OrgAerialGrantNotFound.to_json())

# convert the object into a dict
org_aerial_grant_not_found_dict = org_aerial_grant_not_found_instance.to_dict()
# create an instance of OrgAerialGrantNotFound from a dict
org_aerial_grant_not_found_from_dict = OrgAerialGrantNotFound.from_dict(org_aerial_grant_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


