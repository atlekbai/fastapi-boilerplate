from datetime import datetime, timedelta

from jose import JWTError, jwt
from pydantic import BaseModel, Field


class JWTData(BaseModel):
    user_id: str = Field(alias="sub")


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
            "sub": str(user["_id"]),
            "exp": datetime.utcnow() + expires_delta,
        }

        return jwt.encode(jwt_data, self.secret, algorithm=self.algorithm)

    def parse_jwt_user_data(self, token: str) -> JWTData | None:
        if not token:
            return None

        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.algorithm])
        except JWTError:
            raise InvalidToken()

        return JWTData(**payload)


class AuthorizationFailed(Exception):
    pass


class InvalidToken(Exception):
    pass
