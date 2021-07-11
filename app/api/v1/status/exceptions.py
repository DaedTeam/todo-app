from typing import Dict, List

from fastapi import HTTPException
from starlette import status

from app.api.v1.status.messages import MESSAGE_STATUS


class ExceptionHandle(HTTPException):
    def __init__(
            self,
            errors: List[Dict[str, str]] = None,
            status_code: int = status.HTTP_400_BAD_REQUEST,
            header=None
    ):
        super().__init__(status_code=status_code, detail=errors, headers=header)
        self.errors: List[Dict] = errors

    def get_message_detail(self):
        result = []
        if self.errors:
            for temp in self.errors:
                if not temp.get("detail"):
                    temp.update({"detail": MESSAGE_STATUS.get(temp.get("msg"))})
                    result.append(temp)
                else:
                    result.append(temp)
        return result
