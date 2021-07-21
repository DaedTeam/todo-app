from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID

from bson import ObjectId

from app.api.v1.schemas.base import BaseEnhancedModel
from app.api.v1.schemas.task import TaskMongoSchema


class EIssueStatus(str, Enum):
    backlog = "backlog"
    select_for_development = "s_f_d"
    in_process = "in_process"
    done = "done"


class IssueBase(BaseEnhancedModel):
    name: str
    create_date: datetime
    update_date: datetime
    color: str
    status: EIssueStatus


class IssueCreate(IssueBase):
    user_id: str


class IssueUpdate(IssueBase):
    pass


class IssueSchema(IssueBase):
    id: int


class IssueMongoSchema(IssueBase):
    _id: ObjectId
    object_id: UUID
    user_id: str
    tasks: List[TaskMongoSchema] = []
