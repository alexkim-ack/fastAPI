from .get_user import get_user
from .verify_password import verify_password

# Checks if user is in database and has valid password
# Returns user if true else False
def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user