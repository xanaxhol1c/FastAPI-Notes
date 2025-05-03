import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from todo.config import settings

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'DB')
if not os.path.exists(db_path):
    os.makedirs(db_path)

Base = declarative_base()

engine = create_engine(settings.db_url, echo=True)

def get_db_session():
    db_session_local = SessionLocal()
    try:
       yield db_session_local
    finally:
        db_session_local.close()


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)