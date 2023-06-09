from datetime import datetime, timedelta

from jose import JWTError, jwt
from pydantic import BaseModel, Field


class JWTData(BaseModel):
    user_id: int = Field(alias="sub")
    is_admin: bool


class JwtService:
    def __init__(
        self,
        algorithm: str,
        secret: str,
        expiration: timedelta,
    ) -> None:
        self.algorithm = algorithm
        self.secret = secret
        self.expiration = expiration

    def create_access_token(
        self,
        user: dict,
    ) -> str:
        expires_delta = timedelta(minutes=self.expiration)

        jwt_data = {
            "sub": str(user["id"]),
            "exp": datetime.utcnow() + expires_delta,
            "is_admin": user["is_admin"],
        }

        return jwt.encode(jwt_data, self.secret, algorithm=self.algorithm)

    def parse_jwt_user_data(self, token: str) -> JWTData | None:
        if not token:
            return None

        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
            print(token)
            print(payload)
        except JWTError:
            raise InvalidToken()

        return JWTData(**payload)

    def parse_jwt_admin_data(self, token: str) -> JWTData | None:
        token = self.parse_jwt_user_data(token)
        if token is None:
            return None

        if not token.is_admin:
            raise AuthorizationFailed()

        return token

    def validate_admin_access(self, token: str) -> None:
        token = self.parse_jwt_user_data(token)
        if token and token.is_admin:
            return

        raise AuthorizationFailed()


class AuthorizationFailed(Exception):
    pass


class InvalidToken(Exception):
    pass
