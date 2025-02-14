from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Checks if password matches hash
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)