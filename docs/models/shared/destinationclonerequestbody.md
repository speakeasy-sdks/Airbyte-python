# DestinationCloneRequestBody

The values required to configure the destination. The schema for this should have an id of the existing destination along with the configuration you want to change in case.


## Fields

| Field                                                                                           | Type                                                                                            | Required                                                                                        | Description                                                                                     |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `destination_clone_id`                                                                          | *str*                                                                                           | :heavy_check_mark:                                                                              | N/A                                                                                             |
| `destination_configuration`                                                                     | [Optional[DestinationCloneConfiguration]](../../models/shared/destinationcloneconfiguration.md) | :heavy_minus_sign:                                                                              | N/A                                                                                             |