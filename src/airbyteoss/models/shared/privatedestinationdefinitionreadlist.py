"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import privatedestinationdefinitionread as shared_privatedestinationdefinitionread
from airbyteoss import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PrivateDestinationDefinitionReadList:
    r"""Successful operation"""
    
    destination_definitions: list[shared_privatedestinationdefinitionread.PrivateDestinationDefinitionRead] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationDefinitions') }})
    