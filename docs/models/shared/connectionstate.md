# ConnectionState

Contains the state for a connection. The stateType field identifies what type of state it is. Only the field corresponding to that type will be set, the rest will be null. If stateType=not_set, then none of the fields will be set.


## Fields

| Field                                                             | Type                                                              | Required                                                          | Description                                                       |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `connection_id`                                                   | *str*                                                             | :heavy_check_mark:                                                | N/A                                                               |
| `global_state`                                                    | [Optional[GlobalState]](../../models/shared/globalstate.md)       | :heavy_minus_sign:                                                | N/A                                                               |
| `state`                                                           | [Optional[StateBlob]](../../models/shared/stateblob.md)           | :heavy_minus_sign:                                                | N/A                                                               |
| `state_type`                                                      | [ConnectionStateType](../../models/shared/connectionstatetype.md) | :heavy_check_mark:                                                | N/A                                                               |
| `stream_state`                                                    | list[[StreamState](../../models/shared/streamstate.md)]           | :heavy_minus_sign:                                                | N/A                                                               |