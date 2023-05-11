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
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.JobIDRequestBody(
    id=685467,
)

res = s.jobs.cancel_job(req)

if res.job_info_read is not None:
    # handle response
```

## get_attempt_normalization_statuses_for_job

Get normalization status to determine if we can bypass normalization phase

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.JobIDRequestBody(
    id=943103,
)

res = s.jobs.get_attempt_normalization_statuses_for_job(req)

if res.attempt_normalization_status_read_list is not None:
    # handle response
```

## get_job_debug_info

Gets all information needed to debug this job

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.JobIDRequestBody(
    id=49499,
)

res = s.jobs.get_job_debug_info(req)

if res.job_debug_info_read is not None:
    # handle response
```

## get_job_info

Get information about a job

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.JobIDRequestBody(
    id=211301,
)

res = s.jobs.get_job_info(req)

if res.job_info_read is not None:
    # handle response
```

## get_job_info_light

Get information about a job excluding attempt info and logs

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.JobIDRequestBody(
    id=101854,
)

res = s.jobs.get_job_info_light(req)

if res.job_info_light_read is not None:
    # handle response
```

## get_last_replication_job

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.ConnectionIDRequestBody(
    connection_id='02d514f4-cc6f-418b-b962-1a6a4f77a87e',
)

res = s.jobs.get_last_replication_job(req)

if res.job_optional_read is not None:
    # handle response
```

## list_jobs_for

Returns recent jobs for a connection. Jobs are returned in descending order by createdAt.

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.JobListRequestBody(
    config_id='earum',
    config_types=[
        shared.JobConfigTypeEnum.RESET_CONNECTION,
    ],
    including_job_id=263346,
    pagination=shared.Pagination(
        page_size=701978,
        row_offset=930111,
    ),
)

res = s.jobs.list_jobs_for(req)

if res.job_read_list is not None:
    # handle response
```
