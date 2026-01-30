# PostAuthSessionPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | **str** | Policy conditions aren&#39;t supported for this policy type | [optional] 

## Example

```python
from okta.models.post_auth_session_policy import PostAuthSessionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of PostAuthSessionPolicy from a JSON string
post_auth_session_policy_instance = PostAuthSessionPolicy.from_json(json)
# print the JSON string representation of the object
print(PostAuthSessionPolicy.to_json())

# convert the object into a dict
post_auth_session_policy_dict = post_auth_session_policy_instance.to_dict()
# create an instance of PostAuthSessionPolicy from a dict
post_auth_session_policy_from_dict = PostAuthSessionPolicy.from_dict(post_auth_session_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


