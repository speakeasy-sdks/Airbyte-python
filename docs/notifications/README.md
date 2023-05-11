# notifications

### Available Operations

* [try_notification_config](#try_notification_config) - Try sending a notifications

## try_notification_config

Try sending a notifications

### Example Usage

```python
import airbyte_oss
from airbyte_oss.models import shared

s = airbyte_oss.AirbyteOss()

req = shared.Notification(
    customerio_configuration={
        "explicabo": 'impedit',
        "aliquid": 'quis',
    },
    notification_type=shared.NotificationTypeEnum.CUSTOMERIO,
    send_on_failure=False,
    send_on_success=False,
    slack_configuration=shared.SlackNotificationConfiguration(
        webhook='ipsum',
    ),
)

res = s.notifications.try_notification_config(req)

if res.notification_read is not None:
    # handle response
```
