"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import sourcedefinitioncreate as shared_sourcedefinitioncreate
from airbytetest import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomSourceDefinitionCreate:
    
    source_definition: shared_sourcedefinitioncreate.SourceDefinitionCreate = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceDefinition') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    