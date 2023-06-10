# InvalidInputExceptionInfo

Input failed validation


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `exception_class_name`                                                    | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | N/A                                                                       |
| `exception_stack`                                                         | list[*str*]                                                               | :heavy_minus_sign:                                                        | N/A                                                                       |
| `message`                                                                 | *str*                                                                     | :heavy_check_mark:                                                        | N/A                                                                       |
| `validation_errors`                                                       | list[[InvalidInputProperty](../../models/shared/invalidinputproperty.md)] | :heavy_check_mark:                                                        | N/A                                                                       |