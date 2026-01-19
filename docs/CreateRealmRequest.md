# CreateRealmRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**RealmProfile**](RealmProfile.md) |  | [optional] 

## Example

```python
from okta.models.create_realm_request import CreateRealmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRealmRequest from a JSON string
create_realm_request_instance = CreateRealmRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRealmRequest.to_json())

# convert the object into a dict
create_realm_request_dict = create_realm_request_instance.to_dict()
# create an instance of CreateRealmRequest from a dict
create_realm_request_from_dict = CreateRealmRequest.from_dict(create_realm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


