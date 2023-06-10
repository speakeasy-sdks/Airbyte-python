# openapi

### Available Operations

* [get_open_api_spec](#get_open_api_spec) - Returns the openapi specification

## get_open_api_spec

Returns the openapi specification

### Example Usage

```python
import airbyte


s = airbyte.Airbyte()


res = s.openapi.get_open_api_spec()

if res.get_open_api_spec_200_text_plain_binary_string is not None:
    # handle response
```


### Response

**[operations.GetOpenAPISpecResponse](../../models/operations/getopenapispecresponse.md)**

