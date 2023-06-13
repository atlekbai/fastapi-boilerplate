from fastapi import Depends

from app.utils import AppModel

from ..service import Service, get_service
from . import router


class GetShanyrakRespone(AppModel):
    user_id: str
    type: str
    price: str
    address: str
    area: str
    rooms_count: str
    description: str


@router.get("/{id}", response_model=GetShanyrakRespone)
def get_shanyrak(
    id: str,
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    shanyrak = svc.repository.get_shanyrak_by_id(id)

    return shanyrak
