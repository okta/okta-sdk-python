# MembershipRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_external_id** | **str** | The external ID of the user to be added as a member of the group in Okta | [optional] 

## Example

```python
from okta.models.membership_request_schema import MembershipRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MembershipRequestSchema from a JSON string
membership_request_schema_instance = MembershipRequestSchema.from_json(json)
# print the JSON string representation of the object
print(MembershipRequestSchema.to_json())

# convert the object into a dict
membership_request_schema_dict = membership_request_schema_instance.to_dict()
# create an instance of MembershipRequestSchema from a dict
membership_request_schema_from_dict = MembershipRequestSchema.from_dict(membership_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


