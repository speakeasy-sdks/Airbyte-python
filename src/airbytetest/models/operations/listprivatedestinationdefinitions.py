"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import privatedestinationdefinitionreadlist as shared_privatedestinationdefinitionreadlist
from typing import Optional


@dataclasses.dataclass
class ListPrivateDestinationDefinitionsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    private_destination_definition_read_list: Optional[shared_privatedestinationdefinitionreadlist.PrivateDestinationDefinitionReadList] = dataclasses.field(default=None)
    r"""Successful operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    