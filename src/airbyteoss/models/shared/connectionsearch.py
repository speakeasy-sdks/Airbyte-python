"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import connectionschedule as shared_connectionschedule
from ..shared import connectionscheduledata as shared_connectionscheduledata
from ..shared import connectionscheduletype_enum as shared_connectionscheduletype_enum
from ..shared import connectionstatus_enum as shared_connectionstatus_enum
from ..shared import destinationsearch as shared_destinationsearch
from ..shared import namespacedefinitiontype_enum as shared_namespacedefinitiontype_enum
from ..shared import sourcesearch as shared_sourcesearch
from airbyteoss import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectionSearch:
    
    connection_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connectionId'), 'exclude': lambda f: f is None }})
    destination: Optional[shared_destinationsearch.DestinationSearch] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destination'), 'exclude': lambda f: f is None }})
    destination_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationId'), 'exclude': lambda f: f is None }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    namespace_definition: Optional[shared_namespacedefinitiontype_enum.NamespaceDefinitionTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceDefinition'), 'exclude': lambda f: f is None }})
    r"""Method used for computing final namespace in destination"""
    namespace_format: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespaceFormat'), 'exclude': lambda f: f is None }})
    r"""Used when namespaceDefinition is 'customformat'. If blank then behaves like namespaceDefinition = 'destination'. If \\"${SOURCE_NAMESPACE}\\" then behaves like namespaceDefinition = 'source'."""
    prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prefix'), 'exclude': lambda f: f is None }})
    r"""Prefix that will be prepended to the name of each stream when it is written to the destination."""
    schedule: Optional[shared_connectionschedule.ConnectionSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schedule'), 'exclude': lambda f: f is None }})
    r"""if null, then no schedule is set."""
    schedule_data: Optional[shared_connectionscheduledata.ConnectionScheduleData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduleData'), 'exclude': lambda f: f is None }})
    r"""schedule for when the the connection should run, per the schedule type"""
    schedule_type: Optional[shared_connectionscheduletype_enum.ConnectionScheduleTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduleType'), 'exclude': lambda f: f is None }})
    r"""determine how the schedule data should be interpreted"""
    source: Optional[shared_sourcesearch.SourceSearch] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceId'), 'exclude': lambda f: f is None }})
    status: Optional[shared_connectionstatus_enum.ConnectionStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""Active means that data is flowing through the connection. Inactive means it is not. Deprecated means the connection is off and cannot be re-activated. the schema field describes the elements of the schema that will be synced."""
    