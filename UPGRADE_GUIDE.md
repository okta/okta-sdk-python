# Release Notes: Python SDK V3.0.0 - OpenAPI 3.0 Migration

**Date:** 2025-10-25

## Summary

This is a major release of our Python SDK, introducing support for OpenAPI Specification 3.0. This update allows for more robust, flexible, and descriptive API integrations.

**IMPORTANT:** This version introduces significant breaking changes as we are discontinuing support for OpenAPI 2.0 (formerly Swagger). All users will need to update their integration code to accommodate the changes outlined below.

## New Features

Our migration from a legacy Swagger-based generator to the modern OpenAPI Generator unlocks a new level of functionality and developer experience.

  * **Strongly-Typed Data Models:** By integrating Pydantic, all API models now offer robust data validation and type enforcement at runtime, reducing bugs and improving code clarity.
  * **Auto-Generated Documentation:** The SDK now includes a `docs/` directory with comprehensive, automatically generated documentation for all API endpoints and models, ensuring the documentation is always in sync with the code.
  * **Full OpenAPI 3.0 Feature Support:** The SDK now fully supports key OAS 3.0 features, providing a more flexible and powerful integration experience:
      * **Multiple Server Support:** Dynamically switch between server environments (e.g., production, staging).
      * **Enhanced Request Body Support:** Use complex request bodies with multiple media types.
      * **Callback Support:** Handle asynchronous operations.

## Improvements

This architectural overhaul provides significant long-term benefits for the stability and usability of the SDK.

  * **Faster, More Frequent Updates:** By adopting the `openapi-generator` and a centralized API specification (`management.yaml`), we can now update the SDK much more frequently. This ensures the SDK remains in close alignment with our production APIs, giving you faster access to new features.
  * **Enhanced Developer Experience:** Stricter typing with Pydantic provides better IDE support, including more accurate autocompletion and inline error checking, making development faster and more efficient.
  * **Improved Code & API Consistency:** The SDK's code is now a direct, machine-readable translation of the official API spec. This guarantees that function names, models, and parameters are always consistent with the API documentation.
  * **Robust Error Handling:** With a wider range of specific exception classes, you can now write more precise error-handling logic to manage different failure scenarios.

## Breaking Changes

This release introduces fundamental changes to the SDK's architecture, dependencies, and project structure. Please review the following points carefully to migrate your application.

1.  **Core Dependencies: Pydantic & Typing**
    The SDK now leverages the Pydantic and `typing` libraries to enforce stricter data type binding for function parameters and return types. This improves code reliability and provides a better developer experience with more explicit type checking.
2.  **Model Class Implementation**
    Model classes have been refactored to use Pydantic's `BaseModel` instead of the previous `OktaObject`.
      * **Inheritance:** Models now inherit from `pydantic.BaseModel`.
      * **Initialization:** The `__init__` method for value assignment has been removed. Model properties are now declared directly in the class with expected data types, making them required or optional and allowing default values. This ensures type validation upon object creation.
      * **New Methods:** Models now include several new utility methods for data handling: `to_str()`, `to_json()`, `from_json()`, `to_dict()`, and `from_dict()`.
3.  **Directory and File Structure**
    The project's directory structure has been significantly reorganized.
      * **API Directory (`okta/api`):**
          * Previous: API endpoint files were located in `okta/resource_clients/`.
          * Current: All feature API files are now located in the `okta/api/` directory.
      * **OpenAPI Generation Directory (`openapi/`):**
          * **Generator Tool:** We have migrated from `okta-sdk-generator` to the standard `openapi-generator`.
          * **Templating:** Templates now use Mustache instead of Handlebars.
          * **Configuration (`config.yaml`):** A new `config.yaml` file controls the SDK generation process. It defines:
              * `packageName`: The directory name under which the SDK will be generated.
              * `outputDir`: The path in your repo where the package will be generated.
              * `templateDir`: The path to the template directory location.
              * `files`: Details about custom code templates and their corresponding output Python filenames.
              * `modelPackage`: The name for your models directory.
              * `apiPackage`: The name for your APIs directory.
              * `additionalProperties`: A section to declare custom data objects which can be used in Mustache templates.
          * **Spec File (`management.yaml`):** This new file contains all API definitions, schemas, and properties used by `openapi-generator`.
          * **Tool Versioning (`openapitools.json`):** Replaces `package.json` for managing the `openapi-generator` version.
          * **Generation Scripts:**
              * `regen.sh` has been replaced by `generate.sh`, which now orchestrates the `openapi-generator`.
              * `update_config.py`: A Python script to generate pre-processing custom data objects, append them to `config.yaml`, and make them available for use in Mustache templates.
      * **Test Directory (`tests/`):**
          * Existing integration tests have been fixed and updated.
          * New integration tests have been added to provide coverage for the new API files.
          * Unit tests have been temporarily removed and will be reintroduced in future updates.
      * **New Docs Directory (`docs/`):**
          * This new directory contains comprehensive documentation for all model schemas and APIs generated by the `management.yaml` specification.
4.  **API File Logic**
    The internal logic and structure of API endpoint files have been standardized.
      * **Function Naming:** Function names are now generated directly from the `operationId` in the `management.yaml` spec (e.g., `operationId: createApplication` becomes `def create_application(...)`).
      * **Serialization:** Each API operation now has a corresponding `serialize` function responsible for validating and processing all input parameters.
      * **Execution Flow:** The flow within each API operation function is now as follows:
        1.  A `response_type` dictionary is declared to map status codes to return types.
        2.  The `serialize` function is called to parse inputs and return request components (`method`, `url`, `header_params`, etc.).
        3.  A `request` object is created via `request_executor.create_request`.
        4.  The API is called via `request_executor.execute`.
        5.  The response is processed:
              * If the response is empty or the status code is 204, it will return (`None`, `response`, `None`).
              * If an error is present, the error is returned.
              * Otherwise, the response is converted using the `RESTResponse` class and then deserialized via the API client's `response_deserialize` method.
5.  **API Client (`api_client.py`)**
    The `api_client.py` module has expanded responsibilities beyond being a simple base class.
      * **Initialization:** The `__init__` method now accepts a configuration object and sets up parameters for API calls (e.g., Authorization, private key, org URL).
      * **Parameter Serialization (`param_serialize`):** A new method that validates and assembles all parts of a request, including URL, path/query params, headers, body, and authentication settings. It has supporting methods such as `update_params_for_auth`, `_apply_auth_params`, `parameters_to_tuples`, and `parameters_to_url_query`.
      * **Response Deserialization (`response_deserialize`):** A new method for formatting and handling the API response. It has supporting methods such as `deserialize`, `__deserialize_object`, and `__deserialize_model`.
6.  **Exception Handling (`exceptions/`)**
    The `exceptions.py` file has been expanded to include a wider range of specific exceptions, such as `OpenApi Exception`, `ApiTypeError`, and `ApiValueError`, in addition to the existing `OktaAPIException`.
7.  **New and Modified Modules**
      * **`configuration.py` (New):** This new file defines a `Configuration` class that holds all configuration parameters, which is initialized and used by the `api_client`.
      * **`rest.py` (New):** This module introduces the `RESTResponse` class, used to wrap raw API responses into a standardized object before final processing.
      * **`request_executor.py` (Modified):** The `execute` method now returns the raw `response`, `response_body`, and `error`, as response formatting is now handled by the `api_client`'s `response_deserialize` method.
          * Previous: `return (OktaAPIResponse (...), error)`
          * New: `return response, response_body, error`
      * **`client.py` (Modified):** No major logical changes. It still handles configuration setup and `request_executor` initialization. It now calls `super().__init__` to pass the configuration object to the `api_client` base class.
      * **`api_response.py` (Deprecated):** The `OktaAPIResponse` class is no longer used for response handling. The file is kept for backward compatibility purposes if users wish to reintegrate it manually.

## Migration Guide

We recommend the following step-by-step process for a smooth migration.

### Step 1: Update SDK Version

First, update your `requirements.txt` or `pyproject.toml` to use the new SDK version:

```python
okta-sdk-python>=3.0.0
```

### Step 2: No change to how client initialization process.

### Step 3: Update Your Import Paths

Due to the directory structure changes, you will need to update your import statements.

  * API clients are now in `okta.api` (e.g., `from okta.api.user_api import UserApi`).
  * Models are now in `okta.models` (e.g., `from okta.models.user import User`).

### Step 4: Refactor Model Usage

Models are now Pydantic `BaseModel` objects and are instantiated with keyword arguments instead of an `__init__` method.

**Before:**

```python
# Old OktaObject model
user_profile = { "firstName": "John", "lastName": "Doe" }
new_user = User(profile=user_profile)
```

**After:**

```python
# New Pydantic model
from okta import UserProfile, PasswordCredential, \
CreateUserRequest, UserNextLogin

# Instantiate nested models directly with keyword arguments
profile = UserProfile(firstName="John", lastName="Doe")
create_request = CreateUserRequest(**{"profile":profile})
```

### Step 5: Refactor API Method Calls

This is the most significant change. Function names are now based on the `operationId` from the API spec, and parameters (especially request bodies) are passed as typed model objects.

**Before:**

```python
# Old method name and dictionary-based body
user_profile = { "firstName": "John", "lastName": "Doe" }
created_user, response, error await client.create_user(
    {"profile": user_profile}, activate=True
)
```

**After:**

```python
# New operationId-based method name and Pydantic model for the body
from okta.api.user_api import UserApi
from okta import UserProfile, PasswordCredential, \
CreateUserRequest, UserNextLogin

user_api = UserApi(client.api_client)
profile = UserProfile(firstName="John", lastName="Doe")
create_request = CreateUserRequest(**{"profile":profile})
# Call the new method with the typed request object
created_user await user_api.create_user(
    create_user_request=create_request, activate=True
)
```

### Step 6: Update Exception Handling

Review your `try...except` blocks to catch the new, more specific exceptions for better error handling.

**Before:**

```python
from okta.exceptions import OktaAPIException

try:
    # API call
except OktaAPIException as e:
    print(e)
```

**After:**

```python
from okta.exceptions.exceptions import ApiValueError, ApiException

try:
    #API call
except ApiValueError as e:
    print(f"Validation Error: {e}")
except ApiException as e:
    print(f"Generic API Error: {e}")
```

### Step 7: Test Thoroughly

Finally, execute your test suite against a non-production environment. Pay close attention to `ApiValueError` exceptions, as they will indicate where data types or required fields in your models do not match the new, stricter validation rules.

## Example: Create a User

**Before:**

```python
from okta.client import Client as OktaClient

config = {
    'orgUrl': 'https://{your_org}.okta.com',
    'token': 'YOUR_API_TOKEN',
}

async def main():
    client = OktaClient()
    # create user with custom attribute
    body = {
        "profile": {
            "firstName": "John",
            "lastName": "Smith",
            "email": "jsmith@matrix.com",
            "login": "jsmith@matrix.com",
            "customAttr": "custom value"
        },
        "credentials": {
            "password": { "value": "Knock knock*neo*111" }
        }
    }
    result = await client.create_user(body)

    #create user without custom attribute
    body = {
        "profile": {
            "firstName": "Neo",
            "lastName": "Anderson",
            "email": "nanderson@matrix.com",
            "login": "nanderson@matrix.com"
        },
        "credentials": {
            "password": { "value": "Knock*knock*neo*111" }
        }
    }
    result = await client.create_user(body)

    users, resp, err await client.list_users()
    for user in users:
        print(user.profile.first_name, user.profile.last_name)
        try:
            print(user.profile.customAttr)
        except:
            print('User has no customAttr')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

**After:**

```python
import asyncio
from okta import UserProfile, PasswordCredential, \
CreateUserRequest, UserNextLogin, UserCredentials
from okta.client import Client as OktaClient

config = {
    'orgUrl': 'https://{your_org}.okta.com',
    'token': 'YOUR_API_TOKEN',
}
okta_client = OktaClient(config)

user_config = {
    "firstName": "Sample12",
    "lastName": "Sample12",
    "email": "sample12.sample12@example.com",
    "login": "sample12.sample12@example.com",
    "mobilePhone": "555-415-1337"
}
user_profile = UserProfile(**user_config)

password_value = {
    "value": "Knock knock*neo*111"
}
password_credential = PasswordCredential(**password_value)

user_credentials = {
    "password": password_credential
}
user_credentials = UserCredentials(**user_credentials)

create_user_request = {
    "profile": user_profile,
    "credentials": user_credentials,
}
user_request = CreateUserRequest(**create_user_request)

async def users():
    next_login = UserNextLogin(UserNextLogin.CHANGEPASSWORD)
    app, resp, err = await okta_client.create_user(user_request,
                                                   activate=True, provider=False, next_login=next_login)
    print("The response of ApplicationApi->create_application:\n")
    print(app)
    print(resp, err)

    users, resp, err = await okta_client.list_users()
    for user in users:
        print(user.profile.first_name, user.profile.last_name)
        try:
            print(user.profile.customAttr)
        except:
            print('User has no customAttr')
```