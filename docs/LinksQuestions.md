# LinksQuestions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | [**LinksQuestionsQuestion**](LinksQuestionsQuestion.md) |  | [optional] 

## Example

```python
from okta.models.links_questions import LinksQuestions

# TODO update the JSON string below
json = "{}"
# create an instance of LinksQuestions from a JSON string
links_questions_instance = LinksQuestions.from_json(json)
# print the JSON string representation of the object
print(LinksQuestions.to_json())

# convert the object into a dict
links_questions_dict = links_questions_instance.to_dict()
# create an instance of LinksQuestions from a dict
links_questions_from_dict = LinksQuestions.from_dict(links_questions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


