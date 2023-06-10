# state

## Overview

Interactions with state related resources.

### Available Operations

* [create_or_update_state](#create_or_update_state) - Create or update the state for a connection.
* [get_state](#get_state) - Fetch the current state for a connection.

## create_or_update_state

Create or update the state for a connection.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.ConnectionStateCreateOrUpdate(
    connection_id='1f67f3c4-cce4-4b6d-b696-ff3c57475013',
    connection_state=shared.ConnectionState(
        connection_id='57e44f51-f8b0-484c-b197-e193a245467f',
        global_state=shared.GlobalState(
            shared_state=shared.StateBlob(),
            stream_states=[
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Naomi Kozey',
                        namespace='fugit',
                    ),
                    stream_state=shared.StateBlob(),
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Vernon Rohan',
                        namespace='perspiciatis',
                    ),
                    stream_state=shared.StateBlob(),
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Lois Dibbert',
                        namespace='saepe',
                    ),
                    stream_state=shared.StateBlob(),
                ),
            ],
        ),
        state=shared.StateBlob(),
        state_type=shared.ConnectionStateType.STREAM,
        stream_state=[
            shared.StreamState(
                stream_descriptor=shared.StreamDescriptor(
                    name='Nicolas Legros',
                    namespace='corporis',
                ),
                stream_state=shared.StateBlob(),
            ),
            shared.StreamState(
                stream_descriptor=shared.StreamDescriptor(
                    name='Richard Bartell',
                    namespace='odio',
                ),
                stream_state=shared.StateBlob(),
            ),
        ],
    ),
)

res = s.state.create_or_update_state(req)

if res.connection_state is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.ConnectionStateCreateOrUpdate](../../models/shared/connectionstatecreateorupdate.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateOrUpdateStateResponse](../../models/operations/createorupdatestateresponse.md)**


## get_state

Fetch the current state for a connection.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.ConnectionIDRequestBody(
    connection_id='9ef20387-3205-490c-8c10-96400313b3e5',
)

res = s.state.get_state(req)

if res.connection_state is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.ConnectionIDRequestBody](../../models/shared/connectionidrequestbody.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetStateResponse](../../models/operations/getstateresponse.md)**

