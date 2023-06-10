# SynchronousJobRead


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `config_id`                                           | *Optional[str]*                                       | :heavy_minus_sign:                                    | only present if a config id was provided.             |
| `config_type`                                         | [JobConfigType](../../models/shared/jobconfigtype.md) | :heavy_check_mark:                                    | N/A                                                   |
| `connector_configuration_updated`                     | *Optional[bool]*                                      | :heavy_minus_sign:                                    | N/A                                                   |
| `created_at`                                          | *int*                                                 | :heavy_check_mark:                                    | N/A                                                   |
| `ended_at`                                            | *int*                                                 | :heavy_check_mark:                                    | N/A                                                   |
| `id`                                                  | *str*                                                 | :heavy_check_mark:                                    | N/A                                                   |
| `logs`                                                | [Optional[LogRead]](../../models/shared/logread.md)   | :heavy_minus_sign:                                    | N/A                                                   |
| `succeeded`                                           | *bool*                                                | :heavy_check_mark:                                    | N/A                                                   |