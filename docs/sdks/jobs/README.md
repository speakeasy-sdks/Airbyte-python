# jobs

### Available Operations

* [cancel_job](#cancel_job) - Cancels a job
* [get_attempt_normalization_statuses_for_job](#get_attempt_normalization_statuses_for_job) - Get normalization status to determine if we can bypass normalization phase
* [get_job_debug_info](#get_job_debug_info) - Gets all information needed to debug this job
* [get_job_info](#get_job_info) - Get information about a job
* [get_job_info_light](#get_job_info_light) - Get information about a job excluding attempt info and logs
* [get_last_replication_job](#get_last_replication_job)
* [list_jobs_for](#list_jobs_for) - Returns recent jobs for a connection. Jobs are returned in descending order by createdAt.

## cancel_job

Cancels a job

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.JobIDRequestBody(
    id=556133,
)

res = s.jobs.cancel_job(req)

if res.job_info_read is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.JobIDRequestBody](../../models/shared/jobidrequestbody.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.CancelJobResponse](../../models/operations/canceljobresponse.md)**


## get_attempt_normalization_statuses_for_job

Get normalization status to determine if we can bypass normalization phase

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.JobIDRequestBody(
    id=811259,
)

res = s.jobs.get_attempt_normalization_statuses_for_job(req)

if res.attempt_normalization_status_read_list is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.JobIDRequestBody](../../models/shared/jobidrequestbody.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.GetAttemptNormalizationStatusesForJobResponse](../../models/operations/getattemptnormalizationstatusesforjobresponse.md)**


## get_job_debug_info

Gets all information needed to debug this job

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.JobIDRequestBody(
    id=318028,
)

res = s.jobs.get_job_debug_info(req)

if res.job_debug_info_read is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.JobIDRequestBody](../../models/shared/jobidrequestbody.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.GetJobDebugInfoResponse](../../models/operations/getjobdebuginforesponse.md)**


## get_job_info

Get information about a job

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.JobIDRequestBody(
    id=286453,
)

res = s.jobs.get_job_info(req)

if res.job_info_read is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.JobIDRequestBody](../../models/shared/jobidrequestbody.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.GetJobInfoResponse](../../models/operations/getjobinforesponse.md)**


## get_job_info_light

Get information about a job excluding attempt info and logs

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.JobIDRequestBody(
    id=958068,
)

res = s.jobs.get_job_info_light(req)

if res.job_info_light_read is not None:
    # handle response
```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `request`                                                          | [shared.JobIDRequestBody](../../models/shared/jobidrequestbody.md) | :heavy_check_mark:                                                 | The request object to use for the request.                         |


### Response

**[operations.GetJobInfoLightResponse](../../models/operations/getjobinfolightresponse.md)**


## get_last_replication_job

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.ConnectionIDRequestBody(
    connection_id='efa9c95f-2eac-4556-9d30-7cfee81206e2',
)

res = s.jobs.get_last_replication_job(req)

if res.job_optional_read is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [shared.ConnectionIDRequestBody](../../models/shared/connectionidrequestbody.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetLastReplicationJobResponse](../../models/operations/getlastreplicationjobresponse.md)**


## list_jobs_for

Returns recent jobs for a connection. Jobs are returned in descending order by createdAt.

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.JobListRequestBody(
    config_id='deleniti',
    config_types=[
        shared.JobConfigType.CHECK_CONNECTION_DESTINATION,
    ],
    including_job_id=963913,
    pagination=shared.Pagination(
        page_size=673653,
        row_offset=303421,
    ),
)

res = s.jobs.list_jobs_for(req)

if res.job_read_list is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [shared.JobListRequestBody](../../models/shared/joblistrequestbody.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.ListJobsForResponse](../../models/operations/listjobsforresponse.md)**

