# source_definition_specification

## Overview

SourceDefinition specification related resources.

### Available Operations

* [get_source_definition_specification](#get_source_definition_specification) - Get specification for a SourceDefinition.

## get_source_definition_specification

Get specification for a SourceDefinition.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceDefinitionIDWithWorkspaceID(
    source_definition_id='ef890a54-b475-4f16-b56d-385a3c4ac631',
    workspace_id='b99e26ce-d8f9-4fdb-9410-f63bbf817837',
)

res = s.source_definition_specification.get_source_definition_specification(req)

if res.source_definition_specification_read is not None:
    # handle response
```
