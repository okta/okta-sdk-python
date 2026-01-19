# OktaSupportCaseSelfAssigned

Customer allows Okta Support access to self-assigned cases. Support cases are self-assigned when an Okta Support team member creates and assigns the case to themselves.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**SelfAssignedStatus**](SelfAssignedStatus.md) |  | [optional] 

## Example

```python
from okta.models.okta_support_case_self_assigned import OktaSupportCaseSelfAssigned

# TODO update the JSON string below
json = "{}"
# create an instance of OktaSupportCaseSelfAssigned from a JSON string
okta_support_case_self_assigned_instance = OktaSupportCaseSelfAssigned.from_json(json)
# print the JSON string representation of the object
print(OktaSupportCaseSelfAssigned.to_json())

# convert the object into a dict
okta_support_case_self_assigned_dict = okta_support_case_self_assigned_instance.to_dict()
# create an instance of OktaSupportCaseSelfAssigned from a dict
okta_support_case_self_assigned_from_dict = OktaSupportCaseSelfAssigned.from_dict(okta_support_case_self_assigned_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


