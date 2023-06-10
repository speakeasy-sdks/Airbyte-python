# notifications

### Available Operations

* [try_notification_config](#try_notification_config) - Try sending a notifications

## try_notification_config

Try sending a notifications

### Example Usage

```python
import airbyte
from airbyte.models import shared

s = airbyte.Airbyte()

req = shared.Notification(
    customerio_configuration=shared.CustomerioNotificationConfiguration(),
    notification_type=shared.NotificationType.SLACK,
    send_on_failure=False,
    send_on_success=False,
    slack_configuration=shared.SlackNotificationConfiguration(
        webhook='sunt',
    ),
)

res = s.notifications.try_notification_config(req)

if res.notification_read is not None:
    # handle response
```

### Parameters

| Parameter                                                  | Type                                                       | Required                                                   | Description                                                |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `request`                                                  | [shared.Notification](../../models/shared/notification.md) | :heavy_check_mark:                                         | The request object to use for the request.                 |


### Response

**[operations.TryNotificationConfigResponse](../../models/operations/trynotificationconfigresponse.md)**

