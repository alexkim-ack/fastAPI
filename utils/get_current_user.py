import jwt

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from typing import Annotated

from .get_user import get_user
from constants import ALGORITHM, FAKE_USERS_DB, SECRET_KEY
from models import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Gets user if valid JWT exists
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(FAKE_USERS_DB, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user