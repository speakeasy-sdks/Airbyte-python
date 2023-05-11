# destination_definition

## Overview

DestinationDefinition related resources.

### Available Operations

* [create_custom_destination_definition](#create_custom_destination_definition) - Creates a custom destinationDefinition for the given workspace
* [delete_destination_definition](#delete_destination_definition) - Delete a destination definition
* [get_destination_definition](#get_destination_definition) - Get destinationDefinition
* [get_destination_definition_for_workspace](#get_destination_definition_for_workspace) - Get a destinationDefinition that is configured for the given workspace
* [grant_destination_definition_to_workspace](#grant_destination_definition_to_workspace) - grant a private, non-custom destinationDefinition to a given workspace
* [list_destination_definitions](#list_destination_definitions) - List all the destinationDefinitions the current Airbyte deployment is configured to use
* [list_destination_definitions_for_workspace](#list_destination_definitions_for_workspace) - List all the destinationDefinitions the given workspace is configured to use
* [list_latest_destination_definitions](#list_latest_destination_definitions) - List the latest destinationDefinitions Airbyte supports
* [list_private_destination_definitions](#list_private_destination_definitions) - List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.
* [revoke_destination_definition_from_workspace](#revoke_destination_definition_from_workspace) - revoke a grant to a private, non-custom destinationDefinition from a given workspace
* [update_destination_definition](#update_destination_definition) - Update destinationDefinition

## create_custom_destination_definition

Creates a custom destinationDefinition for the given workspace

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.CustomDestinationDefinitionCreate(
    destination_definition=shared.DestinationDefinitionCreate(
        docker_image_tag='repudiandae',
        docker_repository='accusantium',
        documentation_url='https://uneven-codpiece.org',
        icon='odio',
        name='Fred Champlin',
        resource_requirements=shared.ActorDefinitionResourceRequirements(
            default=shared.ResourceRequirements(
                cpu_limit='earum',
                cpu_request='adipisci',
                memory_limit='recusandae',
                memory_request='similique',
            ),
            job_specific=[
                shared.JobTypeResourceLimit(
                    job_type=shared.JobTypeEnum.RESET_CONNECTION,
                    resource_requirements=shared.ResourceRequirements(
                        cpu_limit='quis',
                        cpu_request='beatae',
                        memory_limit='unde',
                        memory_request='molestiae',
                    ),
                ),
                shared.JobTypeResourceLimit(
                    job_type=shared.JobTypeEnum.REPLICATE,
                    resource_requirements=shared.ResourceRequirements(
                        cpu_limit='cupiditate',
                        cpu_request='fugit',
                        memory_limit='numquam',
                        memory_request='numquam',
                    ),
                ),
            ],
        ),
    ),
    workspace_id='3da7ce52-b895-4c53-bc64-54efb0b34896',
)

res = s.destination_definition.create_custom_destination_definition(req)

if res.destination_definition_read is not None:
    # handle response
```

## delete_destination_definition

Delete a destination definition

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationDefinitionIDRequestBody(
    destination_definition_id='c3ca5acf-be2f-4d57-8757-7929177deac6',
)

res = s.destination_definition.delete_destination_definition(req)

if res.status_code == 200:
    # handle response
```

## get_destination_definition

Get destinationDefinition

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationDefinitionIDRequestBody(
    destination_definition_id='46ecb573-409e-43eb-9e5a-2b12eb07f116',
)

res = s.destination_definition.get_destination_definition(req)

if res.destination_definition_read is not None:
    # handle response
```

## get_destination_definition_for_workspace

Get a destinationDefinition that is configured for the given workspace

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationDefinitionIDWithWorkspaceID(
    destination_definition_id='db99545f-c95f-4a88-970e-189dbb30fcb3',
    workspace_id='3ea055b1-97cd-444e-af52-d82d3513bb6f',
)

res = s.destination_definition.get_destination_definition_for_workspace(req)

if res.destination_definition_read is not None:
    # handle response
```

## grant_destination_definition_to_workspace

grant a private, non-custom destinationDefinition to a given workspace

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationDefinitionIDWithWorkspaceID(
    destination_definition_id='48b656bc-db35-4ff2-a4b2-7537a8cd9e73',
    workspace_id='19c177d5-25f7-47b1-94ee-b52ff785fc37',
)

res = s.destination_definition.grant_destination_definition_to_workspace(req)

if res.private_destination_definition_read is not None:
    # handle response
```

## list_destination_definitions

List all the destinationDefinitions the current Airbyte deployment is configured to use

### Example Usage

```python
import airbyte_oss


s = airbyte_oss.AirbyteOss()


res = s.destination_definition.list_destination_definitions()

if res.destination_definition_read_list is not None:
    # handle response
```

## list_destination_definitions_for_workspace

List all the destinationDefinitions the given workspace is configured to use

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WorkspaceIDRequestBody(
    workspace_id='814d4c98-e0c2-4bb8-9eb7-5dad636c6005',
)

res = s.destination_definition.list_destination_definitions_for_workspace(req)

if res.destination_definition_read_list is not None:
    # handle response
```

## list_latest_destination_definitions

Guaranteed to retrieve the latest information on supported destinations.

### Example Usage

```python
import airbyte_oss


s = airbyte_oss.AirbyteOss()


res = s.destination_definition.list_latest_destination_definitions()

if res.destination_definition_read_list is not None:
    # handle response
```

## list_private_destination_definitions

List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WorkspaceIDRequestBody(
    workspace_id='03d8bb31-180f-4739-ae9e-057eb809e281',
)

res = s.destination_definition.list_private_destination_definitions(req)

if res.private_destination_definition_read_list is not None:
    # handle response
```

## revoke_destination_definition_from_workspace

revoke a grant to a private, non-custom destinationDefinition from a given workspace

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationDefinitionIDWithWorkspaceID(
    destination_definition_id='0331f398-1d4c-4700-b607-f3c93c73b9da',
    workspace_id='3f2ceda7-e23f-4225-b411-faf4b7544e47',
)

res = s.destination_definition.revoke_destination_definition_from_workspace(req)

if res.status_code == 200:
    # handle response
```

## update_destination_definition

Update destinationDefinition

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationDefinitionUpdate(
    destination_definition_id='2e802857-a5b4-4046-ba7d-575f1400e764',
    docker_image_tag='dolorum',
    resource_requirements=shared.ActorDefinitionResourceRequirements(
        default=shared.ResourceRequirements(
            cpu_limit='possimus',
            cpu_request='voluptate',
            memory_limit='consectetur',
            memory_request='nesciunt',
        ),
        job_specific=[
            shared.JobTypeResourceLimit(
                job_type=shared.JobTypeEnum.REPLICATE,
                resource_requirements=shared.ResourceRequirements(
                    cpu_limit='minus',
                    cpu_request='sunt',
                    memory_limit='distinctio',
                    memory_request='iusto',
                ),
            ),
            shared.JobTypeResourceLimit(
                job_type=shared.JobTypeEnum.SYNC,
                resource_requirements=shared.ResourceRequirements(
                    cpu_limit='et',
                    cpu_request='facilis',
                    memory_limit='amet',
                    memory_request='autem',
                ),
            ),
        ],
    ),
)

res = s.destination_definition.update_destination_definition(req)

if res.destination_definition_read is not None:
    # handle response
```
