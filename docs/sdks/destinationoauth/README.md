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
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.CompleteDestinationOAuthRequest(
    destination_definition_id='75f1400e-764a-4d73-b4ec-1b781b36a080',
    destination_id='88d100ef-ada2-400e-b042-2eb2164cf9ab',
    o_auth_input_configuration='totam',
    query_params={
        "aliquid": 'ea',
    },
    redirect_url='impedit',
    workspace_id='723ffda9-e06b-4ee4-825c-1fc0e115c80b',
)

res = s.destination_oauth.complete_destination_o_auth(req)

if res.complete_o_auth_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [shared.CompleteDestinationOAuthRequest](../../models/shared/completedestinationoauthrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.CompleteDestinationOAuthResponse](../../models/operations/completedestinationoauthresponse.md)**


## get_destination_o_auth_consent

Given a destination connector definition ID, return the URL to the consent screen where to redirect the user to.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationOauthConsentRequest(
    destination_definition_id='ff918544-ec42-4def-8ce8-f1977773e635',
    destination_id='62a7b408-f05e-43d4-8fda-f313a1f5fd94',
    o_auth_input_configuration='explicabo',
    redirect_url='ipsam',
    workspace_id='9c0b36f2-5ea9-444f-bb75-6c11f6c37a51',
)

res = s.destination_oauth.get_destination_o_auth_consent(req)

if res.o_auth_consent_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [shared.DestinationOauthConsentRequest](../../models/shared/destinationoauthconsentrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetDestinationOAuthConsentResponse](../../models/operations/getdestinationoauthconsentresponse.md)**


## set_instancewide_destination_oauth_params

Sets instancewide variables to be used for the oauth flow when creating this destination. When set, these variables will be injected into a connector's configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company's Google Ads developer_token, client_id, and client_secret without the user having to know about these variables.


### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SetInstancewideDestinationOauthParamsRequestBody(
    destination_definition_id='26243835-bbc0-45a2-ba45-cefc5fde10a0',
    params={
        "necessitatibus": 'quia',
        "dicta": 'vel',
        "perspiciatis": 'debitis',
        "ullam": 'architecto',
    },
)

res = s.destination_oauth.set_instancewide_destination_oauth_params(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                          | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                          | [shared.SetInstancewideDestinationOauthParamsRequestBody](../../models/shared/setinstancewidedestinationoauthparamsrequestbody.md) | :heavy_check_mark:                                                                                                                 | The request object to use for the request.                                                                                         |


### Response

**[operations.SetInstancewideDestinationOauthParamsResponse](../../models/operations/setinstancewidedestinationoauthparamsresponse.md)**

