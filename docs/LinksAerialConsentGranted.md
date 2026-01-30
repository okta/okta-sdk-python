# LinksAerialConsentGranted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**HrefObjectSelfLink**](HrefObjectSelfLink.md) |  | [optional] 
**revoke** | [**HrefObjectRevokeAerialConsent**](HrefObjectRevokeAerialConsent.md) |  | [optional] 

## Example

```python
from okta.models.links_aerial_consent_granted import LinksAerialConsentGranted

# TODO update the JSON string below
json = "{}"
# create an instance of LinksAerialConsentGranted from a JSON string
links_aerial_consent_granted_instance = LinksAerialConsentGranted.from_json(json)
# print the JSON string representation of the object
print(LinksAerialConsentGranted.to_json())

# convert the object into a dict
links_aerial_consent_granted_dict = links_aerial_consent_granted_instance.to_dict()
# create an instance of LinksAerialConsentGranted from a dict
links_aerial_consent_granted_from_dict = LinksAerialConsentGranted.from_dict(links_aerial_consent_granted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


