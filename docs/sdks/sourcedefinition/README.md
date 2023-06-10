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
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.CustomSourceDefinitionCreate(
    source_definition=shared.SourceDefinitionCreate(
        docker_image_tag='vero',
        docker_repository='eos',
        documentation_url='http://tattered-pilgrimage.com',
        icon='commodi',
        name='Sylvester Cormier',
        resource_requirements=shared.ActorDefinitionResourceRequirements(
            default=shared.ResourceRequirements(
                cpu_limit='iusto',
                cpu_request='ab',
                memory_limit='deserunt',
                memory_request='sed',
            ),
            job_specific=[
                shared.JobTypeResourceLimit(
                    job_type=shared.JobType.RESET_CONNECTION,
                    resource_requirements=shared.ResourceRequirements(
                        cpu_limit='placeat',
                        cpu_request='ullam',
                        memory_limit='molestiae',
                        memory_request='itaque',
                    ),
                ),
                shared.JobTypeResourceLimit(
                    job_type=shared.JobType.SYNC,
                    resource_requirements=shared.ResourceRequirements(
                        cpu_limit='nemo',
                        cpu_request='non',
                        memory_limit='recusandae',
                        memory_request='omnis',
                    ),
                ),
                shared.JobTypeResourceLimit(
                    job_type=shared.JobType.GET_SPEC,
                    resource_requirements=shared.ResourceRequirements(
                        cpu_limit='aliquam',
                        cpu_request='dolor',
                        memory_limit='occaecati',
                        memory_request='quibusdam',
                    ),
                ),
            ],
        ),
    ),
    workspace_id='22246569-4624-4070-84f7-ab37cef02225',
)

res = s.source_definition.create_custom_source_definition(req)

if res.source_definition_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [shared.CustomSourceDefinitionCreate](../../models/shared/customsourcedefinitioncreate.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.CreateCustomSourceDefinitionResponse](../../models/operations/createcustomsourcedefinitionresponse.md)**


## delete_source_definition

Delete a source definition

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceDefinitionIDRequestBody(
    source_definition_id='194db554-10ad-4c66-9af9-0a26c7cdc981',
)

res = s.source_definition.delete_source_definition(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.SourceDefinitionIDRequestBody](../../models/shared/sourcedefinitionidrequestbody.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.DeleteSourceDefinitionResponse](../../models/operations/deletesourcedefinitionresponse.md)**


## get_source_definition

Get source

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceDefinitionIDRequestBody(
    source_definition_id='f068981d-6bb3-43cf-aa34-8c31bf407ee4',
)

res = s.source_definition.get_source_definition(req)

if res.source_definition_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [shared.SourceDefinitionIDRequestBody](../../models/shared/sourcedefinitionidrequestbody.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetSourceDefinitionResponse](../../models/operations/getsourcedefinitionresponse.md)**


## get_source_definition_for_workspace

Get a sourceDefinition that is configured for the given workspace

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceDefinitionIDWithWorkspaceID(
    source_definition_id='fcf0c42b-78f1-4562-a398-a0dc766324cc',
    workspace_id='b06c8ca1-2d02-4529-a70b-8d5722dd895b',
)

res = s.source_definition.get_source_definition_for_workspace(req)

if res.source_definition_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [shared.SourceDefinitionIDWithWorkspaceID](../../models/shared/sourcedefinitionidwithworkspaceid.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetSourceDefinitionForWorkspaceResponse](../../models/operations/getsourcedefinitionforworkspaceresponse.md)**


## grant_source_definition_to_workspace

grant a private, non-custom sourceDefinition to a given workspace

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceDefinitionIDWithWorkspaceID(
    source_definition_id='8bcf24db-9596-4933-92f7-4533994d78de',
    workspace_id='3b6e9389-f5ab-4b7f-a625-50a28382ac48',
)

res = s.source_definition.grant_source_definition_to_workspace(req)

if res.private_source_definition_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [shared.SourceDefinitionIDWithWorkspaceID](../../models/shared/sourcedefinitionidwithworkspaceid.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GrantSourceDefinitionToWorkspaceResponse](../../models/operations/grantsourcedefinitiontoworkspaceresponse.md)**


## list_latest_source_definitions

Guaranteed to retrieve the latest information on supported sources.

### Example Usage

```python
import airbyte


s = airbyte.Airbyte()


res = s.source_definition.list_latest_source_definitions()

if res.source_definition_read_list is not None:
    # handle response
```


### Response

**[operations.ListLatestSourceDefinitionsResponse](../../models/operations/listlatestsourcedefinitionsresponse.md)**


## list_private_source_definitions

List all private, non-custom sourceDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WorkspaceIDRequestBody(
    workspace_id='3afd2315-bba6-4501-a4e0-6f5bf6ae591b',
)

res = s.source_definition.list_private_source_definitions(req)

if res.private_source_definition_read_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.WorkspaceIDRequestBody](../../models/shared/workspaceidrequestbody.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListPrivateSourceDefinitionsResponse](../../models/operations/listprivatesourcedefinitionsresponse.md)**


## list_source_definitions

List all the sourceDefinitions the current Airbyte deployment is configured to use

### Example Usage

```python
import airbyte


s = airbyte.Airbyte()


res = s.source_definition.list_source_definitions()

if res.source_definition_read_list is not None:
    # handle response
```


### Response

**[operations.ListSourceDefinitionsResponse](../../models/operations/listsourcedefinitionsresponse.md)**


## list_source_definitions_for_workspace

List all the sourceDefinitions the given workspace is configured to use

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WorkspaceIDRequestBody(
    workspace_id='c8bdef36-12b6-43c2-85fd-a840774a68a9',
)

res = s.source_definition.list_source_definitions_for_workspace(req)

if res.source_definition_read_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.WorkspaceIDRequestBody](../../models/shared/workspaceidrequestbody.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListSourceDefinitionsForWorkspaceResponse](../../models/operations/listsourcedefinitionsforworkspaceresponse.md)**


## revoke_source_definition_from_workspace

revoke a grant to a private, non-custom sourceDefinition from a given workspace

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceDefinitionIDWithWorkspaceID(
    source_definition_id='a35d086b-6f66-4fef-820e-9f443b4257b9',
    workspace_id='92c8dbda-6a61-4efa-a198-258fd0a9eba4',
)

res = s.source_definition.revoke_source_definition_from_workspace(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [shared.SourceDefinitionIDWithWorkspaceID](../../models/shared/sourcedefinitionidwithworkspaceid.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.RevokeSourceDefinitionFromWorkspaceResponse](../../models/operations/revokesourcedefinitionfromworkspaceresponse.md)**


## update_source_definition

Update a sourceDefinition

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceDefinitionUpdate(
    docker_image_tag='voluptate',
    resource_requirements=shared.ActorDefinitionResourceRequirements(
        default=shared.ResourceRequirements(
            cpu_limit='voluptatibus',
            cpu_request='quam',
            memory_limit='nulla',
            memory_request='dolorem',
        ),
        job_specific=[
            shared.JobTypeResourceLimit(
                job_type=shared.JobType.REPLICATE,
                resource_requirements=shared.ResourceRequirements(
                    cpu_limit='perferendis',
                    cpu_request='quaerat',
                    memory_limit='excepturi',
                    memory_request='aliquid',
                ),
            ),
            shared.JobTypeResourceLimit(
                job_type=shared.JobType.DISCOVER_SCHEMA,
                resource_requirements=shared.ResourceRequirements(
                    cpu_limit='voluptatem',
                    cpu_request='illum',
                    memory_limit='laboriosam',
                    memory_request='culpa',
                ),
            ),
            shared.JobTypeResourceLimit(
                job_type=shared.JobType.GET_SPEC,
                resource_requirements=shared.ResourceRequirements(
                    cpu_limit='atque',
                    cpu_request='ratione',
                    memory_limit='vitae',
                    memory_request='quisquam',
                ),
            ),
            shared.JobTypeResourceLimit(
                job_type=shared.JobType.SYNC,
                resource_requirements=shared.ResourceRequirements(
                    cpu_limit='nihil',
                    cpu_request='culpa',
                    memory_limit='temporibus',
                    memory_request='a',
                ),
            ),
        ],
    ),
    source_definition_id='596fdf1a-d837-4ae8-8c1c-19c95ba99867',
)

res = s.source_definition.update_source_definition(req)

if res.source_definition_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.SourceDefinitionUpdate](../../models/shared/sourcedefinitionupdate.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.UpdateSourceDefinitionResponse](../../models/operations/updatesourcedefinitionresponse.md)**

