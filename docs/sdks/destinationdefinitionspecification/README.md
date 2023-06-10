# destination_definition_specification

## Overview

DestinationDefinitionSpecification related resources.

### Available Operations

* [get_destination_definition_specification](#get_destination_definition_specification) - Get specification for a destinationDefinition

## get_destination_definition_specification

Get specification for a destinationDefinition

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationDefinitionIDWithWorkspaceID(
    destination_definition_id='3c93c73b-9da3-4f2c-ada7-e23f2257411f',
    workspace_id='af4b7544-e472-4e80-a857-a5b40463a7d5',
)

res = s.destination_definition_specification.get_destination_definition_specification(req)

if res.destination_definition_specification_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                      | [shared.DestinationDefinitionIDWithWorkspaceID](../../models/shared/destinationdefinitionidwithworkspaceid.md) | :heavy_check_mark:                                                                                             | The request object to use for the request.                                                                     |


### Response

**[operations.GetDestinationDefinitionSpecificationResponse](../../models/operations/getdestinationdefinitionspecificationresponse.md)**

