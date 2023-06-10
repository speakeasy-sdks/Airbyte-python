# StreamTransform


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `stream_descriptor`                                                                 | [StreamDescriptor](../../models/shared/streamdescriptor.md)                         | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `transform_type`                                                                    | [StreamTransformTransformType](../../models/shared/streamtransformtransformtype.md) | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `update_stream`                                                                     | list[[FieldTransform](../../models/shared/fieldtransform.md)]                       | :heavy_minus_sign:                                                                  | list of field transformations. order does not matter.                               |