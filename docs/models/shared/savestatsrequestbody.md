# SaveStatsRequestBody


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `attempt_number`                                                      | *int*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `job_id`                                                              | *int*                                                                 | :heavy_check_mark:                                                    | N/A                                                                   |
| `stats`                                                               | [AttemptStats](../../models/shared/attemptstats.md)                   | :heavy_check_mark:                                                    | N/A                                                                   |
| `stream_stats`                                                        | list[[AttemptStreamStats](../../models/shared/attemptstreamstats.md)] | :heavy_minus_sign:                                                    | N/A                                                                   |