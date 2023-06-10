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
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.OperatorConfiguration(
    dbt=shared.OperatorDbt(
        dbt_arguments='impedit',
        docker_image='eius',
        git_repo_branch='voluptatum',
        git_repo_url='ipsa',
    ),
    normalization=shared.OperatorNormalization(
        option=shared.OperatorNormalizationOption.BASIC,
    ),
    operator_type=shared.OperatorType.WEBHOOK,
    webhook=shared.OperatorWebhook(
        dbt_cloud=shared.OperatorWebhookDbtCloud(
            account_id=209860,
            job_id=999854,
        ),
        execution_body='aspernatur',
        execution_url='inventore',
        webhook_config_id='32af0310-2d51-44f4-8c6f-18bf9621a6a4',
        webhook_type=shared.OperatorWebhookWebhookType.DBT_CLOUD,
    ),
)

res = s.operation.check_operation(req)

if res.check_operation_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [shared.OperatorConfiguration](../../models/shared/operatorconfiguration.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CheckOperationResponse](../../models/operations/checkoperationresponse.md)**


## create_operation

Create an operation to be applied as part of a connection pipeline

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.OperationCreate(
    name='Julio Koch',
    operator_configuration=shared.OperatorConfiguration(
        dbt=shared.OperatorDbt(
            dbt_arguments='esse',
            docker_image='eveniet',
            git_repo_branch='earum',
            git_repo_url='velit',
        ),
        normalization=shared.OperatorNormalization(
            option=shared.OperatorNormalizationOption.BASIC,
        ),
        operator_type=shared.OperatorType.WEBHOOK,
        webhook=shared.OperatorWebhook(
            dbt_cloud=shared.OperatorWebhookDbtCloud(
                account_id=263346,
                job_id=701978,
            ),
            execution_body='itaque',
            execution_url='dignissimos',
            webhook_config_id='52c65b34-418e-43bb-91c8-d975e0e8419d',
            webhook_type=shared.OperatorWebhookWebhookType.DBT_CLOUD,
        ),
    ),
    workspace_id='8f84f144-f3e0-47ed-8c4a-a5f3cabd905a',
)

res = s.operation.create_operation(req)

if res.operation_read is not None:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [shared.OperationCreate](../../models/shared/operationcreate.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.CreateOperationResponse](../../models/operations/createoperationresponse.md)**


## delete_operation

Delete an operation

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.OperationIDRequestBody(
    operation_id='972e0567-2822-47b2-9309-470bf7a4fa87',
)

res = s.operation.delete_operation(req)

if res.status_code == 200:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.OperationIDRequestBody](../../models/shared/operationidrequestbody.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.DeleteOperationResponse](../../models/operations/deleteoperationresponse.md)**


## get_operation

Returns an operation

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.OperationIDRequestBody(
    operation_id='cf535a6f-ae54-4ebf-a0c3-21f023b75d23',
)

res = s.operation.get_operation(req)

if res.operation_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [shared.OperationIDRequestBody](../../models/shared/operationidrequestbody.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetOperationResponse](../../models/operations/getoperationresponse.md)**


## list_operations_for_connection

List operations for connection.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.ConnectionIDRequestBody(
    connection_id='67fe1a0c-c8df-479f-8a39-6d90c364b7c1',
)

res = s.operation.list_operations_for_connection(req)

if res.operation_read_list is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.ConnectionIDRequestBody](../../models/shared/connectionidrequestbody.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListOperationsForConnectionResponse](../../models/operations/listoperationsforconnectionresponse.md)**


## update_operation

Update an operation

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.OperationUpdate(
    name='Betsy Wuckert',
    operation_id='ce188b1c-4ee2-4c8c-ace6-11feeb1c7cbd',
    operator_configuration=shared.OperatorConfiguration(
        dbt=shared.OperatorDbt(
            dbt_arguments='cum',
            docker_image='suscipit',
            git_repo_branch='saepe',
            git_repo_url='earum',
        ),
        normalization=shared.OperatorNormalization(
            option=shared.OperatorNormalizationOption.BASIC,
        ),
        operator_type=shared.OperatorType.WEBHOOK,
        webhook=shared.OperatorWebhook(
            dbt_cloud=shared.OperatorWebhookDbtCloud(
                account_id=469588,
                job_id=310930,
            ),
            execution_body='ipsum',
            execution_url='ducimus',
            webhook_config_id='8ba25317-747d-4c91-9ad2-caf5dd6723dc',
            webhook_type=shared.OperatorWebhookWebhookType.DBT_CLOUD,
        ),
    ),
)

res = s.operation.update_operation(req)

if res.operation_read is not None:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [shared.OperationUpdate](../../models/shared/operationupdate.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.UpdateOperationResponse](../../models/operations/updateoperationresponse.md)**

