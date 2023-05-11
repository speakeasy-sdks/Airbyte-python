# source_definition

## Overview

SourceDefinition related resources.

### Available Operations

* [create_custom_source_definition](#create_custom_source_definition) - Creates a custom sourceDefinition for the given workspace
* [delete_source_definition](#delete_source_definition) - Delete a source definition
* [get_source_definition](#get_source_definition) - Get source
* [get_source_definition_for_workspace](#get_source_definition_for_workspace) - Get a sourceDefinition that is configured for the given workspace
* [grant_source_definition_to_workspace](#grant_source_definition_to_workspace) - grant a private, non-custom sourceDefinition to a given workspace
* [list_latest_source_definitions](#list_latest_source_definitions) - List the latest sourceDefinitions Airbyte supports
* [list_private_source_definitions](#list_private_source_definitions) - List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.
* [list_source_definitions](#list_source_definitions) - List all the sourceDefinitions the current Airbyte deployment is configured to use
* [list_source_definitions_for_workspace](#list_source_definitions_for_workspace) - List all the sourceDefinitions the given workspace is configured to use
* [revoke_source_definition_from_workspace](#revoke_source_definition_from_workspace) - revoke a grant to a private, non-custom sourceDefinition from a given workspace
* [update_source_definition](#update_source_definition) - Update a sourceDefinition

## create_custom_source_definition

Creates a custom sourceDefinition for the given workspace

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.CustomSourceDefinitionCreate(
    source_definition=shared.SourceDefinitionCreate(
        docker_image_tag='possimus',
        docker_repository='ipsam',
        documentation_url='http://cool-cartilage.org',
        icon='illum',
        name='Kirk Heidenreich',
        resource_requirements=shared.ActorDefinitionResourceRequirements(
            default=shared.ResourceRequirements(
                cpu_limit='facilis',
                cpu_request='placeat',
                memory_limit='reiciendis',
                memory_request='dolores',
            ),
            job_specific=[
                shared.JobTypeResourceLimit(
                    job_type=shared.JobTypeEnum.REPLICATE,
                    resource_requirements=shared.ResourceRequirements(
                        cpu_limit='facilis',
                        cpu_request='cupiditate',
                        memory_limit='nemo',
                        memory_request='natus',
                    ),
                ),
                shared.JobTypeResourceLimit(
                    job_type=shared.JobTypeEnum.DISCOVER_SCHEMA,
                    resource_requirements=shared.ResourceRequirements(
                        cpu_limit='provident',
                        cpu_request='amet',
                        memory_limit='dolor',
                        memory_request='nostrum',
                    ),
                ),
            ],
        ),
    ),
    workspace_id='2f745339-94d7-48de-bb6e-9389f5abb7f6',
)

res = s.source_definition.create_custom_source_definition(req)

if res.source_definition_read is not None:
    # handle response
```

## delete_source_definition

Delete a source definition

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceDefinitionIDRequestBody(
    source_definition_id='62550a28-382a-4c48-bafd-2315bba65016',
)

res = s.source_definition.delete_source_definition(req)

if res.status_code == 200:
    # handle response
```

## get_source_definition

Get source

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceDefinitionIDRequestBody(
    source_definition_id='4e06f5bf-6ae5-491b-88bd-ef3612b63c20',
)

res = s.source_definition.get_source_definition(req)

if res.source_definition_read is not None:
    # handle response
```

## get_source_definition_for_workspace

Get a sourceDefinition that is configured for the given workspace

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceDefinitionIDWithWorkspaceID(
    source_definition_id='5fda8407-74a6-48a9-a35d-086b6f66fef0',
    workspace_id='20e9f443-b425-47b9-92c8-dbda6a61efa2',
)

res = s.source_definition.get_source_definition_for_workspace(req)

if res.source_definition_read is not None:
    # handle response
```

## grant_source_definition_to_workspace

grant a private, non-custom sourceDefinition to a given workspace

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceDefinitionIDWithWorkspaceID(
    source_definition_id='198258fd-0a9e-4ba4-bf7d-3ef049640d6a',
    workspace_id='1831c87a-df59-46fd-b1ad-837ae80c1c19',
)

res = s.source_definition.grant_source_definition_to_workspace(req)

if res.private_source_definition_read is not None:
    # handle response
```

## list_latest_source_definitions

Guaranteed to retrieve the latest information on supported sources.

### Example Usage

```python
import airbyte_oss


s = airbyte_oss.AirbyteOss()


res = s.source_definition.list_latest_source_definitions()

if res.source_definition_read_list is not None:
    # handle response
```

## list_private_source_definitions

List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WorkspaceIDRequestBody(
    workspace_id='c95ba998-678f-4a3f-a969-91af388ce036',
)

res = s.source_definition.list_private_source_definitions(req)

if res.private_source_definition_read_list is not None:
    # handle response
```

## list_source_definitions

List all the sourceDefinitions the current Airbyte deployment is configured to use

### Example Usage

```python
import airbyte_oss


s = airbyte_oss.AirbyteOss()


res = s.source_definition.list_source_definitions()

if res.source_definition_read_list is not None:
    # handle response
```

## list_source_definitions_for_workspace

List all the sourceDefinitions the given workspace is configured to use

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WorkspaceIDRequestBody(
    workspace_id='14448c79-77a0-4ef2-b536-028efeef9341',
)

res = s.source_definition.list_source_definitions_for_workspace(req)

if res.source_definition_read_list is not None:
    # handle response
```

## revoke_source_definition_from_workspace

revoke a grant to a private, non-custom sourceDefinition from a given workspace

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceDefinitionIDWithWorkspaceID(
    source_definition_id='52ed7e25-3f4c-4157-9eaa-7170f445accf',
    workspace_id='667aaf9b-bad1-485f-a431-d6bf5c838fbb',
)

res = s.source_definition.revoke_source_definition_from_workspace(req)

if res.status_code == 200:
    # handle response
```

## update_source_definition

Update a sourceDefinition

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceDefinitionUpdate(
    docker_image_tag='totam',
    resource_requirements=shared.ActorDefinitionResourceRequirements(
        default=shared.ResourceRequirements(
            cpu_limit='quod',
            cpu_request='aspernatur',
            memory_limit='eaque',
            memory_request='impedit',
        ),
        job_specific=[
            shared.JobTypeResourceLimit(
                job_type=shared.JobTypeEnum.DISCOVER_SCHEMA,
                resource_requirements=shared.ResourceRequirements(
                    cpu_limit='odio',
                    cpu_request='delectus',
                    memory_limit='minus',
                    memory_request='ut',
                ),
            ),
            shared.JobTypeResourceLimit(
                job_type=shared.JobTypeEnum.CONNECTION_UPDATER,
                resource_requirements=shared.ResourceRequirements(
                    cpu_limit='eius',
                    cpu_request='eos',
                    memory_limit='veniam',
                    memory_request='repudiandae',
                ),
            ),
            shared.JobTypeResourceLimit(
                job_type=shared.JobTypeEnum.RESET_CONNECTION,
                resource_requirements=shared.ResourceRequirements(
                    cpu_limit='occaecati',
                    cpu_request='debitis',
                    memory_limit='laboriosam',
                    memory_request='eos',
                ),
            ),
        ],
    ),
    source_definition_id='34c9f7b7-9dfe-4b77-a5c3-8d4baf91e506',
)

res = s.source_definition.update_source_definition(req)

if res.source_definition_read is not None:
    # handle response
```
