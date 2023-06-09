from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from ..adapters.jwt_service import JWTData
from ..service import Service, get_service
from .errors import AuthenticationRequiredException, AuthorizationFailedException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/users/tokens", auto_error=False)


def parse_jwt_user_data_optional(
    token: str = Depends(oauth2_scheme),
    svc: Service = Depends(get_service),
) -> JWTData | None:
    return svc.jwt_svc.parse_jwt_user_data(token)


def parse_jwt_user_data(
    token: JWTData | None = Depends(parse_jwt_user_data_optional),
) -> JWTData:
    if not token:
        raise AuthenticationRequiredException

    return token


def parse_jwt_admin_data(
    token: JWTData = Depends(parse_jwt_user_data),
) -> JWTData:
    if not token.is_admin:
        raise AuthorizationFailedException

    return token


def validate_admin_access(
    _: JWTData = Depends(parse_jwt_admin_data),
) -> None:
    pass


# def valid_refresh_token(
#     refresh_token: str = Cookie(..., alias="refreshToken"),
# ) -> Record:
#     db_refresh_token = await repository.get_refresh_token(refresh_token)
#     if not db_refresh_token:
#         raise RefreshTokenNotValid()

#     if not _is_valid_refresh_token(db_refresh_token):
#         raise RefreshTokenNotValid()

#     return db_refresh_token


# def valid_refresh_token_user(
#     refresh_token: Record = Depends(valid_refresh_token),
# ) -> Record:
#     user = await repository.get_user_by_id(refresh_token["user_id"])
#     if not user:
#         raise RefreshTokenNotValid()

#     return user


# def _is_valid_refresh_token(db_refresh_token: Record) -> bool:
#     return datetime.utcnow() <= db_refresh_token["expires_at"]
