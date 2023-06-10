# destination

## Overview

Destination related resources.

### Available Operations

* [check_connection_to_destination](#check_connection_to_destination) - Check connection to the destination
* [check_connection_to_destination_for_update](#check_connection_to_destination_for_update) - Check connection for a proposed update to a destination
* [clone_destination](#clone_destination) - Clone destination
* [create_destination](#create_destination) - Create a destination
* [delete_destination](#delete_destination) - Delete the destination
* [get_destination](#get_destination) - Get configured destination
* [list_destinations_for_workspace](#list_destinations_for_workspace) - List configured destinations for a workspace
* [search_destinations](#search_destinations) - Search destinations
* [update_destination](#update_destination) - Update a destination

## check_connection_to_destination

Check connection to the destination

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationIDRequestBody(
    destination_id='7956f925-1a5a-49da-a60f-f57bfaad4f9e',
)

res = s.destination.check_connection_to_destination(req)

if res.check_connection_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.DestinationIDRequestBody](../../models/shared/destinationidrequestbody.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CheckConnectionToDestinationResponse](../../models/operations/checkconnectiontodestinationresponse.md)**


## check_connection_to_destination_for_update

Check connection for a proposed update to a destination

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationUpdate(
    connection_configuration='sapiente',
    destination_id='c1b4512c-1032-4648-9c2f-615199ebfd0e',
    name='Cary Toy',
)

res = s.destination.check_connection_to_destination_for_update(req)

if res.check_connection_read is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.DestinationUpdate](../../models/shared/destinationupdate.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CheckConnectionToDestinationForUpdateResponse](../../models/operations/checkconnectiontodestinationforupdateresponse.md)**


## clone_destination

Clone destination

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationCloneRequestBody(
    destination_clone_id='632ca3ae-d011-4799-a312-fde04771778f',
    destination_configuration=shared.DestinationCloneConfiguration(
        connection_configuration='reiciendis',
        name='Mr. Diane Stiedemann',
    ),
)

res = s.destination.clone_destination(req)

if res.destination_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [shared.DestinationCloneRequestBody](../../models/shared/destinationclonerequestbody.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CloneDestinationResponse](../../models/operations/clonedestinationresponse.md)**


## create_destination

Create a destination

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationCreate(
    connection_configuration='tempora',
    destination_definition_id='76360a15-db6a-4660-a59a-1adeaab5851d',
    name='Krista Jakubowski',
    workspace_id='b08b6189-1baa-40fe-9ade-008e6f8c5f35',
)

res = s.destination.create_destination(req)

if res.destination_read is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.DestinationCreate](../../models/shared/destinationcreate.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.CreateDestinationResponse](../../models/operations/createdestinationresponse.md)**


## delete_destination

Delete the destination

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationIDRequestBody(
    destination_id='0d8cdb5a-3418-4143-8104-21813d5208ec',
)

res = s.destination.delete_destination(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.DestinationIDRequestBody](../../models/shared/destinationidrequestbody.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.DeleteDestinationResponse](../../models/operations/deletedestinationresponse.md)**


## get_destination

Get configured destination

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationIDRequestBody(
    destination_id='e7e253b6-6845-41c6-86e2-05e16deab3fe',
)

res = s.destination.get_destination(req)

if res.destination_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.DestinationIDRequestBody](../../models/shared/destinationidrequestbody.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetDestinationResponse](../../models/operations/getdestinationresponse.md)**


## list_destinations_for_workspace

List configured destinations for a workspace

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WorkspaceIDRequestBody(
    workspace_id='c9578a64-5842-473a-8418-d162309fb092',
)

res = s.destination.list_destinations_for_workspace(req)

if res.destination_read_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.WorkspaceIDRequestBody](../../models/shared/workspaceidrequestbody.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.ListDestinationsForWorkspaceResponse](../../models/operations/listdestinationsforworkspaceresponse.md)**


## search_destinations

Search destinations

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationSearch(
    connection_configuration='occaecati',
    destination_definition_id='921aefb9-f58c-44d8-ae68-e4be056013f5',
    destination_id='9da757a5-9ecf-4ef6-aef1-caa3383c2beb',
    destination_name='dolore',
    name='Colleen Dickinson',
    workspace_id='c8d72f64-d1db-41f2-8431-0661e96349e1',
)

res = s.destination.search_destinations(req)

if res.destination_read_list is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.DestinationSearch](../../models/shared/destinationsearch.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.SearchDestinationsResponse](../../models/operations/searchdestinationsresponse.md)**


## update_destination

Update a destination

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationUpdate(
    connection_configuration='impedit',
    destination_id='f9e06e3a-4370-400a-a6b6-bc9b8f759eac',
    name='Dana Ortiz',
)

res = s.destination.update_destination(req)

if res.destination_read is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [shared.DestinationUpdate](../../models/shared/destinationupdate.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.UpdateDestinationResponse](../../models/operations/updatedestinationresponse.md)**

