# attempt

## Overview

Interactions with attempt related resources.

### Available Operations

* [save_stats](#save_stats) - For worker to set sync stats of a running attempt.
* [save_sync_config](#save_sync_config) - For worker to save the AttemptSyncConfig for an attempt.
* [set_workflow_in_attempt](#set_workflow_in_attempt) - For worker to register the workflow id in attempt.

## save_stats

For worker to set sync stats of a running attempt.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SaveStatsRequestBody(
    attempt_number=392785,
    job_id=925597,
    stats=shared.AttemptStats(
        bytes_emitted=836079,
        estimated_bytes=71036,
        estimated_records=337396,
        records_committed=87129,
        records_emitted=648172,
        state_messages_emitted=20218,
    ),
    stream_stats=[
        shared.AttemptStreamStats(
            stats=shared.AttemptStats(
                bytes_emitted=832620,
                estimated_bytes=957156,
                estimated_records=778157,
                records_committed=140350,
                records_emitted=870013,
                state_messages_emitted=870088,
            ),
            stream_name='maiores',
            stream_namespace='molestiae',
        ),
        shared.AttemptStreamStats(
            stats=shared.AttemptStats(
                bytes_emitted=799159,
                estimated_bytes=800911,
                estimated_records=461479,
                records_committed=520478,
                records_emitted=780529,
                state_messages_emitted=678880,
            ),
            stream_name='dicta',
            stream_namespace='nam',
        ),
    ],
)

res = s.attempt.save_stats(req)

if res.internal_operation_result is not None:
    # handle response
```

## save_sync_config

For worker to save the AttemptSyncConfig for an attempt.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SaveAttemptSyncConfigRequestBody(
    attempt_number=639921,
    job_id=582020,
    sync_config=shared.AttemptSyncConfig(
        destination_configuration='fugit',
        source_configuration='deleniti',
        state=shared.ConnectionState(
            connection_id='fc816742-cb73-4920-9929-396fea7596eb',
            global_state=shared.GlobalState(
                shared_state={
                    "ipsa": 'reiciendis',
                },
                stream_states=[
                    shared.StreamState(
                        stream_descriptor=shared.StreamDescriptor(
                            name='Cameron Dach',
                            namespace='explicabo',
                        ),
                        stream_state={
                            "enim": 'omnis',
                            "nemo": 'minima',
                            "excepturi": 'accusantium',
                            "iure": 'culpa',
                        },
                    ),
                    shared.StreamState(
                        stream_descriptor=shared.StreamDescriptor(
                            name='Darrin Brakus',
                            namespace='culpa',
                        ),
                        stream_state={
                            "repellat": 'mollitia',
                        },
                    ),
                    shared.StreamState(
                        stream_descriptor=shared.StreamDescriptor(
                            name='Francis Jerde',
                            namespace='velit',
                        ),
                        stream_state={
                            "quia": 'quis',
                            "vitae": 'laborum',
                            "animi": 'enim',
                        },
                    ),
                ],
            ),
            state={
                "quo": 'sequi',
            },
            state_type=shared.ConnectionStateTypeEnum.NOT_SET,
            stream_state=[
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Miss Rufus Ankunding',
                        namespace='laborum',
                    ),
                    stream_state={
                        "reiciendis": 'voluptatibus',
                    },
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Jessie Langosh V',
                        namespace='voluptate',
                    ),
                    stream_state={
                        "perferendis": 'doloremque',
                        "reprehenderit": 'ut',
                        "maiores": 'dicta',
                    },
                ),
            ],
        ),
    ),
)

res = s.attempt.save_sync_config(req)

if res.internal_operation_result is not None:
    # handle response
```

## set_workflow_in_attempt

For worker to register the workflow id in attempt.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SetWorkflowInAttemptRequestBody(
    attempt_number=359444,
    job_id=296140,
    processing_task_queue='iusto',
    workflow_id='dicta',
)

res = s.attempt.set_workflow_in_attempt(req)

if res.internal_operation_result is not None:
    # handle response
```
