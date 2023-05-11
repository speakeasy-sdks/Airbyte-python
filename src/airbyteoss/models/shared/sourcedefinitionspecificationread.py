"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import advancedauth as shared_advancedauth
from ..shared import sourceauthspecification as shared_sourceauthspecification
from ..shared import synchronousjobread as shared_synchronousjobread
from airbyteoss import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceDefinitionSpecificationRead:
    r"""Successful operation"""
    
    job_info: shared_synchronousjobread.SynchronousJobRead = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jobInfo') }})
    source_definition_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceDefinitionId') }})
    advanced_auth: Optional[shared_advancedauth.AdvancedAuth] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('advancedAuth'), 'exclude': lambda f: f is None }})
    auth_specification: Optional[shared_sourceauthspecification.SourceAuthSpecification] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authSpecification'), 'exclude': lambda f: f is None }})
    connection_specification: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionSpecification'), 'exclude': lambda f: f is None }})
    r"""The specification for what values are required to configure the sourceDefinition."""
    documentation_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('documentationUrl'), 'exclude': lambda f: f is None }})
    