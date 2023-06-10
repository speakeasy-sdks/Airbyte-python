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
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.ConnectionStateCreateOrUpdate(
    connection_id='0019c6dc-5e34-4762-b99b-fbbe6949fb2b',
    connection_state=shared.ConnectionState(
        connection_id='b4ecae6c-3d5d-4b3a-9ebd-5daea4c506a8',
        global_state=shared.GlobalState(
            shared_state=shared.StateBlob(),
            stream_states=[
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Sergio Grant Sr.',
                        namespace='aliquid',
                    ),
                    stream_state=shared.StateBlob(),
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Gail Roob',
                        namespace='officiis',
                    ),
                    stream_state=shared.StateBlob(),
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Drew Mraz',
                        namespace='nostrum',
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
                    name='Miss Carroll Rutherford',
                    namespace='laboriosam',
                ),
                stream_state=shared.StateBlob(),
            ),
            shared.StreamState(
                stream_descriptor=shared.StreamDescriptor(
                    name='Sandra Schumm',
                    namespace='consequatur',
                ),
                stream_state=shared.StateBlob(),
            ),
            shared.StreamState(
                stream_descriptor=shared.StreamDescriptor(
                    name='Julie Murazik',
                    namespace='quae',
                ),
                stream_state=shared.StateBlob(),
            ),
        ],
    ),
)

res = s.internal.create_or_update_state(req)

if res.connection_state is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.ConnectionStateCreateOrUpdate](../../models/shared/connectionstatecreateorupdate.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateOrUpdateStateResponse](../../models/operations/createorupdatestateresponse.md)**


## get_attempt_normalization_statuses_for_job

Get normalization status to determine if we can bypass normalization phase

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.JobIDRequestBody(
    id=169819,
)

res = s.internal.get_attempt_normalization_statuses_for_job(req)

if res.attempt_normalization_status_read_list is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.JobIDRequestBody](../../models/shared/jobidrequestbody.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.GetAttemptNormalizationStatusesForJobResponse](../../models/operations/getattemptnormalizationstatusesforjobresponse.md)**


## save_stats

For worker to set sync stats of a running attempt.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SaveStatsRequestBody(
    attempt_number=885797,
    job_id=148379,
    stats=shared.AttemptStats(
        bytes_emitted=898111,
        estimated_bytes=773259,
        estimated_records=55981,
        records_committed=567693,
        records_emitted=950956,
        state_messages_emitted=983000,
    ),
    stream_stats=[
        shared.AttemptStreamStats(
            stats=shared.AttemptStats(
                bytes_emitted=982248,
                estimated_bytes=691,
                estimated_records=992667,
                records_committed=523365,
                records_emitted=118615,
                state_messages_emitted=380595,
            ),
            stream_name='earum',
            stream_namespace='doloribus',
        ),
        shared.AttemptStreamStats(
            stats=shared.AttemptStats(
                bytes_emitted=244569,
                estimated_bytes=260588,
                estimated_records=458212,
                records_committed=446547,
                records_emitted=757407,
                state_messages_emitted=94697,
            ),
            stream_name='neque',
            stream_namespace='vero',
        ),
        shared.AttemptStreamStats(
            stats=shared.AttemptStats(
                bytes_emitted=566312,
                estimated_bytes=37534,
                estimated_records=185816,
                records_committed=771241,
                records_emitted=104736,
                state_messages_emitted=278329,
            ),
            stream_name='dicta',
            stream_namespace='odit',
        ),
    ],
)

res = s.internal.save_stats(req)

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
    attempt_number=357639,
    job_id=701441,
    sync_config=shared.AttemptSyncConfig(
        destination_configuration='alias',
        source_configuration='error',
        state=shared.ConnectionState(
            connection_id='60a66815-1a47-42af-923c-5949f83f350c',
            global_state=shared.GlobalState(
                shared_state=shared.StateBlob(),
                stream_states=[
                    shared.StreamState(
                        stream_descriptor=shared.StreamDescriptor(
                            name='Clinton Hyatt',
                            namespace='nobis',
                        ),
                        stream_state=shared.StateBlob(),
                    ),
                    shared.StreamState(
                        stream_descriptor=shared.StreamDescriptor(
                            name='Steven Carter',
                            namespace='eveniet',
                        ),
                        stream_state=shared.StateBlob(),
                    ),
                    shared.StreamState(
                        stream_descriptor=shared.StreamDescriptor(
                            name='Geoffrey Powlowski',
                            namespace='fugit',
                        ),
                        stream_state=shared.StateBlob(),
                    ),
                    shared.StreamState(
                        stream_descriptor=shared.StreamDescriptor(
                            name='Lillian Rosenbaum',
                            namespace='blanditiis',
                        ),
                        stream_state=shared.StateBlob(),
                    ),
                ],
            ),
            state=shared.StateBlob(),
            state_type=shared.ConnectionStateType.LEGACY,
            stream_state=[
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Lynn Wuckert',
                        namespace='deserunt',
                    ),
                    stream_state=shared.StateBlob(),
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Sheila Torphy',
                        namespace='saepe',
                    ),
                    stream_state=shared.StateBlob(),
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Delia Barton',
                        namespace='quasi',
                    ),
                    stream_state=shared.StateBlob(),
                ),
                shared.StreamState(
                    stream_descriptor=shared.StreamDescriptor(
                        name='Frederick Schaden',
                        namespace='natus',
                    ),
                    stream_state=shared.StateBlob(),
                ),
            ],
        ),
    ),
)

res = s.internal.save_sync_config(req)

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
    attempt_number=793568,
    job_id=154389,
    processing_task_queue='magnam',
    workflow_id='reprehenderit',
)

res = s.internal.set_workflow_in_attempt(req)

if res.internal_operation_result is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [shared.SetWorkflowInAttemptRequestBody](../../models/shared/setworkflowinattemptrequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.SetWorkflowInAttemptResponse](../../models/operations/setworkflowinattemptresponse.md)**


## write_discover_catalog_result

Should only called from worker, to write result from discover activity back to DB.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceDiscoverSchemaWriteRequestBody(
    catalog=shared.AirbyteCatalog(
        streams=[
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='quos',
                    cursor_field=[
                        'amet',
                        'molestiae',
                        'amet',
                    ],
                    destination_sync_mode=shared.DestinationSyncMode.APPEND_DEDUP,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'necessitatibus',
                        ],
                        [
                            'molestias',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'maiores',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'odit',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncMode.INCREMENTAL,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'ipsam',
                        'eaque',
                    ],
                    json_schema=shared.StreamJSONSchema(),
                    name='Lynn Kovacek',
                    namespace='tenetur',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'nemo',
                            'suscipit',
                            'pariatur',
                            'sit',
                        ],
                        [
                            'repellendus',
                            'perferendis',
                            'id',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncMode.FULL_REFRESH,
                        shared.SyncMode.INCREMENTAL,
                        shared.SyncMode.INCREMENTAL,
                        shared.SyncMode.INCREMENTAL,
                    ],
                ),
            ),
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='architecto',
                    cursor_field=[
                        'pariatur',
                    ],
                    destination_sync_mode=shared.DestinationSyncMode.APPEND_DEDUP,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'iure',
                            'explicabo',
                            'minus',
                            'soluta',
                        ],
                        [
                            'velit',
                            'earum',
                            'praesentium',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'quasi',
                                'mollitia',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'harum',
                                'cumque',
                                'doloremque',
                                'expedita',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'eaque',
                                'deserunt',
                                'aliquid',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncMode.INCREMENTAL,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'tempora',
                    ],
                    json_schema=shared.StreamJSONSchema(),
                    name='Rodney Prohaska',
                    namespace='optio',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'quo',
                            'quos',
                            'asperiores',
                            'voluptatum',
                        ],
                        [
                            'corporis',
                            'accusantium',
                            'illo',
                        ],
                        [
                            'doloribus',
                        ],
                        [
                            'at',
                            'possimus',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncMode.INCREMENTAL,
                    ],
                ),
            ),
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='vel',
                    cursor_field=[
                        'mollitia',
                        'quae',
                        'quos',
                        'aperiam',
                    ],
                    destination_sync_mode=shared.DestinationSyncMode.APPEND,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'aliquam',
                            'quisquam',
                        ],
                        [
                            'consequuntur',
                            'maiores',
                            'inventore',
                        ],
                        [
                            'laudantium',
                            'est',
                        ],
                        [
                            'aliquid',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'rem',
                                'voluptatum',
                                'ducimus',
                                'adipisci',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncMode.INCREMENTAL,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'blanditiis',
                        'numquam',
                    ],
                    json_schema=shared.StreamJSONSchema(),
                    name='Margie Balistreri DVM',
                    namespace='autem',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'porro',
                            'deserunt',
                            'magni',
                        ],
                        [
                            'voluptas',
                            'animi',
                        ],
                        [
                            'alias',
                            'fuga',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncMode.FULL_REFRESH,
                    ],
                ),
            ),
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='maxime',
                    cursor_field=[
                        'iste',
                        'ullam',
                    ],
                    destination_sync_mode=shared.DestinationSyncMode.APPEND_DEDUP,
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
                    sync_mode=shared.SyncMode.INCREMENTAL,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'labore',
                        'expedita',
                        'corrupti',
                        'rem',
                    ],
                    json_schema=shared.StreamJSONSchema(),
                    name='Frankie Ritchie',
                    namespace='quo',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'minus',
                            'porro',
                            'id',
                            'excepturi',
                        ],
                        [
                            'libero',
                            'quo',
                            'esse',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncMode.INCREMENTAL,
                        shared.SyncMode.FULL_REFRESH,
                        shared.SyncMode.INCREMENTAL,
                        shared.SyncMode.FULL_REFRESH,
                    ],
                ),
            ),
        ],
    ),
    configuration_hash='pariatur',
    connector_version='eligendi',
    source_id='e10873e4-2b00-46d6-b887-8ba8581a5820',
)

res = s.internal.write_discover_catalog_result(req)

if res.discover_catalog_result is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [shared.SourceDiscoverSchemaWriteRequestBody](../../models/shared/sourcediscoverschemawriterequestbody.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.WriteDiscoverCatalogResultResponse](../../models/operations/writediscovercatalogresultresponse.md)**

