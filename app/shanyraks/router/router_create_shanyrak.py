from fastapi import Depends

from app.auth.adapters.jwt_service import JWTData
from app.auth.router.dependencies import parse_jwt_user_data
from app.utils import AppModel
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from ..service import Service, get_service
from . import router


class CreateTweetRequest(AppModel):
    type: str
    price: str
    address: str
    area: str
    rooms_count: str
    description: str


@router.post("/", status_code=200)
def create_shanyrak(
    input: CreateTweetRequest,
    jwt_data: JWTData = Depends(parse_jwt_user_data),
    svc: Service = Depends(get_service),
) -> dict[str, str]:
    res = svc.repository.create_shanyrak(jwt_data.user_id, input)

    return JSONResponse(content=jsonable_encoder({"id": res}))
