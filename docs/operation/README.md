# operation

### Available Operations

* [check_operation](#check_operation) - Check if an operation to be created is valid
* [create_operation](#create_operation) - Create an operation to be applied as part of a connection pipeline
* [delete_operation](#delete_operation) - Delete an operation
* [get_operation](#get_operation) - Returns an operation
* [list_operations_for_connection](#list_operations_for_connection) - Returns all operations for a connection.
* [update_operation](#update_operation) - Update an operation

## check_operation

Check if an operation to be created is valid

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.OperatorConfiguration(
    dbt=shared.OperatorDbt(
        dbt_arguments='ut',
        docker_image='quaerat',
        git_repo_branch='architecto',
        git_repo_url='praesentium',
    ),
    normalization=shared.OperatorNormalization(
        option=shared.OperatorNormalizationOptionEnum.BASIC,
    ),
    operator_type=shared.OperatorTypeEnum.WEBHOOK,
    webhook=shared.OperatorWebhook(
        dbt_cloud=shared.OperatorWebhookDbtCloud(
            account_id=221781,
            job_id=709051,
        ),
        execution_body='libero',
        execution_url='iste',
        webhook_config_id='1c8d975e-0e84-419d-8f84-f144f3e07edc',
        webhook_type=shared.OperatorWebhookWebhookTypeEnum.DBT_CLOUD,
    ),
)

res = s.operation.check_operation(req)

if res.check_operation_read is not None:
    # handle response
```

## create_operation

Create an operation to be applied as part of a connection pipeline

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.OperationCreate(
    name='Jay Pagac',
    operator_configuration=shared.OperatorConfiguration(
        dbt=shared.OperatorDbt(
            dbt_arguments='reiciendis',
            docker_image='sequi',
            git_repo_branch='porro',
            git_repo_url='laborum',
        ),
        normalization=shared.OperatorNormalization(
            option=shared.OperatorNormalizationOptionEnum.BASIC,
        ),
        operator_type=shared.OperatorTypeEnum.WEBHOOK,
        webhook=shared.OperatorWebhook(
            dbt_cloud=shared.OperatorWebhookDbtCloud(
                account_id=842974,
                job_id=607624,
            ),
            execution_body='aut',
            execution_url='ipsam',
            webhook_config_id='a972e056-7282-427b-ad30-9470bf7a4fa8',
            webhook_type=shared.OperatorWebhookWebhookTypeEnum.DBT_CLOUD,
        ),
    ),
    workspace_id='7cf535a6-fae5-44eb-b60c-321f023b75d2',
)

res = s.operation.create_operation(req)

if res.operation_read is not None:
    # handle response
```

## delete_operation

Delete an operation

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.OperationIDRequestBody(
    operation_id='367fe1a0-cc8d-4f79-b0a3-96d90c364b7c',
)

res = s.operation.delete_operation(req)

if res.status_code == 200:
    # handle response
```

## get_operation

Returns an operation

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.OperationIDRequestBody(
    operation_id='15dfbace-188b-41c4-ae2c-8c6ce611feeb',
)

res = s.operation.get_operation(req)

if res.operation_read is not None:
    # handle response
```

## list_operations_for_connection

List operations for connection.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.ConnectionIDRequestBody(
    connection_id='1c7cbdb6-eec7-4437-8ba2-5317747dc915',
)

res = s.operation.list_operations_for_connection(req)

if res.operation_read_list is not None:
    # handle response
```

## update_operation

Update an operation

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.OperationUpdate(
    name='Gilberto Corkery',
    operation_id='f5dd6723-dc0f-45ae-af3a-6b7008787561',
    operator_configuration=shared.OperatorConfiguration(
        dbt=shared.OperatorDbt(
            dbt_arguments='quaerat',
            docker_image='amet',
            git_repo_branch='sapiente',
            git_repo_url='corporis',
        ),
        normalization=shared.OperatorNormalization(
            option=shared.OperatorNormalizationOptionEnum.BASIC,
        ),
        operator_type=shared.OperatorTypeEnum.DBT,
        webhook=shared.OperatorWebhook(
            dbt_cloud=shared.OperatorWebhookDbtCloud(
                account_id=435142,
                job_id=787629,
            ),
            execution_body='provident',
            execution_url='laudantium',
            webhook_config_id='b5555408-0d40-4bca-8c6c-bd6b5f3ec909',
            webhook_type=shared.OperatorWebhookWebhookTypeEnum.DBT_CLOUD,
        ),
    ),
)

res = s.operation.update_operation(req)

if res.operation_read is not None:
    # handle response
```
