from todo.database.base import Base, engine
from todo.models import Note

Base.metadata.create_all(bind=engine)