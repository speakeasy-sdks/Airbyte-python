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
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceIDRequestBody(
    source_id='02d72165-7650-4664-9870-d9d21f9ad030',
)

res = s.source.check_connection_to_source(req)

if res.check_connection_read is not None:
    # handle response
```

## check_connection_to_source_for_update

Check connection for a proposed update to a source

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceUpdate(
    connection_configuration='optio',
    name='Raquel Runolfsdottir Sr.',
    source_id='a0836429-068b-4850-aa55-e7f73bc845e3',
)

res = s.source.check_connection_to_source_for_update(req)

if res.check_connection_read is not None:
    # handle response
```

## clone_source

Clone source

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceCloneRequestBody(
    source_clone_id='20a319f4-badf-4947-89a8-67bc42426665',
    source_configuration=shared.SourceCloneConfiguration(
        connection_configuration='quos',
        name='Laurie Sporer',
    ),
)

res = s.source.clone_source(req)

if res.source_read is not None:
    # handle response
```

## create_source

Create a source

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceCreate(
    connection_configuration='culpa',
    name='Pat Wuckert DVM',
    source_definition_id='cb4c593e-c12c-4daa-90ec-7afedbd80df4',
    workspace_id='48a47f93-90c5-4888-8983-dabf9ef3ffdd',
)

res = s.source.create_source(req)

if res.source_read is not None:
    # handle response
```

## delete_source

Delete a source

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceIDRequestBody(
    source_id='9f7f079a-f4d3-4572-8cdb-0f4d281187d5',
)

res = s.source.delete_source(req)

if res.status_code == 200:
    # handle response
```

## discover_schema_for_source

Discover the schema catalog of the source

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceDiscoverSchemaRequestBody(
    connection_id='6844eded-85a9-4065-a628-bdfc2032b6c8',
    disable_cache=False,
    notify_schema_change=False,
    source_id='79923b7e-1358-44f7-ae12-c6891f82ce11',
)

res = s.source.discover_schema_for_source(req)

if res.source_discover_schema_read is not None:
    # handle response
```

## get_most_recent_source_actor_catalog

Get most recent ActorCatalog for source

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceIDRequestBody(
    source_id='57172305-377d-4cfa-89df-975e35668609',
)

res = s.source.get_most_recent_source_actor_catalog(req)

if res.actor_catalog_with_updated_at is not None:
    # handle response
```

## get_source

Get source

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceIDRequestBody(
    source_id='2e9c3ddc-5f11-41de-a102-6d541a4d190f',
)

res = s.source.get_source(req)

if res.source_read is not None:
    # handle response
```

## list_sources_for_workspace

List sources for workspace. Does not return deleted sources.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WorkspaceIDRequestBody(
    workspace_id='eb21780b-ccc0-4dbb-9db4-84708fb4e391',
)

res = s.source.list_sources_for_workspace(req)

if res.source_read_list is not None:
    # handle response
```

## search_sources

Search sources

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceSearch(
    connection_configuration='officiis',
    name='Mrs. Susie Schowalter',
    source_definition_id='c4c4e545-99ea-4342-a60e-9b200ce78a1b',
    source_id='d8fb7a0a-116c-4e72-bd40-97fa30e9af72',
    source_name='ipsam',
    workspace_id='b2912203-0d83-4f5a-ab77-99d22e8c1f84',
)

res = s.source.search_sources(req)

if res.source_read_list is not None:
    # handle response
```

## update_source

Update a source

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceUpdate(
    connection_configuration='perspiciatis',
    name='Naomi Cassin',
    source_id='dc42c876-c2c2-4dfb-8cfc-1c76230f841f',
)

res = s.source.update_source(req)

if res.source_read is not None:
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
                    alias_name='architecto',
                    cursor_field=[
                        'assumenda',
                        'eos',
                        'dolorem',
                    ],
                    destination_sync_mode=shared.DestinationSyncModeEnum.APPEND_DEDUP,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'ab',
                            'magnam',
                            'pariatur',
                        ],
                        [
                            'autem',
                            'tempore',
                            'recusandae',
                        ],
                        [
                            'officia',
                            'voluptas',
                        ],
                        [
                            'corporis',
                            'excepturi',
                            'natus',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'aspernatur',
                                'dolores',
                                'laborum',
                                'vero',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'voluptatem',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'id',
                                'quae',
                                'commodi',
                                'a',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncModeEnum.INCREMENTAL,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'nam',
                    ],
                    json_schema={
                        "iusto": 'ab',
                    },
                    name='Louis Kuvalis',
                    namespace='ullam',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'rem',
                            'nemo',
                            'non',
                            'recusandae',
                        ],
                        [
                            'ipsa',
                            'aliquam',
                            'dolor',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncModeEnum.INCREMENTAL,
                        shared.SyncModeEnum.FULL_REFRESH,
                        shared.SyncModeEnum.FULL_REFRESH,
                    ],
                ),
            ),
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='consequuntur',
                    cursor_field=[
                        'commodi',
                        'ipsam',
                    ],
                    destination_sync_mode=shared.DestinationSyncModeEnum.OVERWRITE,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'nisi',
                            'explicabo',
                        ],
                        [
                            'doloremque',
                            'odio',
                        ],
                        [
                            'voluptatum',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'quam',
                                'dolorum',
                                'libero',
                                'ratione',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'optio',
                                'saepe',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncModeEnum.INCREMENTAL,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'sed',
                    ],
                    json_schema={
                        "consequuntur": 'quis',
                    },
                    name='Violet Greenfelder',
                    namespace='exercitationem',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'quasi',
                            'quae',
                        ],
                        [
                            'possimus',
                            'quo',
                            'suscipit',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncModeEnum.INCREMENTAL,
                        shared.SyncModeEnum.INCREMENTAL,
                    ],
                ),
            ),
            shared.AirbyteStreamAndConfiguration(
                config=shared.AirbyteStreamConfiguration(
                    alias_name='doloribus',
                    cursor_field=[
                        'alias',
                        'deserunt',
                        'fugit',
                    ],
                    destination_sync_mode=shared.DestinationSyncModeEnum.OVERWRITE,
                    field_selection_enabled=False,
                    primary_key=[
                        [
                            'maxime',
                            'facere',
                        ],
                        [
                            'cupiditate',
                            'deleniti',
                            'quasi',
                            'maiores',
                        ],
                        [
                            'aliquid',
                        ],
                        [
                            'unde',
                            'corrupti',
                            'quae',
                        ],
                    ],
                    selected=False,
                    selected_fields=[
                        shared.SelectedFieldInfo(
                            field_path=[
                                'libero',
                                'nam',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'adipisci',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'hic',
                                'similique',
                                'fuga',
                                'consectetur',
                            ],
                        ),
                        shared.SelectedFieldInfo(
                            field_path=[
                                'laudantium',
                                'cumque',
                            ],
                        ),
                    ],
                    suggested=False,
                    sync_mode=shared.SyncModeEnum.FULL_REFRESH,
                ),
                stream=shared.AirbyteStream(
                    default_cursor_field=[
                        'nam',
                    ],
                    json_schema={
                        "magnam": 'aperiam',
                        "ducimus": 'itaque',
                        "necessitatibus": 'numquam',
                        "doloribus": 'eligendi',
                    },
                    name='James Russel',
                    namespace='nobis',
                    source_defined_cursor=False,
                    source_defined_primary_key=[
                        [
                            'reiciendis',
                            'vitae',
                            'ullam',
                        ],
                        [
                            'consequuntur',
                            'voluptas',
                        ],
                    ],
                    supported_sync_modes=[
                        shared.SyncModeEnum.INCREMENTAL,
                    ],
                ),
            ),
        ],
    ),
    configuration_hash='corrupti',
    connector_version='est',
    source_id='0dc76632-4ccb-406c-8ca1-2d02529270b8',
)

res = s.source.write_discover_catalog_result(req)

if res.discover_catalog_result is not None:
    # handle response
```
