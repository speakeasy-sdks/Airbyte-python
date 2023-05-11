# destination_definition_specification

## Overview

DestinationDefinitionSpecification related resources.

### Available Operations

* [get_destination_definition_specification](#get_destination_definition_specification) - Get specification for a destinationDefinition

## get_destination_definition_specification

Get specification for a destinationDefinition

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationDefinitionIDWithWorkspaceID(
    destination_definition_id='a08088d1-00ef-4ada-a00e-f0422eb2164c',
    workspace_id='f9ab8366-c723-4ffd-a9e0-6bee4825c1fc',
)

res = s.destination_definition_specification.get_destination_definition_specification(req)

if res.destination_definition_specification_read is not None:
    # handle response
```
