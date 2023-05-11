# health

## Overview

Healthchecks

### Available Operations

* [get_health_check](#get_health_check) - Health Check

## get_health_check

Health Check

### Example Usage

```python
import airbyte


s = airbyte.Airbyte()


res = s.health.get_health_check()

if res.health_check_read is not None:
    # handle response
```
