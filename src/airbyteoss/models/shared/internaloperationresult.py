"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyteoss import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InternalOperationResult:
    r"""Successful Operation"""
    
    succeeded: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('succeeded') }})
    