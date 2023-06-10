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
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.CustomDestinationDefinitionCreate(
    destination_definition=shared.DestinationDefinitionCreate(
        docker_image_tag='labore',
        docker_repository='veritatis',
        documentation_url='https://empty-buffer.com',
        icon='dolorem',
        name='Tina Moore',
        resource_requirements=shared.ActorDefinitionResourceRequirements(
            default=shared.ResourceRequirements(
                cpu_limit='soluta',
                cpu_request='libero',
                memory_limit='rem',
                memory_request='dolorum',
            ),
            job_specific=[
                shared.JobTypeResourceLimit(
                    job_type=shared.JobType.CHECK_CONNECTION,
                    resource_requirements=shared.ResourceRequirements(
                        cpu_limit='alias',
                        cpu_request='magni',
                        memory_limit='vel',
                        memory_request='quae',
                    ),
                ),
                shared.JobTypeResourceLimit(
                    job_type=shared.JobType.GET_SPEC,
                    resource_requirements=shared.ResourceRequirements(
                        cpu_limit='modi',
                        cpu_request='neque',
                        memory_limit='exercitationem',
                        memory_request='itaque',
                    ),
                ),
            ],
        ),
    ),
    workspace_id='139dbc22-59b1-4abd-a8c0-70e1084cb067',
)

res = s.destination_definition.create_custom_destination_definition(req)

if res.destination_definition_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [shared.CustomDestinationDefinitionCreate](../../models/shared/customdestinationdefinitioncreate.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.CreateCustomDestinationDefinitionResponse](../../models/operations/createcustomdestinationdefinitionresponse.md)**


## delete_destination_definition

Delete a destination definition

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationDefinitionIDRequestBody(
    destination_definition_id='2d1ad879-eeb9-4665-b85e-fbd02bae0be2',
)

res = s.destination_definition.delete_destination_definition(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [shared.DestinationDefinitionIDRequestBody](../../models/shared/destinationdefinitionidrequestbody.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.DeleteDestinationDefinitionResponse](../../models/operations/deletedestinationdefinitionresponse.md)**


## get_destination_definition

Get destinationDefinition

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationDefinitionIDRequestBody(
    destination_definition_id='d782259e-3ea4-4b51-97f9-2443da7ce52b',
)

res = s.destination_definition.get_destination_definition(req)

if res.destination_definition_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [shared.DestinationDefinitionIDRequestBody](../../models/shared/destinationdefinitionidrequestbody.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetDestinationDefinitionResponse](../../models/operations/getdestinationdefinitionresponse.md)**


## get_destination_definition_for_workspace

Get a destinationDefinition that is configured for the given workspace

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationDefinitionIDWithWorkspaceID(
    destination_definition_id='895c537c-6454-4efb-8b34-896c3ca5acfb',
    workspace_id='e2fd5707-5779-4291-b7de-ac646ecb5734',
)

res = s.destination_definition.get_destination_definition_for_workspace(req)

if res.destination_definition_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [shared.DestinationDefinitionIDWithWorkspaceID](../../models/shared/destinationdefinitionidwithworkspaceid.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetDestinationDefinitionForWorkspaceResponse](../../models/operations/getdestinationdefinitionforworkspaceresponse.md)**


## grant_destination_definition_to_workspace

grant a private, non-custom destinationDefinition to a given workspace

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationDefinitionIDWithWorkspaceID(
    destination_definition_id='09e3eb1e-5a2b-412e-b07f-116db99545fc',
    workspace_id='95fa8897-0e18-49db-b30f-cb33ea055b19',
)

res = s.destination_definition.grant_destination_definition_to_workspace(req)

if res.private_destination_definition_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [shared.DestinationDefinitionIDWithWorkspaceID](../../models/shared/destinationdefinitionidwithworkspaceid.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GrantDestinationDefinitionToWorkspaceResponse](../../models/operations/grantdestinationdefinitiontoworkspaceresponse.md)**


## list_destination_definitions

List all the destinationDefinitions the current Airbyte deployment is configured to use

### Example Usage

```python
import airbyte


s = airbyte.Airbyte()


res = s.destination_definition.list_destination_definitions()

if res.destination_definition_read_list is not None:
    # handle response
```


### Response

**[operations.ListDestinationDefinitionsResponse](../../models/operations/listdestinationdefinitionsresponse.md)**


## list_destination_definitions_for_workspace

List all the destinationDefinitions the given workspace is configured to use

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WorkspaceIDRequestBody(
    workspace_id='7cd44e2f-52d8-42d3-913b-b6f48b656bcd',
)

res = s.destination_definition.list_destination_definitions_for_workspace(req)

if res.destination_definition_read_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.WorkspaceIDRequestBody](../../models/shared/workspaceidrequestbody.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListDestinationDefinitionsForWorkspaceResponse](../../models/operations/listdestinationdefinitionsforworkspaceresponse.md)**


## list_latest_destination_definitions

Guaranteed to retrieve the latest information on supported destinations.

### Example Usage

```python
import airbyte


s = airbyte.Airbyte()


res = s.destination_definition.list_latest_destination_definitions()

if res.destination_definition_read_list is not None:
    # handle response
```


### Response

**[operations.ListLatestDestinationDefinitionsResponse](../../models/operations/listlatestdestinationdefinitionsresponse.md)**


## list_private_destination_definitions

List all private, non-custom destinationDefinitions, and for each indicate whether the given workspace has a grant for using the definition. Used by admins to view and modify a given workspace's grants.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WorkspaceIDRequestBody(
    workspace_id='b35ff2e4-b275-437a-8cd9-e7319c177d52',
)

res = s.destination_definition.list_private_destination_definitions(req)

if res.private_destination_definition_read_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.WorkspaceIDRequestBody](../../models/shared/workspaceidrequestbody.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListPrivateDestinationDefinitionsResponse](../../models/operations/listprivatedestinationdefinitionsresponse.md)**


## revoke_destination_definition_from_workspace

revoke a grant to a private, non-custom destinationDefinition from a given workspace

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationDefinitionIDWithWorkspaceID(
    destination_definition_id='5f77b114-eeb5-42ff-b85f-c37814d4c98e',
    workspace_id='0c2bb89e-b75d-4ad6-b6c6-00503d8bb311',
)

res = s.destination_definition.revoke_destination_definition_from_workspace(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [shared.DestinationDefinitionIDWithWorkspaceID](../../models/shared/destinationdefinitionidwithworkspaceid.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.RevokeDestinationDefinitionFromWorkspaceResponse](../../models/operations/revokedestinationdefinitionfromworkspaceresponse.md)**


## update_destination_definition

Update destinationDefinition

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationDefinitionUpdate(
    destination_definition_id='80f739ae-9e05-47eb-809e-2810331f3981',
    docker_image_tag='at',
    resource_requirements=shared.ActorDefinitionResourceRequirements(
        default=shared.ResourceRequirements(
            cpu_limit='labore',
            cpu_request='minus',
            memory_limit='esse',
            memory_request='voluptatem',
        ),
        job_specific=[
            shared.JobTypeResourceLimit(
                job_type=shared.JobType.RESET_CONNECTION,
                resource_requirements=shared.ResourceRequirements(
                    cpu_limit='ea',
                    cpu_request='aperiam',
                    memory_limit='dignissimos',
                    memory_request='repellat',
                ),
            ),
        ],
    ),
)

res = s.destination_definition.update_destination_definition(req)

if res.destination_definition_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.DestinationDefinitionUpdate](../../models/shared/destinationdefinitionupdate.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.UpdateDestinationDefinitionResponse](../../models/operations/updatedestinationdefinitionresponse.md)**

