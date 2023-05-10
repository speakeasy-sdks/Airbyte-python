"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbytetest import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WebBackendWorkspaceStateResult:
    r"""Successful operation"""
    
    has_connections: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hasConnections') }})
    has_destinations: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hasDestinations') }})
    has_sources: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hasSources') }})
    