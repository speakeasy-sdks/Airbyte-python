# logs

### Available Operations

* [get_logs](#get_logs) - Get logs

## get_logs

Get logs

### Example Usage

```python
import airbyte_test
from airbyte_test.models import shared

s = airbyte_test.AirbyteTest()

req = shared.LogsRequestBody(
    log_type=shared.LogTypeEnum.SERVER,
)

res = s.logs.get_logs(req)

if res.get_logs_200_text_plain_binary_string is not None:
    # handle response
```
