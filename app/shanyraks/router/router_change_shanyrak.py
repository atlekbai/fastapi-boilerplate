from fastapi import Depends, Response
from pydantic import BaseModel

from ..service import Service, get_service
from . import router
from typing import Optional


class ChangeShanyrakData(BaseModel):
    type: Optional[str] = None
    price: Optional[str] = None
    address: Optional[str] = None
    area: Optional[str] = None
    rooms_count: Optional[str] = None
    description: Optional[str] = None


@router.patch("/{id}")
def change_shanyrak(
    id: str,
    input: ChangeShanyrakData,
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    svc.repository.change_shanyrak(id, input)
    return Response(status_code=200)
