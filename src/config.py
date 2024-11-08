import os

DATABASE_NAME = os.getenv("DATABASE_NAME", "users.db")
SERVER_PORT = int(os.getenv("SERVER_PORT", 8000))