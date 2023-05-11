# web_backend

## Overview

Endpoints for the Airbyte web application. Those APIs should not be called outside the web application implementation and are not
guaranteeing any backwards compatibility.


### Available Operations

* [get_state_type](#get_state_type) - Fetch the current state type for a connection.
* [web_backend_check_updates](#web_backend_check_updates) - Returns a summary of source and destination definitions that could be updated.
* [web_backend_create_connection](#web_backend_create_connection) - Create a connection
* [web_backend_get_connection](#web_backend_get_connection) - Get a connection
* [web_backend_get_workspace_state](#web_backend_get_workspace_state) - Returns the current state of a workspace
* [web_backend_list_connections_for_workspace](#web_backend_list_connections_for_workspace) - Returns all non-deleted connections for a workspace.
* [web_backend_list_geographies](#web_backend_list_geographies) - Returns available geographies can be selected to run data syncs in a particular geography.
The 'auto' entry indicates that the sync will be automatically assigned to a geography according
to the platform default behavior. Entries other than 'auto' are two-letter country codes that
follow the ISO 3166-1 alpha-2 standard.

* [web_backend_update_connection](#web_backend_update_connection) - Update a connection

## get_state_type

Fetch the current state type for a connection.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.ConnectionIDRequestBody(
    connection_id='4444573f-ecd4-4735-bf63-c8209379aa69',
)

res = s.web_backend.get_state_type(req)

if res.connection_state_type is not None:
    # handle response
```

## web_backend_check_updates

Returns a summary of source and destination definitions that could be updated.

### Example Usage

```python
import airbyte_oss


s = airbyte_oss.AirbyteOss()


res = s.web_backend.web_backend_check_updates()

if res.web_backend_check_updates_read is not None:
    # handle response
```

## web_backend_create_connection

Create a connection

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WebBackendConnectionCreate(
    destination_id='cd5fbcf7-9da1-48a7-822b-f95894e6861a',
    geography=shared.GeographyEnum.EU,
    name='Pedro Haley',
    namespace_definition=shared.NamespaceDefinitionTypeEnum.CUSTOMFORMAT,
    namespace_format='${SOURCE_NAMESPACE}',
    non_breaking_changes_preference=shared.NonBreakingChangesPreferenceEnum.IGNORE,
    operation_ids=[
        '751c9fe8-f750-42bf-9c34-50841f176445',
        '6379f3fb-27e2-41f8-a265-7b36fc6b9f58',
        '7ce525c6-7641-4a83-92e5-047b4c21ccb4',
        '23abcdc9-1faa-4bdd-88e7-1f6c48252d77',
    ],
    operations=[
        shared.OperationCreate(
            name='Olive Klocko',
            operator_configuration=shared.OperatorConfiguration(
                dbt=shared.OperatorDbt(
                    dbt_arguments='perferendis',
                    docker_image='in',
                    git_repo_branch='eius',
                    git_repo_url='aut',
                ),
                normalization=shared.OperatorNormalization(
                    option=shared.OperatorNormalizationOptionEnum.BASIC,
                ),
                operator_type=shared.OperatorTypeEnum.NORMALIZATION,
                webhook=shared.OperatorWebhook(
                    dbt_cloud=shared.OperatorWebhookDbtCloud(
                        account_id=611485,
                        job_id=881413,
                    ),
                    execution_body='repellat',
                    execution_url='voluptatum',
                    webhook_config_id='d29de1dd-7097-4b5d-a08c-57fa6c78a216',
                    webhook_type=shared.OperatorWebhookWebhookTypeEnum.DBT_CLOUD,
                ),
            ),
            workspace_id='e19bafec-a619-4149-8140-b64ff8ae170e',
        ),
        shared.OperationCreate(
            name='Donald Ernser',
            operator_configuration=shared.OperatorConfiguration(
                dbt=shared.OperatorDbt(
                    dbt_arguments='a',
                    docker_image='neque',
                    git_repo_branch='nihil',
                    git_repo_url='recusandae',
                ),
                normalization=shared.OperatorNormalization(
                    option=shared.OperatorNormalizationOptionEnum.BASIC,
                ),
                operator_type=shared.OperatorTypeEnum.NORMALIZATION,
                webhook=shared.OperatorWebhook(
                    dbt_cloud=shared.OperatorWebhookDbtCloud(
                        account_id=652013,
                        job_id=651504,
                    ),
                    execution_body='blanditiis',
                    execution_url='suscipit',
                    webhook_config_id='85559667-32aa-45dc-b668-2cb70f8cfd5f',
                    webhook_type=shared.OperatorWebhookWebhookTypeEnum.DBT_CLOUD,
                ),
            ),
            workspace_id='b6e91b9a-9f74-4846-a2c3-309db0536d9e',
        ),
    ],
    prefix='nihil',
    resource_requirements=shared.ResourceRequirements(
        cpu_limit='ad',
        cpu_request='eligendi',
        memory_limit='fuga',
        memory_request='consequatur',
    ),
    schedule=shared.ConnectionSchedule(
        time_unit=shared.ConnectionScheduleTimeUnitEnum.MINUTES,
        units=434632,
    ),
    schedule_data=shared.ConnectionScheduleData(
        basic_schedule=shared.ConnectionScheduleDataBasicSchedule(
            time_unit=shared.ConnectionScheduleDataBasicScheduleTimeUnitEnum.MONTHS,
            units=337581,
        ),
        cron=shared.ConnectionScheduleDataCron(
            cron_expression='dolorem',
            cron_time_zone='omnis',
        ),
    ),
    schedule_type=shared.ConnectionScheduleTypeEnum.MANUAL,
    source_catalog_id='c11a25a8-bf92-4f97-828a-d9a9f8bf8221',
    source_id='125359d9-8387-4f7a-b9cd-72cd2484da21',
    status=shared.ConnectionStatusEnum.INACTIVE,
    sync_catalog=shared.AirbyteCatalog(
        streams=[
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='omnis',
                    cursor_field=[
                        'qui',
                        'similique',
                        'eligendi',
                        'numquam',
                    ],
                    destination_sync_mode=shared.DestinationSyncModeEnum.APPEND,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'exercitationem',
                            'nihil',
                            'quia',
                            'quis',
                        ],
                        [
                            'dicta',
                            'dicta',
                            'eum',
                            'sint',
                        ],
                        [
                            'nobis',
                            'quasi',
                            'itaque',
                        ],
                        [
                            'vitae',
                            'temporibus',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'aspernatur',
                                'neque',
                                'impedit',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'neque',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'amet',
                                'labore',
                                'repellat',
                                'eos',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncModeEnum.INCREMENTAL,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'mollitia',
                        'quaerat',
                        'officia',
                        'sunt',
                    ],
                    json_schema={
                        "quam": 'a',
                        "iure": 'nulla',
                        "recusandae": 'iste',
                    },
                    name='Judy Bosco DVM',
                    namespace='saepe',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'architecto',
                            'sed',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncModeEnum.INCREMENTAL,
                    ],
                ),
            ),
        ],
    ),
)

res = s.web_backend.web_backend_create_connection(req)

if res.web_backend_connection_read is not None:
    # handle response
```

## web_backend_get_connection

Get a connection

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WebBackendConnectionRequestBody(
    connection_id='9853e9f5-43d8-4544-b9ee-224460443bc1',
    with_refreshed_catalog=False,
)

res = s.web_backend.web_backend_get_connection(req)

if res.web_backend_connection_read is not None:
    # handle response
```

## web_backend_get_workspace_state

Returns the current state of a workspace

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WebBackendWorkspaceState(
    workspace_id='54188c2f-56e8-45da-b832-eabd617c3b0d',
)

res = s.web_backend.web_backend_get_workspace_state(req)

if res.web_backend_workspace_state_result is not None:
    # handle response
```

## web_backend_list_connections_for_workspace

Returns all non-deleted connections for a workspace.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WebBackendConnectionListRequestBody(
    destination_id=[
        '1a44bf01-bad8-4706-9460-82bfbdc41ff5',
        'd4e2ae4f-b5cb-435d-9763-8f1edb78359e',
    ],
    source_id=[
        'c5cb860f-8cd5-480b-a738-10e4fe444729',
        '7cd3b1dd-3bbc-4e24-bb76-84eff50126d7',
        '1cffbd0e-b74b-4842-9953-b44bd3c43159',
        'd33e5953-c001-4139-863a-a41e6c31cc2f',
    ],
    workspace_id='1fcb51c9-a41f-4fbe-9cbd-795ee65e076c',
)

res = s.web_backend.web_backend_list_connections_for_workspace(req)

if res.web_backend_connection_read_list is not None:
    # handle response
```

## web_backend_list_geographies

Returns all available geographies in which a data sync can run.

### Example Usage

```python
import airbyte_oss


s = airbyte_oss.AirbyteOss()


res = s.web_backend.web_backend_list_geographies()

if res.web_backend_geographies_list_result is not None:
    # handle response
```

## web_backend_update_connection

Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
Any operations that lack an ID will be created. Then, the newly created operationId will be applied to the
connection along with the rest of the operationIds in the request body.
Apply a patch-style update to a connection. Only fields present on the update request body will be updated.
Note that if a catalog is present in the request body, the connection's entire catalog will be replaced
with the catalog from the request. This means that to modify a single stream, the entire new catalog
containing the updated stream needs to be sent.


### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WebBackendConnectionUpdate(
    connection_id='c7abf616-ea5c-4716-8193-4b90f2e09d19',
    geography=shared.GeographyEnum.EU,
    name='Dr. Lorene Runte',
    namespace_definition=shared.NamespaceDefinitionTypeEnum.CUSTOMFORMAT,
    namespace_format='${SOURCE_NAMESPACE}',
    non_breaking_changes_preference=shared.NonBreakingChangesPreferenceEnum.IGNORE,
    notify_schema_changes=False,
    operations=[
        shared.WebBackendOperationCreateOrUpdate(
            name='Barbara Hilll',
            operation_id='4b935d23-7a72-4f90-849d-6aed4aecb753',
            operator_configuration=shared.OperatorConfiguration(
                dbt=shared.OperatorDbt(
                    dbt_arguments='esse',
                    docker_image='placeat',
                    git_repo_branch='at',
                    git_repo_url='excepturi',
                ),
                normalization=shared.OperatorNormalization(
                    option=shared.OperatorNormalizationOptionEnum.BASIC,
                ),
                operator_type=shared.OperatorTypeEnum.NORMALIZATION,
                webhook=shared.OperatorWebhook(
                    dbt_cloud=shared.OperatorWebhookDbtCloud(
                        account_id=139505,
                        job_id=154268,
                    ),
                    execution_body='maxime',
                    execution_url='excepturi',
                    webhook_config_id='ff57491a-abfa-42e7-a1f0-ca4d456ef103',
                    webhook_type=shared.OperatorWebhookWebhookTypeEnum.DBT_CLOUD,
                ),
            ),
            workspace_id='1e6899f0-c200-41e2-acd5-5cc0584a184d',
        ),
        shared.WebBackendOperationCreateOrUpdate(
            name='Melanie Schumm',
            operation_id='1fc820c6-5b03-47bb-8e0c-c885187e4de0',
            operator_configuration=shared.OperatorConfiguration(
                dbt=shared.OperatorDbt(
                    dbt_arguments='ut',
                    docker_image='laborum',
                    git_repo_branch='hic',
                    git_repo_url='sed',
                ),
                normalization=shared.OperatorNormalization(
                    option=shared.OperatorNormalizationOptionEnum.BASIC,
                ),
                operator_type=shared.OperatorTypeEnum.DBT,
                webhook=shared.OperatorWebhook(
                    dbt_cloud=shared.OperatorWebhookDbtCloud(
                        account_id=803763,
                        job_id=323614,
                    ),
                    execution_body='quibusdam',
                    execution_url='facere',
                    webhook_config_id='db46aa1c-fd6d-4828-9a01-319112964664',
                    webhook_type=shared.OperatorWebhookWebhookTypeEnum.DBT_CLOUD,
                ),
            ),
            workspace_id='5c1d81f2-9042-4f56-9b7a-ff0ea2216cbe',
        ),
        shared.WebBackendOperationCreateOrUpdate(
            name='Stella Boehm',
            operation_id='163e279a-3b08-44da-9925-7d04f40847a7',
            operator_configuration=shared.OperatorConfiguration(
                dbt=shared.OperatorDbt(
                    dbt_arguments='numquam',
                    docker_image='quia',
                    git_repo_branch='repellendus',
                    git_repo_url='blanditiis',
                ),
                normalization=shared.OperatorNormalization(
                    option=shared.OperatorNormalizationOptionEnum.BASIC,
                ),
                operator_type=shared.OperatorTypeEnum.NORMALIZATION,
                webhook=shared.OperatorWebhook(
                    dbt_cloud=shared.OperatorWebhookDbtCloud(
                        account_id=259019,
                        job_id=585730,
                    ),
                    execution_body='nisi',
                    execution_url='placeat',
                    webhook_config_id='bdeecf6b-99bc-4635-a2eb-fdf55c294c06',
                    webhook_type=shared.OperatorWebhookWebhookTypeEnum.DBT_CLOUD,
                ),
            ),
            workspace_id='0b06a128-7764-4eef-ad0c-6d6ed9c73dd6',
        ),
        shared.WebBackendOperationCreateOrUpdate(
            name='Leslie Heaney II',
            operation_id='09a8e870-d3c5-4a1f-9c24-2c7b66a1f30c',
            operator_configuration=shared.OperatorConfiguration(
                dbt=shared.OperatorDbt(
                    dbt_arguments='dignissimos',
                    docker_image='non',
                    git_repo_branch='facere',
                    git_repo_url='repellat',
                ),
                normalization=shared.OperatorNormalization(
                    option=shared.OperatorNormalizationOptionEnum.BASIC,
                ),
                operator_type=shared.OperatorTypeEnum.DBT,
                webhook=shared.OperatorWebhook(
                    dbt_cloud=shared.OperatorWebhookDbtCloud(
                        account_id=693988,
                        job_id=408208,
                    ),
                    execution_body='molestiae',
                    execution_url='vitae',
                    webhook_config_id='9890f42a-4bb4-438d-85b2-60591d745e3c',
                    webhook_type=shared.OperatorWebhookWebhookTypeEnum.DBT_CLOUD,
                ),
            ),
            workspace_id='2059c9c3-f567-4e0e-a527-65b1d62fcdac',
        ),
    ],
    prefix='debitis',
    resource_requirements=shared.ResourceRequirements(
        cpu_limit='architecto',
        cpu_request='reiciendis',
        memory_limit='consequatur',
        memory_request='sunt',
    ),
    schedule=shared.ConnectionSchedule(
        time_unit=shared.ConnectionScheduleTimeUnitEnum.MINUTES,
        units=80673,
    ),
    schedule_data=shared.ConnectionScheduleData(
        basic_schedule=shared.ConnectionScheduleDataBasicSchedule(
            time_unit=shared.ConnectionScheduleDataBasicScheduleTimeUnitEnum.HOURS,
            units=799730,
        ),
        cron=shared.ConnectionScheduleDataCron(
            cron_expression='repudiandae',
            cron_time_zone='consequuntur',
        ),
    ),
    schedule_type=shared.ConnectionScheduleTypeEnum.MANUAL,
    skip_reset=False,
    source_catalog_id='39e8f25c-d0d1-49d9-99f4-39e39266cbd9',
    status=shared.ConnectionStatusEnum.ACTIVE,
    sync_catalog=shared.AirbyteCatalog(
        streams=[
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='molestiae',
                    cursor_field=[
                        'laborum',
                        'odit',
                        'rerum',
                    ],
                    destination_sync_mode=shared.DestinationSyncModeEnum.APPEND,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'et',
                        ],
                        [
                            'nisi',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'temporibus',
                                'et',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'nisi',
                                'aliquid',
                                'excepturi',
                                'quas',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'placeat',
                                'eligendi',
                                'quaerat',
                                'veniam',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncModeEnum.INCREMENTAL,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'dolores',
                        'dicta',
                    ],
                    json_schema={
                        "maxime": 'dolores',
                        "molestias": 'quam',
                    },
                    name='Beth Klocko',
                    namespace='velit',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'ad',
                        ],
                        [
                            'alias',
                            'adipisci',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncModeEnum.INCREMENTAL,
                        shared.SyncModeEnum.INCREMENTAL,
                        shared.SyncModeEnum.INCREMENTAL,
                    ],
                ),
            ),
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='minima',
                    cursor_field=[
                        'molestiae',
                        'et',
                        'accusamus',
                    ],
                    destination_sync_mode=shared.DestinationSyncModeEnum.OVERWRITE,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'perspiciatis',
                        ],
                        [
                            'corporis',
                        ],
                        [
                            'molestiae',
                            'adipisci',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'optio',
                                'itaque',
                                'at',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'id',
                                'cumque',
                                'in',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'quibusdam',
                                'culpa',
                                'dolor',
                                'occaecati',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncModeEnum.FULL_REFRESH,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'labore',
                        'pariatur',
                        'vel',
                    ],
                    json_schema={
                        "soluta": 'minus',
                        "magni": 'mollitia',
                    },
                    name='Ms. Jim Macejkovic',
                    namespace='explicabo',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'occaecati',
                            'enim',
                            'tempora',
                        ],
                        [
                            'iure',
                            'voluptatibus',
                            'id',
                        ],
                        [
                            'explicabo',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncModeEnum.FULL_REFRESH,
                    ],
                ),
            ),
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='nesciunt',
                    cursor_field=[
                        'molestias',
                        'atque',
                    ],
                    destination_sync_mode=shared.DestinationSyncModeEnum.APPEND,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'nemo',
                            'sequi',
                        ],
                        [
                            'libero',
                            'ab',
                            'alias',
                            'accusantium',
                        ],
                        [
                            'autem',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'reiciendis',
                                'incidunt',
                                'provident',
                                'dolores',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'recusandae',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'magni',
                                'sit',
                                'voluptas',
                                'nesciunt',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncModeEnum.INCREMENTAL,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'eius',
                        'perspiciatis',
                    ],
                    json_schema={
                        "ex": 'aliquid',
                    },
                    name='Wilson Ledner',
                    namespace='voluptatem',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'libero',
                        ],
                        [
                            'veritatis',
                            'provident',
                            'veniam',
                            'quos',
                        ],
                        [
                            'facere',
                            'eius',
                            'doloremque',
                        ],
                        [
                            'aut',
                            'sequi',
                            'reiciendis',
                            'neque',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncModeEnum.INCREMENTAL,
                        shared.SyncModeEnum.INCREMENTAL,
                        shared.SyncModeEnum.INCREMENTAL,
                        shared.SyncModeEnum.FULL_REFRESH,
                    ],
                ),
            ),
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='natus',
                    cursor_field=[
                        'facilis',
                        'earum',
                    ],
                    destination_sync_mode=shared.DestinationSyncModeEnum.APPEND,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'consequatur',
                            'harum',
                            'nobis',
                        ],
                        [
                            'consequatur',
                            'temporibus',
                        ],
                        [
                            'quos',
                            'commodi',
                            'blanditiis',
                            'voluptatibus',
                        ],
                        [
                            'nemo',
                            'ratione',
                            'dolore',
                            'perferendis',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'libero',
                                'dolor',
                                'nesciunt',
                                'vitae',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'numquam',
                                'provident',
                                'quia',
                                'reiciendis',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncModeEnum.FULL_REFRESH,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'et',
                        'qui',
                        'iusto',
                        'a',
                    ],
                    json_schema={
                        "aperiam": 'saepe',
                        "voluptatem": 'soluta',
                        "hic": 'beatae',
                    },
                    name='Ms. Casey Corkery',
                    namespace='dignissimos',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'consequatur',
                            'similique',
                            'eligendi',
                            'impedit',
                        ],
                        [
                            'odio',
                            'voluptate',
                            'mollitia',
                        ],
                        [
                            'tempore',
                            'voluptate',
                            'cum',
                            'esse',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncModeEnum.FULL_REFRESH,
                    ],
                ),
            ),
        ],
    ),
)

res = s.web_backend.web_backend_update_connection(req)

if res.web_backend_connection_read is not None:
    # handle response
```
