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
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

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

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.SaveStatsRequestBody](../../models/shared/savestatsrequestbody.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.SaveStatsResponse](../../models/operations/savestatsresponse.md)**


## save_sync_config

For worker to save the AttemptSyncConfig for an attempt.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SaveAttemptSyncConfigRequestBody(
    attempt_number=639921,
    job_id=582020,
    sync_config=shared.AttemptSyncConfig(
        destination_configuration='fugit',
        source_configuration='deleniti',
        state=shared.ConnectionState(
            connection_id='fc816742-cb73-4920-9929-396fea7596eb',
            global_state=shared.GlobalState(
                shared_state=shared.StateBlob(),
                stream_states=[
                    shared.StreamState(
                        stream_descriptor=shared.StreamDescriptor(
                            name='Lela Orn',
                            namespace='dolores',
                        ),
                        stream_state=shared.StateBlob(),
                    ),
                ],
            ),
            state=shared.StateBlob(),
            state_type=shared.ConnectionStateType.GLOBAL,
            stream_state=[
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Della Halvorson',
                        namespace='minima',
                    ),
                    stream_state=shared.StateBlob(),
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Brian Kessler',
                        namespace='sapiente',
                    ),
                    stream_state=shared.StateBlob(),
                ),
            ],
        ),
    ),
)

res = s.attempt.save_sync_config(req)

if res.internal_operation_result is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [shared.SaveAttemptSyncConfigRequestBody](../../models/shared/saveattemptsyncconfigrequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.SaveSyncConfigResponse](../../models/operations/savesyncconfigresponse.md)**


## set_workflow_in_attempt

For worker to register the workflow id in attempt.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SetWorkflowInAttemptRequestBody(
    attempt_number=102044,
    job_id=652790,
    processing_task_queue='dolorem',
    workflow_id='culpa',
)

res = s.attempt.set_workflow_in_attempt(req)

if res.internal_operation_result is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [shared.SetWorkflowInAttemptRequestBody](../../models/shared/setworkflowinattemptrequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.SetWorkflowInAttemptResponse](../../models/operations/setworkflowinattemptresponse.md)**

