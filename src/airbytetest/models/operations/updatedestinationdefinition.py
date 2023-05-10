"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import destinationdefinitionread as shared_destinationdefinitionread
from ..shared import invalidinputexceptioninfo as shared_invalidinputexceptioninfo
from ..shared import notfoundknownexceptioninfo as shared_notfoundknownexceptioninfo
from typing import Optional


@dataclasses.dataclass
class UpdateDestinationDefinitionResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    destination_definition_read: Optional[shared_destinationdefinitionread.DestinationDefinitionRead] = dataclasses.field(default=None)
    r"""Successful operation"""
    invalid_input_exception_info: Optional[shared_invalidinputexceptioninfo.InvalidInputExceptionInfo] = dataclasses.field(default=None)
    r"""Input failed validation"""
    not_found_known_exception_info: Optional[shared_notfoundknownexceptioninfo.NotFoundKnownExceptionInfo] = dataclasses.field(default=None)
    r"""Object with given id was not found."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    