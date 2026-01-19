# LogTransaction

A `transaction` object comprises contextual information associated with its respective event. This information is useful for understanding sequences of correlated events. For example, a `transaction` object such as the following: ``` {   \"id\": \"Wn4f-0RQ8D8lTSLkAmkKdQAADqo\",   \"type\": \"WEB\",   \"detail\": null } ``` indicates that a `WEB` request with `id` `Wn4f-0RQ8D8lTSLkAmkKdQAADqo` has created this event.  A `transaction` object with a `requestApiTokenId` in the `detail` object, for example : ``` {   \"id\": \"YjSlblAAqnKY7CdyCkXNBgAAAIU\",   \"type\": \"WEB\",   \"detail\": {     \"requestApiTokenId\": \"00T94e3cn9kSEO3c51s5\"   } } ``` indicates that this event was the result of an action performed through an API using the token identified by 00T94e3cn9kSEO3c51s5. The token ID is visible in the Admin Console, **Security** > **API**. See [API token management](https://help.okta.com/okta_help.htm?id=Security_API). For more information on API tokens, see [Create an API token](https://developer.okta.com/docs/guides/create-an-api-token/).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **Dict[str, object]** | Details for this transaction. | [optional] [readonly] 
**id** | **str** | Unique identifier for this transaction. | [optional] [readonly] 
**type** | **str** | Describes the kind of transaction. &#x60;WEB&#x60; indicates a web request. &#x60;JOB&#x60; indicates an asynchronous task. | [optional] [readonly] 

## Example

```python
from okta.models.log_transaction import LogTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of LogTransaction from a JSON string
log_transaction_instance = LogTransaction.from_json(json)
# print the JSON string representation of the object
print(LogTransaction.to_json())

# convert the object into a dict
log_transaction_dict = log_transaction_instance.to_dict()
# create an instance of LogTransaction from a dict
log_transaction_from_dict = LogTransaction.from_dict(log_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


