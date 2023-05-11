# destination_oauth

## Overview

Source OAuth related resources to delegate access from user.

### Available Operations

* [complete_destination_o_auth](#complete_destination_o_auth) - Given a destination def ID generate an access/refresh token etc.
* [get_destination_o_auth_consent](#get_destination_o_auth_consent) - Given a destination connector definition ID, return the URL to the consent screen where to redirect the user to.
* [set_instancewide_destination_oauth_params](#set_instancewide_destination_oauth_params) - Sets instancewide variables to be used for the oauth flow when creating this destination. When set, these variables will be injected into a connector's configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company's Google Ads developer_token, client_id, and client_secret without the user having to know about these variables.


## complete_destination_o_auth

Given a destination def ID generate an access/refresh token etc.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.CompleteDestinationOAuthRequest(
    destination_definition_id='0e115c80-bff9-4185-84ec-42defcce8f19',
    destination_id='77773e63-562a-47b4-88f0-5e3d48fdaf31',
    o_auth_input_configuration='nesciunt',
    query_params={
        "illo": 'repellat',
        "nemo": 'doloribus',
        "possimus": 'unde',
    },
    redirect_url='incidunt',
    workspace_id='259c0b36-f25e-4a94-8f3b-756c11f6c37a',
)

res = s.destination_oauth.complete_destination_o_auth(req)

if res.complete_o_auth_response is not None:
    # handle response
```

## get_destination_o_auth_consent

Given a destination connector definition ID, return the URL to the consent screen where to redirect the user to.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationOauthConsentRequest(
    destination_definition_id='51262438-35bb-4c05-a23a-45cefc5fde10',
    destination_id='a0ce2169-e510-4019-86dc-5e34762799bf',
    o_auth_input_configuration='facilis',
    redirect_url='quidem',
    workspace_id='e6949fb2-bb4e-4cae-ac3d-5db3adebd5da',
)

res = s.destination_oauth.get_destination_o_auth_consent(req)

if res.o_auth_consent_read is not None:
    # handle response
```

## set_instancewide_destination_oauth_params

Sets instancewide variables to be used for the oauth flow when creating this destination. When set, these variables will be injected into a connector's configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company's Google Ads developer_token, client_id, and client_secret without the user having to know about these variables.


### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SetInstancewideDestinationOauthParamsRequestBody(
    destination_definition_id='ea4c506a-8aa9-44c0-a644-cf5e9d9a4578',
    params={
        "facere": 'impedit',
        "quasi": 'deserunt',
        "quod": 'laboriosam',
    },
)

res = s.destination_oauth.set_instancewide_destination_oauth_params(req)

if res.status_code == 200:
    # handle response
```
