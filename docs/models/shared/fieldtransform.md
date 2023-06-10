# FieldTransform

Describes the difference between two Streams.


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `add_field`                                                                       | [Optional[FieldAdd]](../../models/shared/fieldadd.md)                             | :heavy_minus_sign:                                                                | N/A                                                                               |
| `breaking`                                                                        | *bool*                                                                            | :heavy_check_mark:                                                                | N/A                                                                               |
| `field_name`                                                                      | list[*str*]                                                                       | :heavy_check_mark:                                                                | A field name is a list of strings that form the path to the field.                |
| `remove_field`                                                                    | [Optional[FieldRemove]](../../models/shared/fieldremove.md)                       | :heavy_minus_sign:                                                                | N/A                                                                               |
| `transform_type`                                                                  | [FieldTransformTransformType](../../models/shared/fieldtransformtransformtype.md) | :heavy_check_mark:                                                                | N/A                                                                               |
| `update_field_schema`                                                             | [Optional[FieldSchemaUpdate]](../../models/shared/fieldschemaupdate.md)           | :heavy_minus_sign:                                                                | N/A                                                                               |