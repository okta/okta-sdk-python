# okta.UserFactorApi

All URIs are relative to *https://subdomain.okta.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_factor**](UserFactorApi.md#activate_factor) | **POST** /api/v1/users/{userId}/factors/{factorId}/lifecycle/activate | Activate a factor
[**enroll_factor**](UserFactorApi.md#enroll_factor) | **POST** /api/v1/users/{userId}/factors | Enroll a factor
[**get_factor**](UserFactorApi.md#get_factor) | **GET** /api/v1/users/{userId}/factors/{factorId} | Retrieve a factor
[**get_factor_transaction_status**](UserFactorApi.md#get_factor_transaction_status) | **GET** /api/v1/users/{userId}/factors/{factorId}/transactions/{transactionId} | Retrieve a factor transaction status
[**get_yubikey_otp_token_by_id**](UserFactorApi.md#get_yubikey_otp_token_by_id) | **GET** /api/v1/org/factors/yubikey_token/tokens/{tokenId} | Retrieve a YubiKey OTP token
[**list_factors**](UserFactorApi.md#list_factors) | **GET** /api/v1/users/{userId}/factors | List all enrolled factors
[**list_supported_factors**](UserFactorApi.md#list_supported_factors) | **GET** /api/v1/users/{userId}/factors/catalog | List all supported factors
[**list_supported_security_questions**](UserFactorApi.md#list_supported_security_questions) | **GET** /api/v1/users/{userId}/factors/questions | List all supported security questions
[**list_yubikey_otp_tokens**](UserFactorApi.md#list_yubikey_otp_tokens) | **GET** /api/v1/org/factors/yubikey_token/tokens | List all YubiKey OTP tokens
[**resend_enroll_factor**](UserFactorApi.md#resend_enroll_factor) | **POST** /api/v1/users/{userId}/factors/{factorId}/resend | Resend a factor enrollment
[**unenroll_factor**](UserFactorApi.md#unenroll_factor) | **DELETE** /api/v1/users/{userId}/factors/{factorId} | Unenroll a factor
[**upload_yubikey_otp_token_seed**](UserFactorApi.md#upload_yubikey_otp_token_seed) | **POST** /api/v1/org/factors/yubikey_token/tokens | Upload a YubiKey OTP seed
[**verify_factor**](UserFactorApi.md#verify_factor) | **POST** /api/v1/users/{userId}/factors/{factorId}/verify | Verify a factor


# **activate_factor**
> UserFactorActivateResponse activate_factor(user_id, factor_id, body=body)

Activate a factor

Activates a factor. Some factors (`call`, `email`, `push`, `sms`, `token:software:totp`, `u2f`, and `webauthn`) require activation to complete the enrollment process.  Okta enforces a rate limit of five activation attempts within five minutes. After a user exceeds the rate limit, Okta returns an error message.  > **Notes:** > * If the user exceeds their SMS, call, or email factor activation rate limit, then an [OTP resend request](./#tag/UserFactor/operation/resendEnrollFactor) isn't allowed for the same factor. > * You can't use the Factors API to activate Okta Fastpass (`signed_nonce`) for a user. See [Configure Okta Fastpass](https://help.okta.com/okta_help.htm?type=oie&id=ext-fp-configure).

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_factor_activate_request import UserFactorActivateRequest
from okta.models.user_factor_activate_response import UserFactorActivateResponse
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.UserFactorApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    factor_id = 'zAgrsaBe0wVGRugDYtdv' # str | ID of an existing user factor
    body = okta.UserFactorActivateRequest() # UserFactorActivateRequest |  (optional)

    try:
        # Activate a factor
        api_response = api_instance.activate_factor(user_id, factor_id, body=body)
        print("The response of UserFactorApi->activate_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->activate_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **factor_id** | **str**| ID of an existing user factor | 
 **body** | [**UserFactorActivateRequest**](UserFactorActivateRequest.md)|  | [optional] 

### Return type

[**UserFactorActivateResponse**](UserFactorActivateResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_factor**
> UserFactor enroll_factor(user_id, body, update_phone=update_phone, template_id=template_id, token_lifetime_seconds=token_lifetime_seconds, activate=activate, accept_language=accept_language)

Enroll a factor

Enrolls a supported factor for the specified user  > **Notes:** >   * All responses return the enrolled factor with a status of either `PENDING_ACTIVATION` or `ACTIVE`. >   * You can't use the Factors API to enroll Okta Fastpass (`signed_nonce`) for a user. See [Configure Okta Fastpass](https://help.okta.com/okta_help.htm?type=oie&id=ext-fp-configure).  #### Additional SMS/Call factor information  * **Rate limits**: Okta may return a `429 Too Many Requests` status code if you attempt to resend an SMS or a voice call challenge (OTP) within the same time window. The current [rate limit](https://developer.okta.com/docs/reference/rate-limits/) is one SMS/CALL challenge per phone number every 30 seconds.  * **Existing phone numbers**: Okta may return a `400 Bad Request` status code if a user attempts to enroll with a different phone number when the user has an existing mobile phone or has an existing phone with voice call capability. A user can enroll only one mobile phone for `sms` and enroll only one voice call capable phone for `call` factor.  #### Additional WebAuthn factor information  * For detailed information on the WebAuthn standard, including an up-to-date list of supported browsers, see [webauthn.me](https://a0.to/webauthnme-okta-docs).  * When you enroll a WebAuthn factor, the `activation` object in `_embedded` contains properties used to help the client to create a new WebAuthn credential for use with Okta. See the [WebAuthn spec for PublicKeyCredentialCreationOptions](https://www.w3.org/TR/webauthn/#dictionary-makecredentialoptions).  #### Additional Custom TOTP factor information  * The enrollment process involves passing both the `factorProfileId` and `sharedSecret` properties for a token.  * A factor profile represents a particular configuration of the Custom TOTP factor. It includes certain properties that match the hardware token that end users possess, such as the HMAC algorithm, passcode length, and time interval. There can be multiple Custom TOTP factor profiles per org, but users can only enroll in one Custom TOTP factor. Admins can [create Custom TOTP factor profiles](https://help.okta.com/okta_help.htm?id=ext-mfa-totp) in the Admin Console. Then, copy the `factorProfileId` from the Admin Console into the API request.  * <x-lifecycle class=\"oie\"></x-lifecycle> For Custom TOTP enrollment, Okta automaticaly enrolls a user with a `token:software:totp` factor and the `push` factor if the user isn't currently enrolled with these factors.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_factor import UserFactor
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.UserFactorApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    body = okta.UserFactor() # UserFactor | Factor
    update_phone = False # bool | If `true`, indicates that you are replacing the currently registered phone number for the specified user. This parameter is ignored if the existing phone number is used by an activated factor. (optional) (default to False)
    template_id = 'cstk2flOtuCMDJK4b0g3' # str | ID of an existing custom SMS template. See the [SMS Templates API](../Template). This parameter is only used by `sms` factors. If the provided ID doesn't exist, the default template is used instead. (optional)
    token_lifetime_seconds = 300 # int | Defines how long the token remains valid (optional) (default to 300)
    activate = False # bool | If `true`, the factor is immediately activated as part of the enrollment. An activation process isn't required. Currently auto-activation is supported by `sms`, `call`, `email` and `token:hotp` (Custom TOTP) factors. (optional) (default to False)
    accept_language = 'fr' # str | An ISO 639-1 two-letter language code that defines a localized message to send. This parameter is only used by `sms` factors. If a localized message doesn't exist or the `templateId` is incorrect, the default template is used instead. (optional)

    try:
        # Enroll a factor
        api_response = api_instance.enroll_factor(user_id, body, update_phone=update_phone, template_id=template_id, token_lifetime_seconds=token_lifetime_seconds, activate=activate, accept_language=accept_language)
        print("The response of UserFactorApi->enroll_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->enroll_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **body** | [**UserFactor**](UserFactor.md)| Factor | 
 **update_phone** | **bool**| If &#x60;true&#x60;, indicates that you are replacing the currently registered phone number for the specified user. This parameter is ignored if the existing phone number is used by an activated factor. | [optional] [default to False]
 **template_id** | **str**| ID of an existing custom SMS template. See the [SMS Templates API](../Template). This parameter is only used by &#x60;sms&#x60; factors. If the provided ID doesn&#39;t exist, the default template is used instead. | [optional] 
 **token_lifetime_seconds** | **int**| Defines how long the token remains valid | [optional] [default to 300]
 **activate** | **bool**| If &#x60;true&#x60;, the factor is immediately activated as part of the enrollment. An activation process isn&#39;t required. Currently auto-activation is supported by &#x60;sms&#x60;, &#x60;call&#x60;, &#x60;email&#x60; and &#x60;token:hotp&#x60; (Custom TOTP) factors. | [optional] [default to False]
 **accept_language** | **str**| An ISO 639-1 two-letter language code that defines a localized message to send. This parameter is only used by &#x60;sms&#x60; factors. If a localized message doesn&#39;t exist or the &#x60;templateId&#x60; is incorrect, the default template is used instead. | [optional] 

### Return type

[**UserFactor**](UserFactor.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_factor**
> UserFactor get_factor(user_id, factor_id)

Retrieve a factor

Retrieves an existing factor for the specified user

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_factor import UserFactor
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.UserFactorApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    factor_id = 'zAgrsaBe0wVGRugDYtdv' # str | ID of an existing user factor

    try:
        # Retrieve a factor
        api_response = api_instance.get_factor(user_id, factor_id)
        print("The response of UserFactorApi->get_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->get_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **factor_id** | **str**| ID of an existing user factor | 

### Return type

[**UserFactor**](UserFactor.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_factor_transaction_status**
> UserFactorPushTransaction get_factor_transaction_status(user_id, factor_id, transaction_id)

Retrieve a factor transaction status

Retrieves the status of a `push` factor verification transaction   > **Note:**  > The response body for a number matching push challenge to an Okta Verify `push` factor enrollment is different from the response body of a standard push challenge.  > The number matching push challenge [response body](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserFactor/#tag/UserFactor/operation/getFactorTransactionStatus!c=200&path=1/_embedded&t=response) contains the correct answer for the challenge.  > Use [Verify a factor](/openapi/okta-management/management/tag/UserFactor/#tag/UserFactor/operation/verifyFactor) to configure which challenge is sent.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_factor_push_transaction import UserFactorPushTransaction
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.UserFactorApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    factor_id = 'zAgrsaBe0wVGRugDYtdv' # str | ID of an existing user factor
    transaction_id = 'gPAQcN3NDjSGOCAeG2Jv' # str | ID of an existing factor verification transaction

    try:
        # Retrieve a factor transaction status
        api_response = api_instance.get_factor_transaction_status(user_id, factor_id, transaction_id)
        print("The response of UserFactorApi->get_factor_transaction_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->get_factor_transaction_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **factor_id** | **str**| ID of an existing user factor | 
 **transaction_id** | **str**| ID of an existing factor verification transaction | 

### Return type

[**UserFactorPushTransaction**](UserFactorPushTransaction.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_yubikey_otp_token_by_id**
> UserFactorYubikeyOtpToken get_yubikey_otp_token_by_id(token_id)

Retrieve a YubiKey OTP token

Retrieves the specified YubiKey OTP token by `id`

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_factor_yubikey_otp_token import UserFactorYubikeyOtpToken
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.UserFactorApi(api_client)
    token_id = 'ykkxdtCA1fKVxyu6R0g3' # str | ID of a YubiKey token

    try:
        # Retrieve a YubiKey OTP token
        api_response = api_instance.get_yubikey_otp_token_by_id(token_id)
        print("The response of UserFactorApi->get_yubikey_otp_token_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->get_yubikey_otp_token_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| ID of a YubiKey token | 

### Return type

[**UserFactorYubikeyOtpToken**](UserFactorYubikeyOtpToken.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_factors**
> List[UserFactor] list_factors(user_id)

List all enrolled factors

Lists all enrolled factors for the specified user that are included in the highest priority [authenticator enrollment policy](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Policy/) that applies to the user.  Only enrolled factors that are `REQUIRED` or `OPTIONAL` in the highest priority authenticator enrollment policy can be returned.  > **Note:** When admins use this endpoint for other users, the authenticator enrollment policy that's evaluated can vary depending on how client-specific conditions are configured in the rules of an authenticator enrollment policy. The client-specific conditions of the admin's client are used during policy evaluation instead of the client-specific conditions of the user. This can affect which authenticator enrollment policy is evaluated and which factors are returned. > > For example, an admin in Europe lists all enrolled factors for a user in North America. The network zone of the admin's client (in Europe) is used during policy evaluation instead of the network zone of the user (in North America).

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_factor import UserFactor
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.UserFactorApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user

    try:
        # List all enrolled factors
        api_response = api_instance.list_factors(user_id)
        print("The response of UserFactorApi->list_factors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->list_factors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 

### Return type

[**List[UserFactor]**](UserFactor.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supported_factors**
> List[UserFactorSupported] list_supported_factors(user_id)

List all supported factors

Lists all the supported factors that can be enrolled for the specified user that are included in the highest priority [authenticator enrollment policy](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/Policy/) that applies to the user.  Only factors that are `REQUIRED` or `OPTIONAL` in the highest priority authenticator enrollment policy can be returned.  > **Note:** When admins use this endpoint for other users, the authenticator enrollment policy that's evaluated can vary depending on how client-specific conditions are configured in the rules of an authenticator enrollment policy. The client-specific conditions of the admin's client are used during policy evaluation instead of the client-specific conditions of the user. This can affect which authenticator enrollment policy is evaluated and which factors are returned. > > For example, an admin in Europe lists all supported factors for a user in North America. The network zone of the admin's client (in Europe) is used during policy evaluation instead of the network zone of the user (in North America).

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_factor_supported import UserFactorSupported
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.UserFactorApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user

    try:
        # List all supported factors
        api_response = api_instance.list_supported_factors(user_id)
        print("The response of UserFactorApi->list_supported_factors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->list_supported_factors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 

### Return type

[**List[UserFactorSupported]**](UserFactorSupported.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supported_security_questions**
> List[UserFactorSecurityQuestionProfile] list_supported_security_questions(user_id)

List all supported security questions

Lists all available security questions for the specified user

### Example

* Api Key Authentication (apiToken):

```python
import okta
from okta.models.user_factor_security_question_profile import UserFactorSecurityQuestionProfile
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.UserFactorApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user

    try:
        # List all supported security questions
        api_response = api_instance.list_supported_security_questions(user_id)
        print("The response of UserFactorApi->list_supported_security_questions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->list_supported_security_questions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 

### Return type

[**List[UserFactorSecurityQuestionProfile]**](UserFactorSecurityQuestionProfile.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_yubikey_otp_tokens**
> List[UserFactorYubikeyOtpToken] list_yubikey_otp_tokens(after=after, expand=expand, filter=filter, for_download=for_download, limit=limit, sort_by=sort_by, sort_order=sort_order)

List all YubiKey OTP tokens

Lists all YubiKey OTP tokens

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_factor_yubikey_otp_token import UserFactorYubikeyOtpToken
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.UserFactorApi(api_client)
    after = 'after_example' # str | Specifies the pagination cursor for the next page of tokens (optional)
    expand = 'expand_example' # str | Embeds the [user](/openapi/okta-management/management/tag/User/) resource if the YubiKey token is assigned to a user and `expand` is set to `user` (optional)
    filter = 'filter_example' # str | The expression used to filter tokens (optional)
    for_download = False # bool | Returns tokens in a CSV to download instead of in the response. When you use this query parameter, the `limit` default changes to 1000. (optional) (default to False)
    limit = 20 # int | Specifies the number of results per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | The value of how the tokens are sorted (optional)
    sort_order = 'sort_order_example' # str | Specifies the sort order, either `ASC` or `DESC` (optional)

    try:
        # List all YubiKey OTP tokens
        api_response = api_instance.list_yubikey_otp_tokens(after=after, expand=expand, filter=filter, for_download=for_download, limit=limit, sort_by=sort_by, sort_order=sort_order)
        print("The response of UserFactorApi->list_yubikey_otp_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->list_yubikey_otp_tokens: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| Specifies the pagination cursor for the next page of tokens | [optional] 
 **expand** | **str**| Embeds the [user](/openapi/okta-management/management/tag/User/) resource if the YubiKey token is assigned to a user and &#x60;expand&#x60; is set to &#x60;user&#x60; | [optional] 
 **filter** | **str**| The expression used to filter tokens | [optional] 
 **for_download** | **bool**| Returns tokens in a CSV to download instead of in the response. When you use this query parameter, the &#x60;limit&#x60; default changes to 1000. | [optional] [default to False]
 **limit** | **int**| Specifies the number of results per page | [optional] [default to 20]
 **sort_by** | **str**| The value of how the tokens are sorted | [optional] 
 **sort_order** | **str**| Specifies the sort order, either &#x60;ASC&#x60; or &#x60;DESC&#x60; | [optional] 

### Return type

[**List[UserFactorYubikeyOtpToken]**](UserFactorYubikeyOtpToken.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_enroll_factor**
> ResendUserFactor resend_enroll_factor(user_id, factor_id, resend_user_factor, template_id=template_id)

Resend a factor enrollment

Resends an `sms`, `call`, or `email` factor challenge as part of an enrollment flow.  For `call` and `sms` factors, Okta enforces a rate limit of one OTP challenge per device every 30 seconds. You can configure your `sms` and `call` factors to use a third-party telephony provider. See the [Telephony inline hook reference](https://developer.okta.com/docs/reference/telephony-hook/). Okta alternates between SMS providers with every resend request to ensure delivery of SMS and Call OTPs across different carriers.  > **Note:** Resend operations aren't allowed after a factor exceeds the activation rate limit. See [Activate a factor](./#tag/UserFactor/operation/activateFactor).

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.resend_user_factor import ResendUserFactor
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.UserFactorApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    factor_id = 'zAgrsaBe0wVGRugDYtdv' # str | ID of an existing user factor
    resend_user_factor = {"factorType":"sms","provider":"OKTA","profile":{"phoneNumber":"+1-555-415-1337"}} # ResendUserFactor | 
    template_id = 'cstk2flOtuCMDJK4b0g3' # str | ID of an existing custom SMS template. See the [SMS Templates API](../Template). This parameter is only used by `sms` factors. (optional)

    try:
        # Resend a factor enrollment
        api_response = api_instance.resend_enroll_factor(user_id, factor_id, resend_user_factor, template_id=template_id)
        print("The response of UserFactorApi->resend_enroll_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->resend_enroll_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **factor_id** | **str**| ID of an existing user factor | 
 **resend_user_factor** | [**ResendUserFactor**](ResendUserFactor.md)|  | 
 **template_id** | **str**| ID of an existing custom SMS template. See the [SMS Templates API](../Template). This parameter is only used by &#x60;sms&#x60; factors. | [optional] 

### Return type

[**ResendUserFactor**](ResendUserFactor.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unenroll_factor**
> unenroll_factor(user_id, factor_id, remove_recovery_enrollment=remove_recovery_enrollment)

Unenroll a factor

Unenrolls an existing factor for the specified user. You can't unenroll a factor from a deactivated user. Unenrolling a factor allows the user to enroll a new factor.  > **Note:** If you unenroll the `push` or the `signed_nonce` factors, Okta also unenrolls any other `totp`, `signed_nonce`, or Okta Verify `push` factors associated with the user.

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.UserFactorApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    factor_id = 'zAgrsaBe0wVGRugDYtdv' # str | ID of an existing user factor
    remove_recovery_enrollment = False # bool | If `true`, removes the phone number as both a recovery method and a factor. This parameter is only used for the `sms` and `call` factors. (optional) (default to False)

    try:
        # Unenroll a factor
        api_instance.unenroll_factor(user_id, factor_id, remove_recovery_enrollment=remove_recovery_enrollment)
    except Exception as e:
        print("Exception when calling UserFactorApi->unenroll_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **factor_id** | **str**| ID of an existing user factor | 
 **remove_recovery_enrollment** | **bool**| If &#x60;true&#x60;, removes the phone number as both a recovery method and a factor. This parameter is only used for the &#x60;sms&#x60; and &#x60;call&#x60; factors. | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_yubikey_otp_token_seed**
> UserFactorYubikeyOtpToken upload_yubikey_otp_token_seed(upload_yubikey_otp_token_seed_request, after=after, expand=expand, filter=filter, for_download=for_download, limit=limit, sort_by=sort_by, sort_order=sort_order)

Upload a YubiKey OTP seed

Uploads a seed for a user to enroll a YubiKey OTP

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.upload_yubikey_otp_token_seed_request import UploadYubikeyOtpTokenSeedRequest
from okta.models.user_factor_yubikey_otp_token import UserFactorYubikeyOtpToken
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.UserFactorApi(api_client)
    upload_yubikey_otp_token_seed_request = okta.UploadYubikeyOtpTokenSeedRequest() # UploadYubikeyOtpTokenSeedRequest | 
    after = 'after_example' # str | Specifies the pagination cursor for the next page of tokens (optional)
    expand = 'expand_example' # str | Embeds the [user](/openapi/okta-management/management/tag/User/) resource if the YubiKey token is assigned to a user and `expand` is set to `user` (optional)
    filter = 'filter_example' # str | The expression used to filter tokens (optional)
    for_download = False # bool | Returns tokens in a CSV to download instead of in the response. When you use this query parameter, the `limit` default changes to 1000. (optional) (default to False)
    limit = 20 # int | Specifies the number of results per page (optional) (default to 20)
    sort_by = 'sort_by_example' # str | The value of how the tokens are sorted (optional)
    sort_order = 'sort_order_example' # str | Specifies the sort order, either `ASC` or `DESC` (optional)

    try:
        # Upload a YubiKey OTP seed
        api_response = api_instance.upload_yubikey_otp_token_seed(upload_yubikey_otp_token_seed_request, after=after, expand=expand, filter=filter, for_download=for_download, limit=limit, sort_by=sort_by, sort_order=sort_order)
        print("The response of UserFactorApi->upload_yubikey_otp_token_seed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->upload_yubikey_otp_token_seed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_yubikey_otp_token_seed_request** | [**UploadYubikeyOtpTokenSeedRequest**](UploadYubikeyOtpTokenSeedRequest.md)|  | 
 **after** | **str**| Specifies the pagination cursor for the next page of tokens | [optional] 
 **expand** | **str**| Embeds the [user](/openapi/okta-management/management/tag/User/) resource if the YubiKey token is assigned to a user and &#x60;expand&#x60; is set to &#x60;user&#x60; | [optional] 
 **filter** | **str**| The expression used to filter tokens | [optional] 
 **for_download** | **bool**| Returns tokens in a CSV to download instead of in the response. When you use this query parameter, the &#x60;limit&#x60; default changes to 1000. | [optional] [default to False]
 **limit** | **int**| Specifies the number of results per page | [optional] [default to 20]
 **sort_by** | **str**| The value of how the tokens are sorted | [optional] 
 **sort_order** | **str**| Specifies the sort order, either &#x60;ASC&#x60; or &#x60;DESC&#x60; | [optional] 

### Return type

[**UserFactorYubikeyOtpToken**](UserFactorYubikeyOtpToken.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_factor**
> UserFactorVerifyResponse verify_factor(user_id, factor_id, template_id=template_id, token_lifetime_seconds=token_lifetime_seconds, x_forwarded_for=x_forwarded_for, user_agent=user_agent, accept_language=accept_language, body=body)

Verify a factor

Verifies an OTP for a factor. Some factors (`call`, `email`, `push`, `sms`, `u2f`, and `webauthn`) must first issue a challenge before you can verify the factor. Do this by making a request without a body. After a challenge is issued, make another request to verify the factor.  > **Notes:** > - You can send standard push challenges or number matching push challenges to Okta Verify `push` factor enrollments. Use a [request body](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserFactor/#tag/UserFactor/operation/verifyFactor!path=2/useNumberMatchingChallenge&t=request) for number matching push challenges. > - To verify a `push` factor, use the **poll** link returned when you issue the challenge. See [Retrieve a factor transaction status](/openapi/okta-management/management/tag/UserFactor/#tag/UserFactor/operation/getFactorTransactionStatus).

### Example

* Api Key Authentication (apiToken):
* OAuth Authentication (oauth2):

```python
import okta
from okta.models.user_factor_verify_request import UserFactorVerifyRequest
from okta.models.user_factor_verify_response import UserFactorVerifyResponse
from okta.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://subdomain.okta.com
# See configuration.py for a list of all supported configuration parameters.
configuration = okta.Configuration(
    host = "https://subdomain.okta.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiToken
configuration.api_key['apiToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiToken'] = 'Bearer'

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with okta.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = okta.UserFactorApi(api_client)
    user_id = '00ub0oNGTSWTBKOLGLNR' # str | ID of an existing Okta user
    factor_id = 'zAgrsaBe0wVGRugDYtdv' # str | ID of an existing user factor
    template_id = 'cstk2flOtuCMDJK4b0g3' # str | ID of an existing custom SMS template. See the [SMS Templates API](../Template). This parameter is only used by `sms` factors. (optional)
    token_lifetime_seconds = 300 # int | Defines how long the token remains valid (optional) (default to 300)
    x_forwarded_for = 'x_forwarded_for_example' # str | Public IP address for the user agent (optional)
    user_agent = 'user_agent_example' # str | Type of user agent detected when the request is made. Required to verify `push` factors. (optional)
    accept_language = 'fr' # str | An ISO 639-1 two-letter language code that defines a localized message to send. This parameter is only used by `sms` factors. If a localized message doesn't exist or the `templateId` is incorrect, the default template is used instead. (optional)
    body = okta.UserFactorVerifyRequest() # UserFactorVerifyRequest | Verifies an OTP for a factor. Some factors (`call`, `email`, `push`, `sms`, `u2f`, and `webauthn`) must first issue a challenge before you can verify the factor. Do this by making a request without a body. After a challenge is issued, make another request to verify the factor.  > **Note:** > Unlike standard push challenges that don't require a request body, a number matching [`push`](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserFactor/#tag/UserFactor/operation/verifyFactor!path=2/useNumberMatchingChallenge&t=request) challenge requires a request body. `useNumberMatchingChallenge` must be set to `true`. > When a number matching challenge is issued for an Okta Verify `push` factor enrollment, a `correctAnswer` challenge object is returned in the [`_embedded`](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserFactor/#tag/UserFactor/operation/verifyFactor!c=200&path=_embedded&t=response) object. (optional)

    try:
        # Verify a factor
        api_response = api_instance.verify_factor(user_id, factor_id, template_id=template_id, token_lifetime_seconds=token_lifetime_seconds, x_forwarded_for=x_forwarded_for, user_agent=user_agent, accept_language=accept_language, body=body)
        print("The response of UserFactorApi->verify_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserFactorApi->verify_factor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of an existing Okta user | 
 **factor_id** | **str**| ID of an existing user factor | 
 **template_id** | **str**| ID of an existing custom SMS template. See the [SMS Templates API](../Template). This parameter is only used by &#x60;sms&#x60; factors. | [optional] 
 **token_lifetime_seconds** | **int**| Defines how long the token remains valid | [optional] [default to 300]
 **x_forwarded_for** | **str**| Public IP address for the user agent | [optional] 
 **user_agent** | **str**| Type of user agent detected when the request is made. Required to verify &#x60;push&#x60; factors. | [optional] 
 **accept_language** | **str**| An ISO 639-1 two-letter language code that defines a localized message to send. This parameter is only used by &#x60;sms&#x60; factors. If a localized message doesn&#39;t exist or the &#x60;templateId&#x60; is incorrect, the default template is used instead. | [optional] 
 **body** | [**UserFactorVerifyRequest**](UserFactorVerifyRequest.md)| Verifies an OTP for a factor. Some factors (&#x60;call&#x60;, &#x60;email&#x60;, &#x60;push&#x60;, &#x60;sms&#x60;, &#x60;u2f&#x60;, and &#x60;webauthn&#x60;) must first issue a challenge before you can verify the factor. Do this by making a request without a body. After a challenge is issued, make another request to verify the factor.  &gt; **Note:** &gt; Unlike standard push challenges that don&#39;t require a request body, a number matching [&#x60;push&#x60;](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserFactor/#tag/UserFactor/operation/verifyFactor!path&#x3D;2/useNumberMatchingChallenge&amp;t&#x3D;request) challenge requires a request body. &#x60;useNumberMatchingChallenge&#x60; must be set to &#x60;true&#x60;. &gt; When a number matching challenge is issued for an Okta Verify &#x60;push&#x60; factor enrollment, a &#x60;correctAnswer&#x60; challenge object is returned in the [&#x60;_embedded&#x60;](https://developer.okta.com/docs/api/openapi/okta-management/management/tag/UserFactor/#tag/UserFactor/operation/verifyFactor!c&#x3D;200&amp;path&#x3D;_embedded&amp;t&#x3D;response) object. | [optional] 

### Return type

[**UserFactorVerifyResponse**](UserFactorVerifyResponse.md)

### Authorization

[apiToken](../README.md#apiToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Too Many Requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

