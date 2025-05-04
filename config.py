import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent.parent / "todo" / ".env")

class Settings:
    app_name: str = os.getenv('NAME_APP')
    db_url: str = os.getenv("SQLALCHEMY_DB_URI")

settings = Settings()
