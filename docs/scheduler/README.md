# scheduler

### Available Operations

* [execute_destination_check_connection](#execute_destination_check_connection) - Run check connection for a given destination configuration
* [execute_source_check_connection](#execute_source_check_connection) - Run check connection for a given source configuration
* [execute_source_discover_schema](#execute_source_discover_schema) - Run discover schema for a given source a source configuration

## execute_destination_check_connection

Run check connection for a given destination configuration

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.DestinationCoreConfig(
    connection_configuration='adipisci',
    destination_definition_id='04f926ba-d255-4381-9b47-4b0ed20e5624',
    destination_id='8fff639a-910a-4bdc-ab62-676696e1ec00',
    workspace_id='221b335d-89ac-4b3e-8fda-8d0c549ef030',
)

res = s.scheduler.execute_destination_check_connection(req)

if res.check_connection_read is not None:
    # handle response
```

## execute_source_check_connection

Run check connection for a given source configuration

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceCoreConfig(
    connection_configuration='doloremque',
    source_definition_id='4978a61f-a1cf-4206-88f7-7c1ffc71dca1',
    source_id='63f2a3c8-0a97-4ff3-b4cd-df857a9e6187',
    workspace_id='6c6ab21d-29df-4c94-96fe-cd799390066a',
)

res = s.scheduler.execute_source_check_connection(req)

if res.check_connection_read is not None:
    # handle response
```

## execute_source_discover_schema

Run discover schema for a given source a source configuration

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.SourceCoreConfig(
    connection_configuration='autem',
    source_definition_id='d2d00035-5338-4cec-886f-a21e9152cb31',
    source_id='19167b8e-3c8d-4b03-808d-6d364ffd4559',
    workspace_id='06d1263d-48e9-435c-ac9e-81f30be3e432',
)

res = s.scheduler.execute_source_discover_schema(req)

if res.source_discover_schema_read is not None:
    # handle response
```
