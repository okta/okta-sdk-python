# UpdateRealmRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**RealmProfile**](RealmProfile.md) |  | [optional] 

## Example

```python
from okta.models.update_realm_request import UpdateRealmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRealmRequest from a JSON string
update_realm_request_instance = UpdateRealmRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRealmRequest.to_json())

# convert the object into a dict
update_realm_request_dict = update_realm_request_instance.to_dict()
# create an instance of UpdateRealmRequest from a dict
update_realm_request_from_dict = UpdateRealmRequest.from_dict(update_realm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


