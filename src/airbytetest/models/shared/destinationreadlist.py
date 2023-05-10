"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import destinationread as shared_destinationread
from airbytetest import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationReadList:
    r"""Successful operation"""
    
    destinations: list[shared_destinationread.DestinationRead] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinations') }})
    