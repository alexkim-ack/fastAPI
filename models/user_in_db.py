from pydantic import BaseModel
from .user import User

class UserInDB(User):
    hashed_password: str