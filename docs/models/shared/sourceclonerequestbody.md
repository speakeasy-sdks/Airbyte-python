# SourceCloneRequestBody

The values required to configure the source. The schema for this should have an id of the existing source along with the configuration you want to change in case.


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `source_clone_id`                                                                     | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `source_configuration`                                                                | [Optional[SourceCloneConfiguration]](../../models/shared/sourcecloneconfiguration.md) | :heavy_minus_sign:                                                                    | N/A                                                                                   |