from datetime import datetime
from enum import Enum
from typing import Any, Optional, Type, Union

from pydantic import BaseModel


class BaseEnhancedModel(BaseModel):

    @classmethod
    def construct(cls: Type['Model'], _fields_set: Optional['SetStr'] = None, **values: Any) -> 'Model':
        values["object_id"] = str(values.get("_id", None))
        return super().construct(_fields_set=_fields_set, **values)

    def dict(
            self,
            *,
            include: Union['AbstractSetIntStr', 'MappingIntStrAny'] = None,
            exclude: Union['AbstractSetIntStr', 'MappingIntStrAny'] = None,
            by_alias: bool = False,
            skip_defaults: bool = None,
            exclude_unset: bool = False,
            exclude_defaults: bool = False,
            exclude_none: bool = False,
    ) -> 'DictStrAny':
        processing_dict = super().dict()
        for key, value in processing_dict.items():
            if isinstance(value, Enum):
                processing_dict[key] = value.value
            if isinstance(value, datetime):
                value: datetime
                processing_dict[key] = value.replace(tzinfo=None)
        return processing_dict

    class Config:
        orm_mode = True
