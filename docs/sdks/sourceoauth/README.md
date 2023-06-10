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
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.CompleteSourceOauthRequest(
    o_auth_input_configuration='incidunt',
    query_params={
        "sunt": 'ullam',
        "quam": 'illum',
        "voluptates": 'officia',
        "est": 'in',
    },
    redirect_url='illo',
    source_definition_id='70f445ac-cf66-47aa-b9bb-ad185fe431d6',
    source_id='bf5c838f-bb8c-420c-b67f-c4b425e99e62',
    workspace_id='34c9f7b7-9dfe-4b77-a5c3-8d4baf91e506',
)

res = s.source_oauth.complete_source_o_auth(req)

if res.complete_o_auth_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.CompleteSourceOauthRequest](../../models/shared/completesourceoauthrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CompleteSourceOAuthResponse](../../models/operations/completesourceoauthresponse.md)**


## get_source_o_auth_consent

Given a source connector definition ID, return the URL to the consent screen where to redirect the user to.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceOauthConsentRequest(
    o_auth_input_configuration='eveniet',
    redirect_url='delectus',
    source_definition_id='890a54b4-75f1-46f5-ad38-5a3c4ac631b9',
    source_id='9e26ced8-f9fd-4b94-90f6-3bbf817837b0',
    workspace_id='1afdd788-6241-489e-b448-73f5033f19db',
)

res = s.source_oauth.get_source_o_auth_consent(req)

if res.o_auth_consent_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [shared.SourceOauthConsentRequest](../../models/shared/sourceoauthconsentrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetSourceOAuthConsentResponse](../../models/operations/getsourceoauthconsentresponse.md)**


## set_instancewide_source_oauth_params

Sets instancewide variables to be used for the oauth flow when creating this source. When set, these variables will be injected into a connector's configuration before any interaction with the connector image itself. This enables running oauth flows with consistent variables e.g: the company's Google Ads developer_token, client_id, and client_secret without the user having to know about these variables.


### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SetInstancewideSourceOauthParamsRequestBody(
    params={
        "quasi": 'consequuntur',
        "nemo": 'nobis',
        "debitis": 'labore',
        "veritatis": 'minima',
    },
    source_definition_id='2eab9cd7-e522-44a6-a0e1-23b7847ec59e',
)

res = s.source_oauth.set_instancewide_source_oauth_params(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [shared.SetInstancewideSourceOauthParamsRequestBody](../../models/shared/setinstancewidesourceoauthparamsrequestbody.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.SetInstancewideSourceOauthParamsResponse](../../models/operations/setinstancewidesourceoauthparamsresponse.md)**

