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
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationIDRequestBody(
    destination_id='6312fde0-4771-4778-bf61-d017476360a1',
)

res = s.destination.check_connection_to_destination(req)

if res.check_connection_read is not None:
    # handle response
```

## check_connection_to_destination_for_update

Check connection for a proposed update to a destination

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationUpdate(
    connection_configuration='nostrum',
    destination_id='db6a6606-59a1-4ade-aab5-851d6c645b08',
    name='Gene Brekke',
)

res = s.destination.check_connection_to_destination_for_update(req)

if res.check_connection_read is not None:
    # handle response
```

## clone_destination

Clone destination

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationCloneRequestBody(
    destination_clone_id='1baa0fe1-ade0-408e-af8c-5f350d8cdb5a',
    destination_configuration=shared.DestinationCloneConfiguration(
        connection_configuration='dolor',
        name='Mrs. Stephanie Lind',
    ),
)

res = s.destination.clone_destination(req)

if res.destination_read is not None:
    # handle response
```

## create_destination

Create a destination

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationCreate(
    connection_configuration='consequatur',
    destination_definition_id='10421813-d520-48ec-a7e2-53b668451c6c',
    name='Mrs. Kate Cronin',
    workspace_id='16deab3f-ec95-478a-a458-4273a8418d16',
)

res = s.destination.create_destination(req)

if res.destination_read is not None:
    # handle response
```

## delete_destination

Delete the destination

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationIDRequestBody(
    destination_id='2309fb09-2992-41ae-bb9f-58c4d86e68e4',
)

res = s.destination.delete_destination(req)

if res.status_code == 200:
    # handle response
```

## get_destination

Get configured destination

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationIDRequestBody(
    destination_id='be056013-f59d-4a75-ba59-ecfef66ef1ca',
)

res = s.destination.get_destination(req)

if res.destination_read is not None:
    # handle response
```

## list_destinations_for_workspace

List configured destinations for a workspace

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.WorkspaceIDRequestBody(
    workspace_id='a3383c2b-eb47-4737-bc8d-72f64d1db1f2',
)

res = s.destination.list_destinations_for_workspace(req)

if res.destination_read_list is not None:
    # handle response
```

## search_destinations

Search destinations

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationSearch(
    connection_configuration='porro',
    destination_definition_id='4310661e-9634-49e1-8f9e-06e3a437000a',
    destination_id='e6b6bc9b-8f75-49ea-855a-9741d3113529',
    destination_name='ex',
    name='Patty Reinger',
    workspace_id='72026114-35e1-439d-bc22-59b1abda8c07',
)

res = s.destination.search_destinations(req)

if res.destination_read_list is not None:
    # handle response
```

## update_destination

Update a destination

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationUpdate(
    connection_configuration='ipsa',
    destination_id='e1084cb0-672d-41ad-879e-eb9665b85efb',
    name='Robert Crona',
)

res = s.destination.update_destination(req)

if res.destination_read is not None:
    # handle response
```
