# source_oauth

## Overview

Source OAuth related resources to delegate access from user.

### Available Operations

* [complete_source_o_auth](#complete_source_o_auth) - Given a source def ID generate an access/refresh token etc.
* [get_source_o_auth_consent](#get_source_o_auth_consent) - Given a source connector definition ID, return the URL to the consent screen where to redirect the user to.
* [set_instancewide_source_oauth_params](#set_instancewide_source_oauth_params) - Sets instancewide variables to be used for the oauth flow when creating this source. When set, these variables will be injected into a connector's configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company's Google Ads developer_token, client_id, and client_secret without the user having to know about these variables.


## complete_source_o_auth

Given a source def ID generate an access/refresh token etc.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.CompleteSourceOauthRequest(
    o_auth_input_configuration='nam',
    query_params={
        "vitae": 'mollitia',
    },
    redirect_url='asperiores',
    source_definition_id='dd788624-189e-4b44-873f-5033f19dbf12',
    source_id='5ce4152e-ab9c-4d7e-9224-a6a0e123b784',
    workspace_id='7ec59e1f-67f3-4c4c-8e4b-6d7696ff3c57',
)

res = s.source_oauth.complete_source_o_auth(req)

if res.complete_o_auth_response is not None:
    # handle response
```

## get_source_o_auth_consent

Given a source connector definition ID, return the URL to the consent screen where to redirect the user to.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceOauthConsentRequest(
    o_auth_input_configuration='eius',
    redirect_url='dignissimos',
    source_definition_id='501357e4-4f51-4f8b-884c-3197e193a245',
    source_id='467f9487-4c2d-45cc-8972-233e66bd8fe5',
    workspace_id='d00b979e-f203-4873-a059-0ccc10964003',
)

res = s.source_oauth.get_source_o_auth_consent(req)

if res.o_auth_consent_read is not None:
    # handle response
```

## set_instancewide_source_oauth_params

Sets instancewide variables to be used for the oauth flow when creating this source. When set, these variables will be injected into a connector's configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company's Google Ads developer_token, client_id, and client_secret without the user having to know about these variables.


### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SetInstancewideSourceOauthParamsRequestBody(
    params={
        "sequi": 'rerum',
    },
    source_definition_id='3e5044f6-5fe7-42dc-8077-d0cc3f408efc',
)

res = s.source_oauth.set_instancewide_source_oauth_params(req)

if res.status_code == 200:
    # handle response
```
