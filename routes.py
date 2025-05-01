from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from todo.database.base import get_db_session
from fastapi.templating import Jinja2Templates
from pathlib import Path
from todo.config import settings
from todo.models import Note

router = APIRouter()
templates = Jinja2Templates(directory=Path(__file__).parent.parent / "todo" / "templates")

@router.get("/")
async def home(request: Request, db_session : Session = Depends(get_db_session)):
    app_name = settings.app_name

    notes = db_session.query(Note).all()

    return templates.TemplateResponse('todo/index.html', {"request": request, "app_name": app_name, "notes" : notes})

@router.post("/add")
async def add(title : str = Form, )