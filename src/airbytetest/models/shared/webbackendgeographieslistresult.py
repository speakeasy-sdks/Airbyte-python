"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import geography_enum as shared_geography_enum
from airbytetest import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class WebBackendGeographiesListResult:
    r"""Successful operation"""
    
    geographies: list[shared_geography_enum.GeographyEnum] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('geographies') }})
    