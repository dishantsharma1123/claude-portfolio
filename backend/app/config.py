import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    OPENROUTER_API_KEY: str = os.getenv("OPENROUTER_API_KEY")
    CLERK_JWT_ISSUER_URL: str = os.getenv("CLERK_JWT_ISSUER_URL")

settings = Settings()