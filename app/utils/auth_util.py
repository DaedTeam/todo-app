from typing import Dict, Optional, Union

from fastapi import HTTPException
from starlette import status


class AuthUtil:
    @staticmethod
    def decode_token(authorization: Optional[str]) -> Union[str, Dict]:
        if not authorization:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        # TODO
        # return authorization[7:]
        return "1"
