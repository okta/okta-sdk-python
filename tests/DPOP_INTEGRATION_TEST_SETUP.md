# DPoP Integration Test Setup Guide

This guide explains how to set up and run the DPoP (Demonstrating Proof-of-Possession) integration tests for the Okta Python SDK.

## Overview

The DPoP integration tests validate the implementation of RFC 9449 against a live Okta org, similar to the .NET SDK integration tests: https://github.com/okta/okta-sdk-dotnet/pull/855

## Prerequisites

- Python 3.7+
- pytest and pytest-asyncio installed
- Access to an Okta org (for live testing) OR use pre-recorded cassettes (offline testing)

## Setup Options

### Option 1: Automatic Setup (Recommended)

The easiest way to set up the DPoP integration tests is to use the automated setup script:

```bash
python setup_dpop_test_app.py
```

This script will:
1. Prompt you for your Okta org URL (e.g., `https://dev-xxxxx.okta.com`)
2. Prompt you for your Okta API token
3. Automatically create an OIDC application with DPoP enabled
4. Generate an RSA 3072-bit key pair for DPoP
5. Save the configuration to `dpop_test_config.py` (gitignored)

**Example:**
```bash
$ python setup_dpop_test_app.py
Enter your Okta org URL (e.g., https://dev-xxxxx.okta.com): https://dev-20982288.okta.com
Enter your Okta API token: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

✓ Created OIDC application: 0oaXXXXXXXXXXXXXXXXX
✓ Generated RSA key pair
✓ Configuration saved to dpop_test_config.py

Setup complete! Run tests with:
  pytest tests/integration/test_dpop_it.py -v
```

### Option 2: Manual Setup

If you prefer manual setup or need more control:

#### Step 1: Create a DPoP-Enabled OIDC Application

1. Sign in to your Okta Admin Console
2. Go to **Applications** > **Applications** > **Create App Integration**
3. Select **OIDC - OpenID Connect**
4. Choose **Web Application**
5. Configure the application:
   - **Name:** `DPoP_Test_App` (or any name you prefer)
   - **Grant types:** Check **Client Credentials**
   - **Token Endpoint Authentication Method:** Select `private_key_jwt`
   - **Enable DPoP Bound Access Tokens:** ✅ **Enable this option** (critical!)
6. Click **Save**
7. Note the **Client ID** (e.g., `0oaXXXXXXXXXXXXXXXXX`)

#### Step 2: Generate RSA Key Pair

Generate an RSA 3072-bit key pair for signing client assertions and DPoP proofs:

```bash
# Generate private key (3072-bit RSA)
openssl genrsa -out dpop_test_private_key.pem 3072

# Generate corresponding public key
openssl rsa -in dpop_test_private_key.pem -pubout -out dpop_test_public_key.pem

# Extract public JWK (optional, for verification)
python generate_dpop_keys.py --from-pem dpop_test_private_key.pem
```

**Security:** Keep `dpop_test_private_key.pem` secure and never commit it to version control (it's gitignored).

#### Step 3: Create Configuration File

Create a file named `dpop_test_config.py` in the project root:

```python
# dpop_test_config.py
# This file is gitignored - safe for local testing with real credentials

DPOP_CONFIG = {
    'orgUrl': 'https://xxxxx.okta.com',  # Replace with your org URL
    'authorizationMode': 'PrivateKey',
    'clientId': '0oaXXXXXXXXXXXXXXXXX',  # Replace with your OIDC app client ID
    'scopes': ['okta.users.read', 'okta.apps.read', 'okta.groups.read'],
    'privateKey': open('dpop_test_private_key.pem').read(),  # Path to your private key
    'dpopEnabled': True,
    'dpopKeyRotationInterval': 3600  # 1 hour (in seconds)
}
```

**Important:** Do NOT commit `dpop_test_config.py` - it contains sensitive credentials.

### Option 3: Environment Variables

Alternatively, configure via environment variables:

```bash
# Set Okta org URL
export OKTA_CLIENT_ORGURL="https://xxxxx.okta.com"

# Set DPoP client ID
export DPOP_CLIENT_ID="0oaXXXXXXXXXXXXXXXXX"

# Set DPoP private key (from file)
export DPOP_PRIVATE_KEY="$(cat dpop_test_private_key.pem)"
```

Then run tests:
```bash
pytest tests/integration/test_dpop_it.py -v
```

### Option 4: Using Cassettes (No Setup Needed)

If you just want to run tests **without a live Okta org**, you can use the pre-recorded VCR cassettes:

```bash
pytest tests/integration/test_dpop_it.py -v
```

The tests will automatically use the cassettes in `tests/integration/cassettes/` and run in offline mode.

## Running Tests

### Run All DPoP Integration Tests

```bash
pytest tests/integration/test_dpop_it.py -v
```

### Run Specific Test

```bash
# Run only the token request test
pytest tests/integration/test_dpop_it.py::TestDPoPIntegration::test_get_dpop_access_token -v

# Run only the API call test
pytest tests/integration/test_dpop_it.py::TestDPoPIntegration::test_api_call_with_dpop -v
```

### Run with Live Okta Org (Skip Cassettes)

To force tests to use a live Okta org and skip cassettes:

```bash
MOCK_TESTS=false pytest tests/integration/test_dpop_it.py -v
```

### Re-record Cassettes

To update cassettes with fresh API responses from your Okta org:

```bash
pytest tests/integration/test_dpop_it.py -v --record-mode=rewrite
```

**Note:** This will overwrite existing cassettes. Ensure credentials are sanitized before committing.

### Run with Debug Logging

To see detailed DPoP flow (JWT generation, nonce handling, etc.):

```bash
pytest tests/integration/test_dpop_it.py -v -s --log-cli-level=DEBUG
```

## Test Coverage

The integration tests cover the following scenarios:

1. **OAuth Token Request with DPoP**
   - Request DPoP-bound access token
   - Handle nonce challenge (400 → retry with nonce → 200)
   - Verify `token_type: "DPoP"` returned

2. **API Calls with DPoP-Bound Tokens**
   - Make API requests with DPoP proof JWTs
   - Include `ath` (access token hash) claim
   - Verify `DPoP` header is sent
   - Verify `x-okta-user-agent-extended: isDPoP:true` header

3. **Nonce Handling**
   - Store nonce from 400 response
   - Include nonce in retry requests
   - Update nonce from successful responses

4. **Key Rotation**
   - Generate new RSA key pair
   - Clear nonce (tied to old key)
   - Continue operation with new keys

5. **Error Handling**
   - Invalid nonce
   - Expired DPoP proof
   - Token/proof mismatch

6. **Token Reuse and Caching**
   - Cache DPoP token + type atomically
   - Reuse token for multiple API calls
   - Regenerate DPoP proof per request

## Configuration Reference

### Required Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `orgUrl` | string | Okta org URL | `https://dev-xxxxx.okta.com` |
| `authorizationMode` | string | Must be `PrivateKey` for DPoP | `PrivateKey` |
| `clientId` | string | OIDC application client ID | `0oaXXXXXXXXXXXXXXXXX` |
| `scopes` | list | OAuth scopes | `['okta.users.read', 'okta.apps.read']` |
| `privateKey` | string | RSA private key (PEM format) | See Step 2 |
| `dpopEnabled` | boolean | Enable DPoP | `True` |

### Optional Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `dpopKeyRotationInterval` | int | `86400` | Key rotation interval in seconds (24 hours) |

## File Structure

```
okta-sdk-python/
├── tests/
│   ├── DPOP_INTEGRATION_TEST_SETUP.md   ← This file
│   ├── integration/
│   │   ├── test_dpop_it.py              ← DPoP integration tests
│   │   └── cassettes/
│   │       ├── test_get_dpop_access_token.yaml
│   │       ├── test_api_call_with_dpop.yaml
│   │       └── test_dpop_nonce_handling.yaml
│   └── ...
├── dpop_test_config.py          ← Created by setup script (gitignored)
├── dpop_test_private_key.pem    ← Generated RSA private key (gitignored)
├── dpop_test_public_key.pem     ← Generated RSA public key (gitignored)
├── dpop_test_public_jwk.json    ← Generated public JWK (gitignored)
└── setup_dpop_test_app.py       ← Automated setup script
```

## Security Best Practices

### ✅ Safe to Commit

- `tests/integration/test_dpop_it.py` - No hardcoded credentials
- `tests/integration/cassettes/*.yaml` - Sanitized responses
- `tests/DPOP_INTEGRATION_TEST_SETUP.md` - This file (documentation only)
- `setup_dpop_test_app.py` - Setup script (no credentials)

### ❌ NEVER Commit

- `dpop_test_config.py` - Contains real credentials (gitignored)
- `dpop_test_private_key.pem` - RSA private key (gitignored)
- `dpop_test_public_key.pem` - RSA public key (gitignored)
- `dpop_test_public_jwk.json` - Public JWK (gitignored)

### Cassette Sanitization

When recording new cassettes, ensure the following are sanitized:

- **Access tokens** → `sanitized_access_token`
- **Client assertions** → `sanitized_client_assertion_jwt`
- **DPoP proofs** → `sanitized_dpop_proof_jwt`
- **Org URLs** → `https://example.okta.com`
- **Client IDs** → `0oaEXAMPLECLIENTID`
- **Nonces** → `sanitized_nonce_value`

## Troubleshooting

### Issue: `ImportError: cannot import name 'DPOP_CONFIG'`

**Cause:** `dpop_test_config.py` not found.

**Solution:** Run `python setup_dpop_test_app.py` or create the file manually (see Option 2).

---

### Issue: `DPoP was enabled but server returned Bearer token`

**Cause:** DPoP is not enabled for the OIDC application in Okta.

**Solution:**
1. Go to your OIDC app in Okta Admin Console
2. Edit the app settings
3. **Enable** "DPoP Bound Access Tokens"
4. Save and retry

---

### Issue: `use_dpop_nonce` error even after retry

**Cause:** Nonce may have rotated during retry, or server configuration issue.

**Solution:**
- Check server logs for nonce rotation policy
- Ensure application is correctly configured for DPoP
- Try regenerating keys: `python setup_dpop_test_app.py`

---

### Issue: `SECURITY VIOLATION: Private key components found in JWK`

**Cause:** Critical bug in JWK export logic.

**Solution:** This should never happen. If you see this error, please file an issue with:
- Python version
- `jwcrypto` version
- `Cryptodome` version
- Full stack trace

---

### Issue: Cassettes not found

**Cause:** Running tests for the first time or cassettes were deleted.

**Solution:**
- Configure live org (Option 1, 2, or 3)
- Run tests with `--record-mode=rewrite` to create new cassettes

---

## Advanced Usage

### Custom Key Rotation Interval

To test key rotation with a shorter interval:

```python
DPOP_CONFIG = {
    # ...other config...
    'dpopKeyRotationInterval': 300  # 5 minutes
}
```

### Multiple Org Testing

To test against multiple Okta orgs, create separate config files:

```bash
dpop_test_config_dev.py
dpop_test_config_staging.py
dpop_test_config_prod.py
```

Then modify the test to load the appropriate config.

## References

- **RFC 9449** - OAuth 2.0 Demonstrating Proof of Possession: https://datatracker.ietf.org/doc/html/rfc9449
- **Okta DPoP Guide**: https://developer.okta.com/docs/guides/dpop/
- **.NET SDK DPoP PR**: https://github.com/okta/okta-sdk-dotnet/pull/855
- **Python SDK Repository**: https://github.com/okta/okta-sdk-python

## Support

For issues or questions about the DPoP integration tests:

1. Check this guide and the troubleshooting section
2. Review the test file: `tests/integration/test_dpop_it.py`
3. Check existing GitHub issues: https://github.com/okta/okta-sdk-python/issues
4. File a new issue with:
   - Python version
   - SDK version
   - Detailed error message
   - Steps to reproduce

---

**Last Updated:** March 10, 2026

