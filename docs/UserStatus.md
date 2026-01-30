# UserStatus

The current status of the user.  The status of a user changes in response to explicit events, such as admin-driven lifecycle changes, user login, or self-service password recovery. Okta doesn't asynchronously sweep through users and update their password expiry state, for example. Instead, Okta evaluates password policy at login time, notices the password has expired, and moves the user to the expired state. When running reports, remember that the data is valid as of the last login or lifecycle event for that user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


