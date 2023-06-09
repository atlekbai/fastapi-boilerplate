from fastapi import HTTPException, status

AuthenticationRequiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Authentication required",
)

AuthorizationFailedException = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Authorization failed. User has no access",
)

InvalidCredentialsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid credentials",
)
