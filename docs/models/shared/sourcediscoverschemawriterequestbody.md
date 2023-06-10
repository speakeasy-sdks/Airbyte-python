# SourceDiscoverSchemaWriteRequestBody

to write this requested object to database.


## Fields

| Field                                                   | Type                                                    | Required                                                | Description                                             |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| `catalog`                                               | [AirbyteCatalog](../../models/shared/airbytecatalog.md) | :heavy_check_mark:                                      | describes the available schema (catalog).               |
| `configuration_hash`                                    | *Optional[str]*                                         | :heavy_minus_sign:                                      | N/A                                                     |
| `connector_version`                                     | *Optional[str]*                                         | :heavy_minus_sign:                                      | N/A                                                     |
| `source_id`                                             | *Optional[str]*                                         | :heavy_minus_sign:                                      | N/A                                                     |