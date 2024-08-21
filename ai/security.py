import os
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

class TokenData(BaseModel):
    username: str = None

credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Retrieves the current user based on the provided token.

    Args:
        token (str): The JWT token.

    Returns:
        TokenData: The token data containing the username.

    Raises:
        HTTPException: If the token is invalid or the username is not found.
    """
    xsuaa_url = os.getenv('XSUAA_URL')
    try:
        payload = jwt.decode(token, xsuaa_url, algorithms=['RS256'])
        username: str = payload.get('user_name')
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    return token_data
