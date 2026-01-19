# Okta SDK Python - Pagination Guide

This guide demonstrates how to use pagination with the Okta SDK for Python.

## Overview

The Okta API returns paginated results for list operations (users, applications, groups, etc.). The SDK now includes built-in pagination utilities to make this easy!

## How Okta Pagination Works

Okta uses cursor-based pagination with the `after` parameter. The `Link` response header contains the URL for the next page:

```
Link: <https://your-domain.okta.com/api/v1/users?after=CURSOR>; rel="next"
```

## Quick Start - Using SDK Pagination Helpers (Recommended)

The SDK now provides helper functions that handle pagination automatically:

### Method 1: `paginate_all()` - Iterate Through All Items

```python
from okta.client import Client as OktaClient
from okta import paginate_all

async def fetch_all_users(okta_client):
    """Fetch all users automatically"""
    all_users = []
    
    # Automatically paginate through all users
    async for user in paginate_all(
        okta_client.list_users_with_http_info,
        limit=200  # Items per page
    ):
        all_users.append(user)
        print(f"User: {user.profile.email}")
    
    return all_users
```

### Method 2: `paginate_pages()` - Process in Batches

```python
from okta import paginate_pages

async def process_users_in_batches(okta_client):
    """Process users page by page"""
    
    async for page_data, page_num, has_more in paginate_pages(
        okta_client.list_users_with_http_info,
        limit=100,
        max_pages=5  # Optional: limit number of pages
    ):
        print(f"Processing page {page_num} with {len(page_data)} users")
        
        # Process the batch
        for user in page_data:
            process_user(user)
        
        if not has_more:
            print("Reached the last page")
```

### Method 3: `PaginationHelper` - Manual Control

```python
from okta import PaginationHelper

async def manual_pagination(okta_client):
    """Manually control pagination"""
    after_cursor = None
    
    while True:
        users, response, error = await okta_client.list_users_with_http_info(
            limit=200,
            after=after_cursor
        )
        
        if error or not users:
            break
        
        # Process users
        for user in users:
            print(user.profile.email)
        
        # Get next cursor using SDK helper
        after_cursor = PaginationHelper.extract_next_cursor(response.headers)
        
        if not after_cursor:
            break  # No more pages
```

## SDK Pagination Utilities Reference

### `paginate_all(api_method, limit, max_pages, **kwargs)`

Automatically paginate through all results, yielding individual items.

**Parameters:**
- `api_method`: The `_with_http_info` method to call
- `limit`: Number of results per page (default: 200)
- `max_pages`: Maximum pages to fetch (default: None = unlimited)
- `**kwargs`: Additional arguments for the API method

**Yields:** Individual items from all pages

**Example:**
```python
# Fetch all applications with filtering
async for app in paginate_all(
    client.list_applications_with_http_info,
    limit=100,
    filter='status eq "ACTIVE"'
):
    print(app.label)
```

### `paginate_pages(api_method, limit, max_pages, **kwargs)`

Paginate through results, yielding complete pages.

**Parameters:**
- Same as `paginate_all`

**Yields:** Tuples of `(page_data, page_number, has_more)`

**Example:**
```python
async for page, page_num, has_more in paginate_pages(
    client.list_groups_with_http_info,
    limit=50
):
    print(f"Page {page_num}: {len(page)} groups")
    # Process page...
```

### `PaginationHelper.extract_next_cursor(headers)`

Extract the pagination cursor from response headers.

**Parameters:**
- `headers`: HTTP response headers dictionary

**Returns:** The next page cursor string, or `None` if no more pages

**Example:**
```python
users, response, error = await client.list_users_with_http_info(limit=100)
next_cursor = PaginationHelper.extract_next_cursor(response.headers)
if next_cursor:
    print(f"Next page available with cursor: {next_cursor}")
```

### `PaginationHelper.has_next_page(headers)`

Check if more pages are available.

**Returns:** `True` if another page exists, `False` otherwise

### `PaginationHelper.extract_pagination_info(headers)`

Extract all pagination information.

**Returns:** Dict with `{'next': cursor, 'prev': cursor, 'self': cursor}`

## Manual Implementation Example

If you need more control, you can implement pagination manually:

### Basic Pagination Pattern

```python
async def paginate_users(okta_client):
    """Fetch all users using pagination"""
    all_users = []
    after_cursor = None
    
    while True:
        # Use _with_http_info to get response headers
        users, response, error = await okta_client.list_users_with_http_info(
            limit=200,  # Maximum per page
            after=after_cursor
        )
        
        if error or not users:
            break
        
        all_users.extend(users)
        
        # Extract next cursor from Link header
        after_cursor = extract_next_cursor(response.headers)
        
        if not after_cursor:
            break  # No more pages
    
    return all_users
```

### Extracting the Next Cursor

```python
def extract_next_cursor(headers):
    """Extract the 'after' cursor from Link header"""
    link_header = headers.get('Link') or headers.get('link')
    
    if not link_header:
        return None
    
    # Parse Link header: <URL>; rel="next"
    links = link_header.split(',')
    for link in links:
        if 'rel="next"' in link:
            url = link.split(';')[0].strip('<>').strip()
            if 'after=' in url:
                after_param = url.split('after=')[1]
                return after_param.split('&')[0]
    
    return None
```

## Complete Example

See `comprehensive_okta_test.py` for a complete working example. Key methods:

- `list_users_with_pagination()` - Demonstrates user pagination (Step 7b)
- `list_applications_with_pagination()` - Demonstrates application pagination (Step 7c)
- `_extract_next_cursor()` - Helper method to parse Link headers

## Running the Example

```bash
# Install dependencies
pip install okta-sdk-python

# Update credentials in comprehensive_okta_test.py
# Then run:
python comprehensive_okta_test.py
```

## Key Points

1. **Use `_with_http_info` methods**: These return `(data, response, error)` tuples that include headers
2. **Parse the Link header**: Extract the `after` cursor for the next page
3. **Set appropriate limits**: Maximum is usually 200 per page
4. **Handle rate limits**: Okta has rate limits, so implement backoff strategies for production

## Available Paginated Methods

Most list operations support pagination:

- `list_users_with_http_info()`
- `list_applications_with_http_info()`
- `list_groups_with_http_info()`
- `list_policies_with_http_info()`
- And many more...

## Complete Working Examples

### Example 1: Fetch All Users (Simple)

```python
import asyncio
from okta.client import Client as OktaClient
from okta import paginate_all

async def main():
    config = {
        'orgUrl': 'https://your-domain.okta.com',
        'token': 'your-api-token',
    }
    
    client = OktaClient(config)
    
    # Collect all users
    all_users = [user async for user in paginate_all(
        client.list_users_with_http_info,
        limit=200
    )]
    
    print(f"Total users: {len(all_users)}")
    
if __name__ == "__main__":
    asyncio.run(main())
```

### Example 2: Process Users in Batches (Memory Efficient)

```python
import asyncio
from okta.client import Client as OktaClient
from okta import paginate_pages

async def process_users_in_batches():
    config = {
        'orgUrl': 'https://your-domain.okta.com',
        'token': 'your-api-token',
    }
    
    client = OktaClient(config)
    total_processed = 0
    
    async for page_data, page_num, has_more in paginate_pages(
        client.list_users_with_http_info,
        limit=200
    ):
        # Process this batch
        print(f"Processing page {page_num}: {len(page_data)} users")
        
        for user in page_data:
            # Do something with each user
            print(f"  - {user.profile.email}")
            total_processed += 1
        
        # Optional: add delay for rate limiting
        if has_more:
            await asyncio.sleep(0.5)
    
    print(f"Total processed: {total_processed} users")
    
if __name__ == "__main__":
    asyncio.run(process_users_in_batches())
```

### Example 3: Filtered Pagination with Error Handling

```python
import asyncio
from okta.client import Client as OktaClient
from okta import paginate_all

async def fetch_active_applications():
    config = {
        'orgUrl': 'https://your-domain.okta.com',
        'token': 'your-api-token',
    }
    
    client = OktaClient(config)
    active_apps = []
    
    try:
        async for app in paginate_all(
            client.list_applications_with_http_info,
            limit=100,
            filter='status eq "ACTIVE"',
            max_pages=10  # Safety limit
        ):
            active_apps.append(app)
            print(f"Found: {app.label}")
    
    except Exception as e:
        print(f"Error during pagination: {e}")
    
    print(f"Total active applications: {len(active_apps)}")
    return active_apps

if __name__ == "__main__":
    asyncio.run(fetch_active_applications())
```

### Example 4: Manual Pagination with SDK Helper

```python
import asyncio
from okta.client import Client as OktaClient
from okta import PaginationHelper

async def manual_pagination_example():
    config = {
        'orgUrl': 'https://your-domain.okta.com',
        'token': 'your-api-token',
    }
    
    client = OktaClient(config)
    
    after_cursor = None
    page_count = 0
    total_groups = 0
    
    while True:
        # Fetch page
        groups, response, error = await client.list_groups_with_http_info(
            limit=50,
            after=after_cursor
        )
        
        if error:
            print(f"Error: {error}")
            break
        
        if not groups:
            break
        
        page_count += 1
        total_groups += len(groups)
        print(f"Page {page_count}: {len(groups)} groups")
        
        # Check for next page using SDK helper
        if not PaginationHelper.has_next_page(response.headers):
            print("Reached last page")
            break
        
        # Get next cursor
        after_cursor = PaginationHelper.extract_next_cursor(response.headers)
        
        # Rate limiting
        await asyncio.sleep(0.5)
    
    print(f"Total: {total_groups} groups across {page_count} pages")

if __name__ == "__main__":
    asyncio.run(manual_pagination_example())
```

## Best Practices

1. **Use SDK helpers**: Prefer `paginate_all()` or `paginate_pages()` for cleaner code
2. **Set appropriate limits**: Use 100-200 per page in production (don't use 5 like in demos)
3. **Handle rate limits**: Add delays between pages or implement exponential backoff
4. **Process incrementally**: For large datasets, use `paginate_pages()` to avoid memory issues
5. **Set safety limits**: Use `max_pages` parameter to prevent runaway pagination
6. **Handle errors**: Always wrap pagination in try-except blocks
7. **Use filtering**: Apply filters to reduce the amount of data fetched

## Additional Resources

- [Okta API Pagination Documentation](https://developer.okta.com/docs/reference/api-overview/#pagination)
- [Okta SDK Python GitHub](https://github.com/okta/okta-sdk-python)

