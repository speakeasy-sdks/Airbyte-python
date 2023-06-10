# scheduler

### Available Operations

* [execute_destination_check_connection](#execute_destination_check_connection) - Run check connection for a given destination configuration
* [execute_source_check_connection](#execute_source_check_connection) - Run check connection for a given source configuration
* [execute_source_discover_schema](#execute_source_discover_schema) - Run discover schema for a given source a source configuration

## execute_destination_check_connection

Run check connection for a given destination configuration

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.DestinationCoreConfig(
    connection_configuration='ipsa',
    destination_definition_id='f5ae2f3a-6b70-4087-8756-143f5a6c98b5',
    destination_id='5554080d-40bc-4acc-acbd-6b5f3ec90930',
    workspace_id='4f926bad-2553-4819-b474-b0ed20e56248',
)

res = s.scheduler.execute_destination_check_connection(req)

if res.check_connection_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.DestinationCoreConfig](../../models/shared/destinationcoreconfig.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.ExecuteDestinationCheckConnectionResponse](../../models/operations/executedestinationcheckconnectionresponse.md)**


## execute_source_check_connection

Run check connection for a given source configuration

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceCoreConfig(
    connection_configuration='hic',
    source_definition_id='ff639a91-0abd-4cab-a267-6696e1ec0022',
    source_id='1b335d89-acb3-4ecf-9a8d-0c549ef03004',
    workspace_id='978a61fa-1cf2-4068-8f77-c1ffc71dca16',
)

res = s.scheduler.execute_source_check_connection(req)

if res.check_connection_read is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.SourceCoreConfig](../../models/shared/sourcecoreconfig.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.ExecuteSourceCheckConnectionResponse](../../models/operations/executesourcecheckconnectionresponse.md)**


## execute_source_discover_schema

Run discover schema for a given source a source configuration

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.SourceCoreConfig(
    connection_configuration='consectetur',
    source_definition_id='f2a3c80a-97ff-4334-8ddf-857a9e61876c',
    source_id='6ab21d29-dfc9-44d6-becd-799390066a6d',
    workspace_id='2d000355-338c-4ec0-86fa-21e9152cb311',
)

res = s.scheduler.execute_source_discover_schema(req)

if res.source_discover_schema_read is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.SourceCoreConfig](../../models/shared/sourcecoreconfig.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.ExecuteSourceDiscoverSchemaResponse](../../models/operations/executesourcediscoverschemaresponse.md)**

