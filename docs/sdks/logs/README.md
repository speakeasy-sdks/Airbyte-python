# logs

### Available Operations

* [get_logs](#get_logs) - Get logs

## get_logs

Get logs

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.LogsRequestBody(
    log_type=shared.LogType.SCHEDULER,
)

res = s.logs.get_logs(req)

if res.get_logs_200_text_plain_binary_string is not None:
    # handle response
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [shared.LogsRequestBody](../../models/shared/logsrequestbody.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.GetLogsResponse](../../models/operations/getlogsresponse.md)**

