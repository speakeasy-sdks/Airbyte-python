# AirbyteStreamAndConfiguration

each stream is split in two parts; the immutable schema from source and mutable configuration for destination


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `config`                                                                                  | [Optional[AirbyteStreamConfiguration]](../../models/shared/airbytestreamconfiguration.md) | :heavy_minus_sign:                                                                        | the mutable part of the stream to configure the destination                               |
| `stream`                                                                                  | [Optional[AirbyteStream]](../../models/shared/airbytestream.md)                           | :heavy_minus_sign:                                                                        | the immutable schema defined by the source                                                |