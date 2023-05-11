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
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.ConnectionStateCreateOrUpdate(
    connection_id='15ceb4d6-e1ea-4e0f-b5ae-df2acab58b99',
    connection_state=shared.ConnectionState(
        connection_id='1c926ddb-5894-461e-b421-cbe6d9502f0e',
        global_state=shared.GlobalState(
            shared_state={
                "error": 'ratione',
                "perferendis": 'distinctio',
                "voluptas": 'sint',
            },
            stream_states=[
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Lee Runte',
                        namespace='esse',
                    ),
                    stream_state={
                        "delectus": 'quos',
                    },
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Miss Jon Bailey I',
                        namespace='occaecati',
                    ),
                    stream_state={
                        "veritatis": 'ex',
                    },
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Ms. Tracey D'Amore',
                        namespace='blanditiis',
                    ),
                    stream_state={
                        "voluptates": 'minus',
                        "autem": 'vel',
                        "beatae": 'quos',
                    },
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Latoya West',
                        namespace='suscipit',
                    ),
                    stream_state={
                        "unde": 'debitis',
                        "quidem": 'magnam',
                    },
                ),
            ],
        ),
        state={
            "accusamus": 'quod',
        },
        state_type=shared.ConnectionStateTypeEnum.GLOBAL,
        stream_state=[
            shared.StreamState(
                stream_descriptor=shared.StreamDescriptor(
                    name='Cameron Wehner',
                    namespace='rerum',
                ),
                stream_state={
                    "nam": 'ullam',
                },
            ),
            shared.StreamState(
                stream_descriptor=shared.StreamDescriptor(
                    name='Lois Ondricka',
                    namespace='error',
                ),
                stream_state={
                    "reprehenderit": 'eligendi',
                },
            ),
        ],
    ),
)

res = s.state.create_or_update_state(req)

if res.connection_state is not None:
    # handle response
```

## get_state

Fetch the current state for a connection.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.ConnectionIDRequestBody(
    connection_id='baaf4452-c484-42c9-b2ad-32dafe81a88f',
)

res = s.state.get_state(req)

if res.connection_state is not None:
    # handle response
```
