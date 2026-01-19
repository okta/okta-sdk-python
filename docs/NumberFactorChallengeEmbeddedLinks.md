# NumberFactorChallengeEmbeddedLinks

Contains the `challenge` and `correctAnswer` objects for `push` factors that use a number matching challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenge** | [**NumberFactorChallengeEmbeddedLinksChallenge**](NumberFactorChallengeEmbeddedLinksChallenge.md) |  | [optional] 

## Example

```python
from okta.models.number_factor_challenge_embedded_links import NumberFactorChallengeEmbeddedLinks

# TODO update the JSON string below
json = "{}"
# create an instance of NumberFactorChallengeEmbeddedLinks from a JSON string
number_factor_challenge_embedded_links_instance = NumberFactorChallengeEmbeddedLinks.from_json(json)
# print the JSON string representation of the object
print(NumberFactorChallengeEmbeddedLinks.to_json())

# convert the object into a dict
number_factor_challenge_embedded_links_dict = number_factor_challenge_embedded_links_instance.to_dict()
# create an instance of NumberFactorChallengeEmbeddedLinks from a dict
number_factor_challenge_embedded_links_from_dict = NumberFactorChallengeEmbeddedLinks.from_dict(number_factor_challenge_embedded_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


