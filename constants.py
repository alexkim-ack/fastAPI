ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Database shouldn't be stored in this service, but for simplicity and transparency, we're committing it
FAKE_USERS_DB = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    },
}

# This should not be committed, but for simplicity and transparency, we're committing it
SECRET_KEY = "405a2570f9207f8c765149f3e2709d7076caaeecffa528ec668ea4fc8eb6e884"
