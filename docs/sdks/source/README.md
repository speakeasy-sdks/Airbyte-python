# source

## Overview

Source related resources.

### Available Operations

* [check_connection_to_source](#check_connection_to_source) - Check connection to the source
* [check_connection_to_source_for_update](#check_connection_to_source_for_update) - Check connection for a proposed update to a source
* [clone_source](#clone_source) - Clone source
* [create_source](#create_source) - Create a source
* [delete_source](#delete_source) - Delete a source
* [discover_schema_for_source](#discover_schema_for_source) - Discover the schema catalog of the source
* [get_most_recent_source_actor_catalog](#get_most_recent_source_actor_catalog) - Get most recent ActorCatalog for source
* [get_source](#get_source) - Get source
* [list_sources_for_workspace](#list_sources_for_workspace) - List sources for workspace
* [search_sources](#search_sources) - Search sources
* [update_source](#update_source) - Update a source
* [write_discover_catalog_result](#write_discover_catalog_result) - Should only called from worker, to write result from discover activity back to DB.

## check_connection_to_source

Check connection to the source

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceIDRequestBody(
    source_id='9167b8e3-c8db-4034-88d6-d364ffd45590',
)

res = s.source.check_connection_to_source(req)

if res.check_connection_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.SourceIDRequestBody](../../models/shared/sourceidrequestbody.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CheckConnectionToSourceResponse](../../models/operations/checkconnectiontosourceresponse.md)**


## check_connection_to_source_for_update

Check connection for a proposed update to a source

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceUpdate(
    connection_configuration='ex',
    name='Keith Crist',
    source_id='d48e935c-2c9e-481f-b0be-3e43202d7216',
)

res = s.source.check_connection_to_source_for_update(req)

if res.check_connection_read is not None:
    # handle response
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [shared.SourceUpdate](../../models/shared/sourceupdate.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.CheckConnectionToSourceForUpdateResponse](../../models/operations/checkconnectiontosourceforupdateresponse.md)**


## clone_source

Clone source

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceCloneRequestBody(
    source_clone_id='57650664-1870-4d9d-a1f9-ad030c4ecc11',
    source_configuration=shared.SourceCloneConfiguration(
        connection_configuration='id',
        name='Brandy Dicki',
    ),
)

res = s.source.clone_source(req)

if res.source_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.SourceCloneRequestBody](../../models/shared/sourceclonerequestbody.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.CloneSourceResponse](../../models/operations/clonesourceresponse.md)**


## create_source

Create a source

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceCreate(
    connection_configuration='eos',
    name='Kenneth Hoppe',
    source_definition_id='8502a55e-7f73-4bc8-85e3-20a319f4badf',
    workspace_id='947c9a86-7bc4-4242-a665-816ddca8ef51',
)

res = s.source.create_source(req)

if res.source_read is not None:
    # handle response
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [shared.SourceCreate](../../models/shared/sourcecreate.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.CreateSourceResponse](../../models/operations/createsourceresponse.md)**


## delete_source

Delete a source

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceIDRequestBody(
    source_id='fcb4c593-ec12-4cda-ad0e-c7afedbd80df',
)

res = s.source.delete_source(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.SourceIDRequestBody](../../models/shared/sourceidrequestbody.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.DeleteSourceResponse](../../models/operations/deletesourceresponse.md)**


## discover_schema_for_source

Discover the schema catalog of the source

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceDiscoverSchemaRequestBody(
    connection_id='448a47f9-390c-4588-8098-3dabf9ef3ffd',
    disable_cache=False,
    notify_schema_change=False,
    source_id='d9f7f079-af4d-4357-a4cd-b0f4d281187d',
)

res = s.source.discover_schema_for_source(req)

if res.source_discover_schema_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [shared.SourceDiscoverSchemaRequestBody](../../models/shared/sourcediscoverschemarequestbody.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.DiscoverSchemaForSourceResponse](../../models/operations/discoverschemaforsourceresponse.md)**


## get_most_recent_source_actor_catalog

Get most recent ActorCatalog for source

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceIDRequestBody(
    source_id='56844ede-d85a-4906-9e62-8bdfc2032b6c',
)

res = s.source.get_most_recent_source_actor_catalog(req)

if res.actor_catalog_with_updated_at is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.SourceIDRequestBody](../../models/shared/sourceidrequestbody.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetMostRecentSourceActorCatalogResponse](../../models/operations/getmostrecentsourceactorcatalogresponse.md)**


## get_source

Get source

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceIDRequestBody(
    source_id='879923b7-e135-484f-bae1-2c6891f82ce1',
)

res = s.source.get_source(req)

if res.source_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.SourceIDRequestBody](../../models/shared/sourceidrequestbody.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetSourceResponse](../../models/operations/getsourceresponse.md)**


## list_sources_for_workspace

List sources for workspace. Does not return deleted sources.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WorkspaceIDRequestBody(
    workspace_id='15717230-5377-4dcf-a89d-f975e3566860',
)

res = s.source.list_sources_for_workspace(req)

if res.source_read_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.WorkspaceIDRequestBody](../../models/shared/workspaceidrequestbody.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListSourcesForWorkspaceResponse](../../models/operations/listsourcesforworkspaceresponse.md)**


## search_sources

Search sources

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceSearch(
    connection_configuration='perspiciatis',
    name='Kellie Miller',
    source_definition_id='ddc5f111-dea1-4026-9541-a4d190feb217',
    source_id='80bccc0d-bbdd-4b48-8708-fb4e391e6bc1',
    source_name='ad',
    workspace_id='8c4c4e54-599e-4a34-a260-e9b200ce78a1',
)

res = s.source.search_sources(req)

if res.source_read_list is not None:
    # handle response
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [shared.SourceSearch](../../models/shared/sourcesearch.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.SearchSourcesResponse](../../models/operations/searchsourcesresponse.md)**


## update_source

Update a source

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceUpdate(
    connection_configuration='expedita',
    name='Isaac Wyman',
    source_id='a0a116ce-723d-4409-bfa3-0e9af725b291',
)

res = s.source.update_source(req)

if res.source_read is not None:
    # handle response
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [shared.SourceUpdate](../../models/shared/sourceupdate.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.UpdateSourceResponse](../../models/operations/updatesourceresponse.md)**


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
                    alias_name='explicabo',
                    cursor_field=[
                        'amet',
                    ],
                    destination_sync_mode=shared.DestinationSyncMode.APPEND,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'velit',
                            'hic',
                            'ullam',
                        ],
                        [
                            'itaque',
                            'distinctio',
                            'iusto',
                        ],
                        [
                            'provident',
                            'occaecati',
                        ],
                        [
                            'sunt',
                            'odit',
                            'vero',
                            'deleniti',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'repellat',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'magnam',
                                'perspiciatis',
                                'amet',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'sunt',
                                'nemo',
                                'delectus',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'porro',
                                'quaerat',
                                'magni',
                                'cumque',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncMode.INCREMENTAL,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'commodi',
                        'maxime',
                    ],
                    json_schema=shared.StreamJSONSchema(),
                    name='Alexandra Crooks',
                    namespace='harum',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'hic',
                            'quo',
                            'illo',
                            'nobis',
                        ],
                        [
                            'nisi',
                            'explicabo',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncMode.FULL_REFRESH,
                    ],
                ),
            ),
        ],
    ),
    configuration_hash='reiciendis',
    connector_version='quos',
    source_id='41fb1bd2-3fdb-414d-b6be-5a685998e22a',
)

res = s.source.write_discover_catalog_result(req)

if res.discover_catalog_result is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [shared.SourceDiscoverSchemaWriteRequestBody](../../models/shared/sourcediscoverschemawriterequestbody.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.WriteDiscoverCatalogResultResponse](../../models/operations/writediscovercatalogresultresponse.md)**

