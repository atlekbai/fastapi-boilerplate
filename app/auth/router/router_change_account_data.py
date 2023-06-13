from fastapi import Depends, Response
from pydantic import BaseModel

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from . import router
from .dependencies import parse_jwt_user_data
from typing import Optional


class ChangeAccountDataRequest(BaseModel):
    phone: Optional[str] = None
    name: Optional[str] = None
    city: Optional[str] = None


@router.patch("/users/me")
def change_account_data(
    input: ChangeAccountDataRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    svc.repository.change_user(jwt_data.user_id, input)
    return Response(status_code=200)
