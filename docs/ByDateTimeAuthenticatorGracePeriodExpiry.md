# ByDateTimeAuthenticatorGracePeriodExpiry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **str** | The expiry date for a &#x60;BY_DATE_TIME&#x60; grace period type. Valid format: &#x60;yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;&#x60;  For example, &#x60;2025-01-01T18:30:45.000Z&#x60;  | [optional] 

## Example

```python
from okta.models.by_date_time_authenticator_grace_period_expiry import ByDateTimeAuthenticatorGracePeriodExpiry

# TODO update the JSON string below
json = "{}"
# create an instance of ByDateTimeAuthenticatorGracePeriodExpiry from a JSON string
by_date_time_authenticator_grace_period_expiry_instance = ByDateTimeAuthenticatorGracePeriodExpiry.from_json(json)
# print the JSON string representation of the object
print(ByDateTimeAuthenticatorGracePeriodExpiry.to_json())

# convert the object into a dict
by_date_time_authenticator_grace_period_expiry_dict = by_date_time_authenticator_grace_period_expiry_instance.to_dict()
# create an instance of ByDateTimeAuthenticatorGracePeriodExpiry from a dict
by_date_time_authenticator_grace_period_expiry_from_dict = ByDateTimeAuthenticatorGracePeriodExpiry.from_dict(by_date_time_authenticator_grace_period_expiry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


