# source_definition_specification

## Overview

SourceDefinition specification related resources.

### Available Operations

* [get_source_definition_specification](#get_source_definition_specification) - Get specification for a SourceDefinition.

## get_source_definition_specification

Get specification for a SourceDefinition.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceDefinitionIDWithWorkspaceID(
    source_definition_id='8fa3f696-991a-4f38-8ce0-3614448c7977',
    workspace_id='a0ef2f53-6028-4efe-af93-4152ed7e253f',
)

res = s.source_definition_specification.get_source_definition_specification(req)

if res.source_definition_specification_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [shared.SourceDefinitionIDWithWorkspaceID](../../models/shared/sourcedefinitionidwithworkspaceid.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetSourceDefinitionSpecificationResponse](../../models/operations/getsourcedefinitionspecificationresponse.md)**

