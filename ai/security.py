import os
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
import requests

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

class TokenData(BaseModel):
    username: str = None

async def get_current_user(token: str = Depends(oauth2_scheme)):
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
