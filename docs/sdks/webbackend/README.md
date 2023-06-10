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
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.ConnectionIDRequestBody(
    connection_id='044f65fe-72dc-4407-bd0c-c3f408efc15c',
)

res = s.web_backend.get_state_type(req)

if res.connection_state_type is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.ConnectionIDRequestBody](../../models/shared/connectionidrequestbody.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetStateTypeResponse](../../models/operations/getstatetyperesponse.md)**


## web_backend_check_updates

Returns a summary of source and destination definitions that could be updated.

### Example Usage

```python
import airbyte


s = airbyte.Airbyte()


res = s.web_backend.web_backend_check_updates()

if res.web_backend_check_updates_read is not None:
    # handle response
```


### Response

**[operations.WebBackendCheckUpdatesResponse](../../models/operations/webbackendcheckupdatesresponse.md)**


## web_backend_create_connection

Create a connection

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WebBackendConnectionCreate(
    destination_id='eb4d6e1e-ae0f-475a-adf2-acab58b991c9',
    geography=shared.Geography.AUTO,
    name='Mable Stroman',
    namespace_definition=shared.NamespaceDefinitionType.DESTINATION,
    namespace_format='${SOURCE_NAMESPACE}',
    non_breaking_changes_preference=shared.NonBreakingChangesPreference.DISABLE,
    operation_ids=[
        '61e7421c-be6d-4950-af0e-a930b69f7ac2',
        'f72f8850-0904-4911-a082-07888ec66183',
    ],
    operations=[
        shared.OperationCreate(
            name='Terence Mertz',
            operator_configuration=shared.OperatorConfiguration(
                dbt=shared.OperatorDbt(
                    dbt_arguments='unde',
                    docker_image='debitis',
                    git_repo_branch='quidem',
                    git_repo_url='magnam',
                ),
                normalization=shared.OperatorNormalization(
                    option=shared.OperatorNormalizationOption.BASIC,
                ),
                operator_type=shared.OperatorType.NORMALIZATION,
                webhook=shared.OperatorWebhook(
                    dbt_cloud=shared.OperatorWebhookDbtCloud(
                        account_id=881095,
                        job_id=800761,
                    ),
                    execution_body='sunt',
                    execution_url='voluptas',
                    webhook_config_id='faf75b0b-532a-44da-b7cb-aaf4452c4842',
                    webhook_type=shared.OperatorWebhookWebhookType.DBT_CLOUD,
                ),
            ),
            workspace_id='c9b2ad32-dafe-481a-88f4-444573fecd47',
        ),
        shared.OperationCreate(
            name='Vivian Donnelly',
            operator_configuration=shared.OperatorConfiguration(
                dbt=shared.OperatorDbt(
                    dbt_arguments='dolor',
                    docker_image='placeat',
                    git_repo_branch='quos',
                    git_repo_url='sed',
                ),
                normalization=shared.OperatorNormalization(
                    option=shared.OperatorNormalizationOption.BASIC,
                ),
                operator_type=shared.OperatorType.NORMALIZATION,
                webhook=shared.OperatorWebhook(
                    dbt_cloud=shared.OperatorWebhookDbtCloud(
                        account_id=617060,
                        job_id=191202,
                    ),
                    execution_body='nihil',
                    execution_url='unde',
                    webhook_config_id='aa69cd5f-bcf7-49da-98a7-822bf95894e6',
                    webhook_type=shared.OperatorWebhookWebhookType.DBT_CLOUD,
                ),
            ),
            workspace_id='861adb55-f9e5-4d75-9c9f-e8f7502bfdc3',
        ),
        shared.OperationCreate(
            name='Veronica Abshire',
            operator_configuration=shared.OperatorConfiguration(
                dbt=shared.OperatorDbt(
                    dbt_arguments='illo',
                    docker_image='a',
                    git_repo_branch='et',
                    git_repo_url='molestiae',
                ),
                normalization=shared.OperatorNormalization(
                    option=shared.OperatorNormalizationOption.BASIC,
                ),
                operator_type=shared.OperatorType.DBT,
                webhook=shared.OperatorWebhook(
                    dbt_cloud=shared.OperatorWebhookDbtCloud(
                        account_id=294314,
                        job_id=261219,
                    ),
                    execution_body='nostrum',
                    execution_url='ex',
                    webhook_config_id='379f3fb2-7e21-4f86-a657-b36fc6b9f587',
                    webhook_type=shared.OperatorWebhookWebhookType.DBT_CLOUD,
                ),
            ),
            workspace_id='ce525c67-641a-4831-ae50-47b4c21ccb42',
        ),
    ],
    prefix='amet',
    resource_requirements=shared.ResourceRequirements(
        cpu_limit='culpa',
        cpu_request='facilis',
        memory_limit='minus',
        memory_request='vero',
    ),
    schedule=shared.ConnectionSchedule(
        time_unit=shared.ConnectionScheduleTimeUnit.WEEKS,
        units=607242,
    ),
    schedule_data=shared.ConnectionScheduleData(
        basic_schedule=shared.ConnectionScheduleDataBasicSchedule(
            time_unit=shared.ConnectionScheduleDataBasicScheduleTimeUnit.MINUTES,
            units=939131,
        ),
        cron=shared.ConnectionScheduleDataCron(
            cron_expression='fuga',
            cron_time_zone='est',
        ),
    ),
    schedule_type=shared.ConnectionScheduleType.CRON,
    source_catalog_id='dd88e71f-6c48-4252-9777-1e7fd074009e',
    source_id='f8d29de1-dd70-497b-9da0-8c57fa6c78a2',
    status=shared.ConnectionStatus.ACTIVE,
    sync_catalog=shared.AirbyteCatalog(
        streams=[
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='accusamus',
                    cursor_field=[
                        'excepturi',
                    ],
                    destination_sync_mode=shared.DestinationSyncMode.APPEND_DEDUP,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'repudiandae',
                            'minus',
                            'officia',
                            'laboriosam',
                        ],
                        [
                            'cupiditate',
                        ],
                        [
                            'aliquam',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'dicta',
                                'magnam',
                                'doloremque',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'suscipit',
                                'eius',
                                'maiores',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'quos',
                                'id',
                                'officiis',
                                'ab',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncMode.FULL_REFRESH,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'itaque',
                    ],
                    json_schema=shared.StreamJSONSchema(),
                    name='Donald Ernser',
                    namespace='a',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'recusandae',
                            'numquam',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncMode.INCREMENTAL,
                        shared.SyncMode.INCREMENTAL,
                        shared.SyncMode.FULL_REFRESH,
                    ],
                ),
            ),
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='quas',
                    cursor_field=[
                        'enim',
                        'corporis',
                    ],
                    destination_sync_mode=shared.DestinationSyncMode.OVERWRITE,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'voluptate',
                            'nesciunt',
                        ],
                        [
                            'animi',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'temporibus',
                                'porro',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'commodi',
                                'autem',
                                'praesentium',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'quisquam',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncMode.INCREMENTAL,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'eaque',
                        'delectus',
                    ],
                    json_schema=shared.StreamJSONSchema(),
                    name='Kim Wiegand',
                    namespace='a',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'earum',
                            'occaecati',
                        ],
                        [
                            'quidem',
                        ],
                        [
                            'laborum',
                            'molestias',
                            'a',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncMode.FULL_REFRESH,
                        shared.SyncMode.INCREMENTAL,
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

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.WebBackendConnectionCreate](../../models/shared/webbackendconnectioncreate.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.WebBackendCreateConnectionResponse](../../models/operations/webbackendcreateconnectionresponse.md)**


## web_backend_get_connection

Get a connection

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WebBackendConnectionRequestBody(
    connection_id='46e2c330-9db0-4536-99e7-5ca006f5392c',
    with_refreshed_catalog=False,
)

res = s.web_backend.web_backend_get_connection(req)

if res.web_backend_connection_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [shared.WebBackendConnectionRequestBody](../../models/shared/webbackendconnectionrequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.WebBackendGetConnectionResponse](../../models/operations/webbackendgetconnectionresponse.md)**


## web_backend_get_workspace_state

Returns the current state of a workspace

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WebBackendWorkspaceState(
    workspace_id='11a25a8b-f92f-4974-a8ad-9a9f8bf82211',
)

res = s.web_backend.web_backend_get_workspace_state(req)

if res.web_backend_workspace_state_result is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.WebBackendWorkspaceState](../../models/shared/webbackendworkspacestate.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.WebBackendGetWorkspaceStateResponse](../../models/operations/webbackendgetworkspacestateresponse.md)**


## web_backend_list_connections_for_workspace

Returns all non-deleted connections for a workspace.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WebBackendConnectionListRequestBody(
    destination_id=[
        '5359d983-87f7-4a79-8d72-cd2484da2172',
    ],
    source_id=[
        'f2ac41ef-5725-4f11-a9ac-1e41d8a23c23',
        'e34f2dfa-4a19-47f6-9e92-2151fe171209',
        '9853e9f5-43d8-4544-b9ee-224460443bc1',
    ],
    workspace_id='54188c2f-56e8-45da-b832-eabd617c3b0d',
)

res = s.web_backend.web_backend_list_connections_for_workspace(req)

if res.web_backend_connection_read_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [shared.WebBackendConnectionListRequestBody](../../models/shared/webbackendconnectionlistrequestbody.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.WebBackendListConnectionsForWorkspaceResponse](../../models/operations/webbackendlistconnectionsforworkspaceresponse.md)**


## web_backend_list_geographies

Returns all available geographies in which a data sync can run.

### Example Usage

```python
import airbyte


s = airbyte.Airbyte()


res = s.web_backend.web_backend_list_geographies()

if res.web_backend_geographies_list_result is not None:
    # handle response
```


### Response

**[operations.WebBackendListGeographiesResponse](../../models/operations/webbackendlistgeographiesresponse.md)**


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
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WebBackendConnectionUpdate(
    connection_id='51a44bf0-1bad-4870-ad46-082bfbdc41ff',
    geography=shared.Geography.US,
    name='Clifford Torp',
    namespace_definition=shared.NamespaceDefinitionType.CUSTOMFORMAT,
    namespace_format='${SOURCE_NAMESPACE}',
    non_breaking_changes_preference=shared.NonBreakingChangesPreference.IGNORE,
    notify_schema_changes=False,
    operations=[
        shared.WebBackendOperationCreateOrUpdate(
            name='Warren Rutherford',
            operation_id='5d17638f-1edb-4783-99ec-c5cb860f8cd5',
            operator_configuration=shared.OperatorConfiguration(
                dbt=shared.OperatorDbt(
                    dbt_arguments='praesentium',
                    docker_image='perferendis',
                    git_repo_branch='soluta',
                    git_repo_url='animi',
                ),
                normalization=shared.OperatorNormalization(
                    option=shared.OperatorNormalizationOption.BASIC,
                ),
                operator_type=shared.OperatorType.DBT,
                webhook=shared.OperatorWebhook(
                    dbt_cloud=shared.OperatorWebhookDbtCloud(
                        account_id=197872,
                        job_id=559715,
                    ),
                    execution_body='sunt',
                    execution_url='aperiam',
                    webhook_config_id='e4fe4447-297c-4d3b-9dd3-bbce247b7684',
                    webhook_type=shared.OperatorWebhookWebhookType.DBT_CLOUD,
                ),
            ),
            workspace_id='eff50126-d71c-4ffb-90eb-74b8421953b4',
        ),
        shared.WebBackendOperationCreateOrUpdate(
            name='Melody Stoltenberg',
            operation_id='43159d33-e595-43c0-8113-9863aa41e6c3',
            operator_configuration=shared.OperatorConfiguration(
                dbt=shared.OperatorDbt(
                    dbt_arguments='ab',
                    docker_image='maxime',
                    git_repo_branch='porro',
                    git_repo_url='explicabo',
                ),
                normalization=shared.OperatorNormalization(
                    option=shared.OperatorNormalizationOption.BASIC,
                ),
                operator_type=shared.OperatorType.WEBHOOK,
                webhook=shared.OperatorWebhook(
                    dbt_cloud=shared.OperatorWebhookDbtCloud(
                        account_id=120600,
                        job_id=942436,
                    ),
                    execution_body='porro',
                    execution_url='tempore',
                    webhook_config_id='51c9a41f-fbe9-4cbd-b95e-e65e076cc7ab',
                    webhook_type=shared.OperatorWebhookWebhookType.DBT_CLOUD,
                ),
            ),
            workspace_id='f616ea5c-7164-4193-8b90-f2e09d19d2fc',
        ),
        shared.WebBackendOperationCreateOrUpdate(
            name='Faith Mosciski',
            operation_id='e105944b-935d-4237-a72f-90849d6aed4a',
            operator_configuration=shared.OperatorConfiguration(
                dbt=shared.OperatorDbt(
                    dbt_arguments='eveniet',
                    docker_image='optio',
                    git_repo_branch='soluta',
                    git_repo_url='dignissimos',
                ),
                normalization=shared.OperatorNormalization(
                    option=shared.OperatorNormalizationOption.BASIC,
                ),
                operator_type=shared.OperatorType.DBT,
                webhook=shared.OperatorWebhook(
                    dbt_cloud=shared.OperatorWebhookDbtCloud(
                        account_id=204877,
                        job_id=458597,
                    ),
                    execution_body='placeat',
                    execution_url='at',
                    webhook_config_id='9222c9ff-5749-41aa-bfa2-e761f0ca4d45',
                    webhook_type=shared.OperatorWebhookWebhookType.DBT_CLOUD,
                ),
            ),
            workspace_id='6ef1031e-6899-4f0c-a001-e22cd55cc058',
        ),
        shared.WebBackendOperationCreateOrUpdate(
            name='Hattie Botsford',
            operation_id='d76d971f-c820-4c65-b037-bb8e0cc88518',
            operator_configuration=shared.OperatorConfiguration(
                dbt=shared.OperatorDbt(
                    dbt_arguments='molestiae',
                    docker_image='officiis',
                    git_repo_branch='labore',
                    git_repo_url='nulla',
                ),
                normalization=shared.OperatorNormalization(
                    option=shared.OperatorNormalizationOption.BASIC,
                ),
                operator_type=shared.OperatorType.WEBHOOK,
                webhook=shared.OperatorWebhook(
                    dbt_cloud=shared.OperatorWebhookDbtCloud(
                        account_id=9687,
                        job_id=284927,
                    ),
                    execution_body='laborum',
                    execution_url='hic',
                    webhook_config_id='28c5dddb-46aa-41cf-96d8-28da01319112',
                    webhook_type=shared.OperatorWebhookWebhookType.DBT_CLOUD,
                ),
            ),
            workspace_id='9646645c-1d81-4f29-842f-569b7aff0ea2',
        ),
    ],
    prefix='eos',
    resource_requirements=shared.ResourceRequirements(
        cpu_limit='veritatis',
        cpu_request='vel',
        memory_limit='placeat',
        memory_request='libero',
    ),
    schedule=shared.ConnectionSchedule(
        time_unit=shared.ConnectionScheduleTimeUnit.MONTHS,
        units=57719,
    ),
    schedule_data=shared.ConnectionScheduleData(
        basic_schedule=shared.ConnectionScheduleDataBasicSchedule(
            time_unit=shared.ConnectionScheduleDataBasicScheduleTimeUnit.DAYS,
            units=82503,
        ),
        cron=shared.ConnectionScheduleDataCron(
            cron_expression='harum',
            cron_time_zone='cumque',
        ),
    ),
    schedule_type=shared.ConnectionScheduleType.MANUAL,
    skip_reset=False,
    source_catalog_id='63e279a3-b084-4da9-9257-d04f40847a74',
    status=shared.ConnectionStatus.ACTIVE,
    sync_catalog=shared.AirbyteCatalog(
        streams=[
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='blanditiis',
                    cursor_field=[
                        'eius',
                        'cupiditate',
                    ],
                    destination_sync_mode=shared.DestinationSyncMode.OVERWRITE,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'facere',
                            'earum',
                            'debitis',
                        ],
                        [
                            'reiciendis',
                            'ex',
                            'tempore',
                            'provident',
                        ],
                        [
                            'soluta',
                            'maxime',
                            'commodi',
                        ],
                        [
                            'corporis',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'eveniet',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'asperiores',
                                'temporibus',
                                'delectus',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncMode.FULL_REFRESH,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'porro',
                        'dolores',
                    ],
                    json_schema=shared.StreamJSONSchema(),
                    name='Ms. Mario Sawayn DDS',
                    namespace='accusantium',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'et',
                            'fugit',
                            'quos',
                        ],
                        [
                            'voluptate',
                            'autem',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncMode.INCREMENTAL,
                        shared.SyncMode.INCREMENTAL,
                    ],
                ),
            ),
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='earum',
                    cursor_field=[
                        'assumenda',
                        'doloremque',
                    ],
                    destination_sync_mode=shared.DestinationSyncMode.APPEND_DEDUP,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'vel',
                            'itaque',
                            'nulla',
                            'excepturi',
                        ],
                        [
                            'in',
                            'nesciunt',
                            'temporibus',
                            'temporibus',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'ut',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'dignissimos',
                                'illo',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncMode.FULL_REFRESH,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'occaecati',
                    ],
                    json_schema=shared.StreamJSONSchema(),
                    name='Nelson Walker',
                    namespace='doloremque',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'minus',
                        ],
                        [
                            'id',
                            'architecto',
                        ],
                        [
                            'perspiciatis',
                            'quod',
                            'magni',
                            'incidunt',
                        ],
                        [
                            'quisquam',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncMode.INCREMENTAL,
                        shared.SyncMode.FULL_REFRESH,
                    ],
                ),
            ),
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='aliquid',
                    cursor_field=[
                        'illo',
                        'reiciendis',
                        'ipsum',
                    ],
                    destination_sync_mode=shared.DestinationSyncMode.APPEND,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'non',
                            'facere',
                        ],
                        [
                            'exercitationem',
                            'quidem',
                            'ea',
                            'molestiae',
                        ],
                        [
                            'excepturi',
                        ],
                        [
                            'iste',
                            'eaque',
                            'reiciendis',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'est',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'nobis',
                                'expedita',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncMode.FULL_REFRESH,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'atque',
                    ],
                    json_schema=shared.StreamJSONSchema(),
                    name='Jordan Hegmann',
                    namespace='laboriosam',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'perspiciatis',
                            'dicta',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncMode.FULL_REFRESH,
                        shared.SyncMode.FULL_REFRESH,
                        shared.SyncMode.FULL_REFRESH,
                        shared.SyncMode.INCREMENTAL,
                    ],
                ),
            ),
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='sequi',
                    cursor_field=[
                        'consequuntur',
                        'quae',
                        'veniam',
                        'sint',
                    ],
                    destination_sync_mode=shared.DestinationSyncMode.APPEND_DEDUP,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'nesciunt',
                            'maiores',
                            'veniam',
                            'autem',
                        ],
                        [
                            'officiis',
                            'aperiam',
                        ],
                        [
                            'sed',
                            'corporis',
                            'consequuntur',
                            'odio',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'nobis',
                                'beatae',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'ex',
                                'consequuntur',
                                'delectus',
                                'nobis',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncMode.INCREMENTAL,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'optio',
                        'debitis',
                        'architecto',
                    ],
                    json_schema=shared.StreamJSONSchema(),
                    name='David Casper III',
                    namespace='quod',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'aspernatur',
                        ],
                        [
                            'sint',
                        ],
                        [
                            'deleniti',
                            'earum',
                            'consequuntur',
                            'enim',
                        ],
                        [
                            'quibusdam',
                            'accusantium',
                            'nulla',
                            'inventore',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncMode.INCREMENTAL,
                        shared.SyncMode.INCREMENTAL,
                        shared.SyncMode.FULL_REFRESH,
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

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [shared.WebBackendConnectionUpdate](../../models/shared/webbackendconnectionupdate.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.WebBackendUpdateConnectionResponse](../../models/operations/webbackendupdateconnectionresponse.md)**

