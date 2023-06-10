# workspace

## Overview

Workspace related resources.

### Available Operations

* [create_workspace](#create_workspace) - Creates a workspace
* [delete_workspace](#delete_workspace) - Deletes a workspace
* [get_workspace](#get_workspace) - Find workspace by ID
* [get_workspace_by_connection_id](#get_workspace_by_connection_id) - Find workspace by connection id
* [get_workspace_by_slug](#get_workspace_by_slug) - Find workspace by slug
* [list_workspaces](#list_workspaces) - List all workspaces registered in the current Airbyte deployment
* [update_workspace](#update_workspace) - Update workspace state
* [update_workspace_feedback](#update_workspace_feedback) - Update workspace feedback state
* [update_workspace_name](#update_workspace_name) - Update workspace name

## create_workspace

Creates a workspace

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WorkspaceCreate(
    anonymous_data_collection=False,
    default_geography=shared.Geography.US,
    display_setup_wizard=False,
    email='Eliseo_Feil@hotmail.com',
    name='Becky Daugherty',
    news=False,
    notifications=[
        shared.Notification(
            customerio_configuration=shared.CustomerioNotificationConfiguration(),
            notification_type=shared.NotificationType.CUSTOMERIO,
            send_on_failure=False,
            send_on_success=False,
            slack_configuration=shared.SlackNotificationConfiguration(
                webhook='temporibus',
            ),
        ),
        shared.Notification(
            customerio_configuration=shared.CustomerioNotificationConfiguration(),
            notification_type=shared.NotificationType.CUSTOMERIO,
            send_on_failure=False,
            send_on_success=False,
            slack_configuration=shared.SlackNotificationConfiguration(
                webhook='quaerat',
            ),
        ),
        shared.Notification(
            customerio_configuration=shared.CustomerioNotificationConfiguration(),
            notification_type=shared.NotificationType.CUSTOMERIO,
            send_on_failure=False,
            send_on_success=False,
            slack_configuration=shared.SlackNotificationConfiguration(
                webhook='molestiae',
            ),
        ),
        shared.Notification(
            customerio_configuration=shared.CustomerioNotificationConfiguration(),
            notification_type=shared.NotificationType.CUSTOMERIO,
            send_on_failure=False,
            send_on_success=False,
            slack_configuration=shared.SlackNotificationConfiguration(
                webhook='laborum',
            ),
        ),
    ],
    security_updates=False,
    webhook_configs=[
        shared.WebhookConfigWrite(
            auth_token='rerum',
            name='Mr. Megan Botsford',
            validation_url='perspiciatis',
        ),
    ],
)

res = s.workspace.create_workspace(req)

if res.workspace_read is not None:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [shared.WorkspaceCreate](../../models/shared/workspacecreate.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.CreateWorkspaceResponse](../../models/operations/createworkspaceresponse.md)**


## delete_workspace

Deletes a workspace

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WorkspaceIDRequestBody(
    workspace_id='5d1e6698-fcc4-4596-a17c-297767633425',
)

res = s.workspace.delete_workspace(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.WorkspaceIDRequestBody](../../models/shared/workspaceidrequestbody.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.DeleteWorkspaceResponse](../../models/operations/deleteworkspaceresponse.md)**


## get_workspace

Find workspace by ID

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WorkspaceIDRequestBody(
    workspace_id='4038bfb5-971e-4981-9055-7389cedbac7f',
)

res = s.workspace.get_workspace(req)

if res.workspace_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.WorkspaceIDRequestBody](../../models/shared/workspaceidrequestbody.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetWorkspaceResponse](../../models/operations/getworkspaceresponse.md)**


## get_workspace_by_connection_id

Find workspace by connection id

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.ConnectionIDRequestBody(
    connection_id='da39594d-66bc-42ae-8806-32b9954b6fa2',
)

res = s.workspace.get_workspace_by_connection_id(req)

if res.workspace_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.ConnectionIDRequestBody](../../models/shared/connectionidrequestbody.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetWorkspaceByConnectionIDResponse](../../models/operations/getworkspacebyconnectionidresponse.md)**


## get_workspace_by_slug

Find workspace by slug

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SlugRequestBody(
    slug='explicabo',
)

res = s.workspace.get_workspace_by_slug(req)

if res.workspace_read is not None:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [shared.SlugRequestBody](../../models/shared/slugrequestbody.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.GetWorkspaceBySlugResponse](../../models/operations/getworkspacebyslugresponse.md)**


## list_workspaces

List all workspaces registered in the current Airbyte deployment

### Example Usage

```python
import airbyte


s = airbyte.Airbyte()


res = s.workspace.list_workspaces()

if res.workspace_read_list is not None:
    # handle response
```


### Response

**[operations.ListWorkspacesResponse](../../models/operations/listworkspacesresponse.md)**


## update_workspace

Update workspace state

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WorkspaceUpdate(
    anonymous_data_collection=False,
    default_geography=shared.Geography.AUTO,
    display_setup_wizard=False,
    email='Colten_Johnson@yahoo.com',
    initial_setup_complete=False,
    news=False,
    notifications=[
        shared.Notification(
            customerio_configuration=shared.CustomerioNotificationConfiguration(),
            notification_type=shared.NotificationType.CUSTOMERIO,
            send_on_failure=False,
            send_on_success=False,
            slack_configuration=shared.SlackNotificationConfiguration(
                webhook='ipsam',
            ),
        ),
    ],
    security_updates=False,
    webhook_configs=[
        shared.WebhookConfigWrite(
            auth_token='sequi',
            name='Mr. Pete Bergstrom III',
            validation_url='tempore',
        ),
        shared.WebhookConfigWrite(
            auth_token='necessitatibus',
            name='Randall McLaughlin DVM',
            validation_url='quod',
        ),
    ],
    workspace_id='2053b749-366a-4c8e-a0f2-bf19588d40d0',
)

res = s.workspace.update_workspace(req)

if res.workspace_read is not None:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [shared.WorkspaceUpdate](../../models/shared/workspaceupdate.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.UpdateWorkspaceResponse](../../models/operations/updateworkspaceresponse.md)**


## update_workspace_feedback

Update workspace feedback state

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WorkspaceGiveFeedback(
    workspace_id='3f3deba2-97be-43e9-8bc4-0df868fd5240',
)

res = s.workspace.update_workspace_feedback(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.WorkspaceGiveFeedback](../../models/shared/workspacegivefeedback.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.UpdateWorkspaceFeedbackResponse](../../models/operations/updateworkspacefeedbackresponse.md)**


## update_workspace_name

Update workspace name

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.WorkspaceUpdateName(
    name='Leticia Renner',
    workspace_id='1d492f4f-127f-4b0e-8bf1-f8217978d0ac',
)

res = s.workspace.update_workspace_name(req)

if res.workspace_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.WorkspaceUpdateName](../../models/shared/workspaceupdatename.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.UpdateWorkspaceNameResponse](../../models/operations/updateworkspacenameresponse.md)**

