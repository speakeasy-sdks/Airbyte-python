# internal

### Available Operations

* [create_or_update_state](#create_or_update_state) - Create or update the state for a connection.
* [get_attempt_normalization_statuses_for_job](#get_attempt_normalization_statuses_for_job) - Get normalization status to determine if we can bypass normalization phase
* [save_stats](#save_stats) - For worker to set sync stats of a running attempt.
* [save_sync_config](#save_sync_config) - For worker to save the AttemptSyncConfig for an attempt.
* [set_workflow_in_attempt](#set_workflow_in_attempt) - For worker to register the workflow id in attempt.
* [write_discover_catalog_result](#write_discover_catalog_result) - Should only called from worker, to write result from discover activity back to DB.

## create_or_update_state

Create or update the state for a connection.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.ConnectionStateCreateOrUpdate(
    connection_id='00dec001-ac80-42e2-ac09-ff8f0f816ff3',
    connection_state=shared.ConnectionState(
        connection_id='477c13e9-02c1-4412-9b09-60a668151a47',
        global_state=shared.GlobalState(
            shared_state={
                "deserunt": 'delectus',
            },
            stream_states=[
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Peggy Schneider',
                        namespace='aliquam',
                    ),
                    stream_state={
                        "maiores": 'laudantium',
                        "velit": 'reiciendis',
                        "amet": 'nemo',
                    },
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Adrienne White',
                        namespace='aliquid',
                    ),
                    stream_state={
                        "a": 'nobis',
                        "perspiciatis": 'accusantium',
                        "dicta": 'minus',
                        "commodi": 'eveniet',
                    },
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Geoffrey Powlowski',
                        namespace='fugit',
                    ),
                    stream_state={
                        "sequi": 'eligendi',
                        "asperiores": 'esse',
                    },
                ),
            ],
        ),
        state={
            "sint": 'repellat',
            "a": 'animi',
            "maiores": 'itaque',
        },
        state_type=shared.ConnectionStateTypeEnum.NOT_SET,
        stream_state=[
            shared.StreamState(
                stream_descriptor=shared.StreamDescriptor(
                    name='Sheila Torphy',
                    namespace='saepe',
                ),
                stream_state={
                    "repudiandae": 'accusantium',
                    "officia": 'impedit',
                },
            ),
            shared.StreamState(
                stream_descriptor=shared.StreamDescriptor(
                    name='Mattie Gibson',
                    namespace='nobis',
                ),
                stream_state={
                    "minus": 'quia',
                    "magnam": 'reprehenderit',
                    "quod": 'quos',
                },
            ),
            shared.StreamState(
                stream_descriptor=shared.StreamDescriptor(
                    name='Allen Kozey',
                    namespace='modi',
                ),
                stream_state={
                    "necessitatibus": 'architecto',
                },
            ),
        ],
    ),
)

res = s.internal.create_or_update_state(req)

if res.connection_state is not None:
    # handle response
```

## get_attempt_normalization_statuses_for_job

Get normalization status to determine if we can bypass normalization phase

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.JobIDRequestBody(
    id=564627,
)

res = s.internal.get_attempt_normalization_statuses_for_job(req)

if res.attempt_normalization_status_read_list is not None:
    # handle response
```

## save_stats

For worker to set sync stats of a running attempt.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SaveStatsRequestBody(
    attempt_number=292177,
    job_id=125811,
    stats=shared.AttemptStats(
        bytes_emitted=982991,
        estimated_bytes=205011,
        estimated_records=139745,
        records_committed=936845,
        records_emitted=330596,
        state_messages_emitted=373106,
    ),
    stream_stats=[
        shared.AttemptStreamStats(
            stats=shared.AttemptStats(
                bytes_emitted=350387,
                estimated_bytes=331269,
                estimated_records=469994,
                records_committed=320326,
                records_emitted=394161,
                state_messages_emitted=946808,
            ),
            stream_name='quis',
            stream_namespace='quibusdam',
        ),
    ],
)

res = s.internal.save_stats(req)

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
    attempt_number=366480,
    job_id=382764,
    sync_config=shared.AttemptSyncConfig(
        destination_configuration='pariatur',
        source_configuration='sit',
        state=shared.ConnectionState(
            connection_id='bd0af2df-e13d-4b4f-a2cb-a3f8941aebc0',
            global_state=shared.GlobalState(
                shared_state={
                    "corrupti": 'eaque',
                    "deserunt": 'aliquid',
                    "excepturi": 'magni',
                },
                stream_states=[
                    shared.StreamState(
                        stream_descriptor=shared.StreamDescriptor(
                            name='Rodney Prohaska',
                            namespace='optio',
                        ),
                        stream_state={
                            "minus": 'quo',
                            "quos": 'asperiores',
                            "voluptatum": 'iste',
                            "corporis": 'accusantium',
                        },
                    ),
                    shared.StreamState(
                        stream_descriptor=shared.StreamDescriptor(
                            name='Susan Wyman',
                            namespace='possimus',
                        ),
                        stream_state={
                            "pariatur": 'vel',
                        },
                    ),
                ],
            ),
            state={
                "mollitia": 'quae',
                "quos": 'aperiam',
                "non": 'voluptates',
                "ad": 'aliquam',
            },
            state_type=shared.ConnectionStateTypeEnum.NOT_SET,
            stream_state=[
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Ebony Bode',
                        namespace='est',
                    ),
                    stream_state={
                        "aliquid": 'consectetur',
                    },
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Ian Legros',
                        namespace='recusandae',
                    ),
                    stream_state={
                        "blanditiis": 'numquam',
                        "sequi": 'voluptatum',
                    },
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Olivia Boehm',
                        namespace='quidem',
                    ),
                    stream_state={
                        "porro": 'deserunt',
                        "magni": 'nihil',
                        "voluptas": 'animi',
                    },
                ),
            ],
        ),
    ),
)

res = s.internal.save_sync_config(req)

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
    attempt_number=413780,
    job_id=716,
    processing_task_queue='fuga',
    workflow_id='aut',
)

res = s.internal.set_workflow_in_attempt(req)

if res.internal_operation_result is not None:
    # handle response
```

## write_discover_catalog_result

Should only called from worker, to write result from discover activity back to DB.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceDiscoverSchemaWriteRequestBody(
    catalog=shared.AirbyteCatalog(
        streams=[
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='maxime',
                    cursor_field=[
                        'iste',
                        'ullam',
                    ],
                    destination_sync_mode=shared.DestinationSyncModeEnum.APPEND_DEDUP,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'occaecati',
                            'unde',
                        ],
                        [
                            'nihil',
                        ],
                        [
                            'libero',
                        ],
                        [
                            'quasi',
                            'cumque',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'facere',
                                'facilis',
                                'beatae',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncModeEnum.INCREMENTAL,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'labore',
                        'expedita',
                        'corrupti',
                        'rem',
                    ],
                    json_schema={
                        "officiis": 'cum',
                        "pariatur": 'sapiente',
                        "quo": 'incidunt',
                    },
                    name='Kim Sauer',
                    namespace='occaecati',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'esse',
                            'hic',
                            'maxime',
                            'accusantium',
                        ],
                        [
                            'fugit',
                            'pariatur',
                            'eligendi',
                        ],
                        [
                            'veritatis',
                            'aut',
                            'laudantium',
                            'iusto',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncModeEnum.INCREMENTAL,
                    ],
                ),
            ),
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='tempora',
                    cursor_field=[
                        'rerum',
                    ],
                    destination_sync_mode=shared.DestinationSyncModeEnum.APPEND,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'at',
                            'eum',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'blanditiis',
                                'nihil',
                                'atque',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'deserunt',
                                'atque',
                                'nostrum',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncModeEnum.INCREMENTAL,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'est',
                    ],
                    json_schema={
                        "rem": 'magni',
                        "quae": 'quas',
                    },
                    name='Lloyd Grant',
                    namespace='delectus',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'cumque',
                            'natus',
                            'quaerat',
                        ],
                        [
                            'quia',
                            'officiis',
                            'mollitia',
                            'cumque',
                        ],
                        [
                            'enim',
                            'eum',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncModeEnum.INCREMENTAL,
                        shared.SyncModeEnum.FULL_REFRESH,
                    ],
                ),
            ),
        ],
    ),
    configuration_hash='sit',
    connector_version='odio',
    source_id='cfee8120-6e28-413f-a4a4-1c480d3f2132',
)

res = s.internal.write_discover_catalog_result(req)

if res.discover_catalog_result is not None:
    # handle response
```
