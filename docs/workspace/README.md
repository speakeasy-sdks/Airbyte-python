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
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WorkspaceCreate(
    anonymous_data_collection=False,
    default_geography=shared.GeographyEnum.AUTO,
    display_setup_wizard=False,
    email='Franco30@yahoo.com',
    name='Luz Hudson',
    news=False,
    notifications=[
        shared.Notification(
            customerio_configuration={
                "voluptatibus": 'facilis',
                "doloremque": 'officiis',
                "nisi": 'reprehenderit',
            },
            notification_type=shared.NotificationTypeEnum.CUSTOMERIO,
            send_on_failure=False,
            send_on_success=False,
            slack_configuration=shared.SlackNotificationConfiguration(
                webhook='alias',
            ),
        ),
        shared.Notification(
            customerio_configuration={
                "ut": 'hic',
                "facere": 'tenetur',
                "saepe": 'assumenda',
            },
            notification_type=shared.NotificationTypeEnum.SLACK,
            send_on_failure=False,
            send_on_success=False,
            slack_configuration=shared.SlackNotificationConfiguration(
                webhook='exercitationem',
            ),
        ),
        shared.Notification(
            customerio_configuration={
                "sit": 'recusandae',
                "a": 'exercitationem',
            },
            notification_type=shared.NotificationTypeEnum.SLACK,
            send_on_failure=False,
            send_on_success=False,
            slack_configuration=shared.SlackNotificationConfiguration(
                webhook='mollitia',
            ),
        ),
    ],
    security_updates=False,
    webhook_configs=[
        shared.WebhookConfigWrite(
            auth_token='ut',
            name='Ryan Prosacco',
            validation_url='recusandae',
        ),
    ],
)

res = s.workspace.create_workspace(req)

if res.workspace_read is not None:
    # handle response
```

## delete_workspace

Deletes a workspace

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WorkspaceIDRequestBody(
    workspace_id='99731adc-05d8-45ae-adfb-70fb3874290d',
)

res = s.workspace.delete_workspace(req)

if res.status_code == 200:
    # handle response
```

## get_workspace

Find workspace by ID

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WorkspaceIDRequestBody(
    workspace_id='336561ec-a16e-4f89-851b-d76eeeb518c4',
)

res = s.workspace.get_workspace(req)

if res.workspace_read is not None:
    # handle response
```

## get_workspace_by_connection_id

Find workspace by connection id

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.ConnectionIDRequestBody(
    connection_id='da1fad35-512f-406d-8e5b-72f0f548568a',
)

res = s.workspace.get_workspace_by_connection_id(req)

if res.workspace_read is not None:
    # handle response
```

## get_workspace_by_slug

Find workspace by slug

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SlugRequestBody(
    slug='consequatur',
)

res = s.workspace.get_workspace_by_slug(req)

if res.workspace_read is not None:
    # handle response
```

## list_workspaces

List all workspaces registered in the current Airbyte deployment

### Example Usage

```python
import airbyte_oss


s = airbyte_oss.AirbyteOss()


res = s.workspace.list_workspaces()

if res.workspace_read_list is not None:
    # handle response
```

## update_workspace

Update workspace state

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WorkspaceUpdate(
    anonymous_data_collection=False,
    default_geography=shared.GeographyEnum.AUTO,
    display_setup_wizard=False,
    email='Effie2@gmail.com',
    initial_setup_complete=False,
    news=False,
    notifications=[
        shared.Notification(
            customerio_configuration={
                "quibusdam": 'autem',
            },
            notification_type=shared.NotificationTypeEnum.CUSTOMERIO,
            send_on_failure=False,
            send_on_success=False,
            slack_configuration=shared.SlackNotificationConfiguration(
                webhook='tempore',
            ),
        ),
        shared.Notification(
            customerio_configuration={
                "modi": 'ratione',
                "aliquam": 'ea',
                "aliquam": 'corporis',
            },
            notification_type=shared.NotificationTypeEnum.CUSTOMERIO,
            send_on_failure=False,
            send_on_success=False,
            slack_configuration=shared.SlackNotificationConfiguration(
                webhook='ipsa',
            ),
        ),
        shared.Notification(
            customerio_configuration={
                "aut": 'molestias',
            },
            notification_type=shared.NotificationTypeEnum.SLACK,
            send_on_failure=False,
            send_on_success=False,
            slack_configuration=shared.SlackNotificationConfiguration(
                webhook='repellat',
            ),
        ),
    ],
    security_updates=False,
    webhook_configs=[
        shared.WebhookConfigWrite(
            auth_token='libero',
            name='Alvin Runolfsdottir',
            validation_url='a',
        ),
        shared.WebhookConfigWrite(
            auth_token='tenetur',
            name='Mr. Bernadette Quigley',
            validation_url='debitis',
        ),
        shared.WebhookConfigWrite(
            auth_token='enim',
            name='Eloise Hintz',
            validation_url='animi',
        ),
    ],
    workspace_id='45ac82b8-5f8b-4c2c-aba8-da4127dd597f',
)

res = s.workspace.update_workspace(req)

if res.workspace_read is not None:
    # handle response
```

## update_workspace_feedback

Update workspace feedback state

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WorkspaceGiveFeedback(
    workspace_id='f4711aa1-bc74-4b86-8ecc-74f77b4848bd',
)

res = s.workspace.update_workspace_feedback(req)

if res.status_code == 200:
    # handle response
```

## update_workspace_name

Update workspace name

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WorkspaceUpdateName(
    name='Angie Johnston I',
    workspace_id='41d2c3b8-0809-4437-be06-0459bebbad02',
)

res = s.workspace.update_workspace_name(req)

if res.workspace_read is not None:
    # handle response
```
