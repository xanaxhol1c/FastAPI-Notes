from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse
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

    notes = db_session.query(Note).order_by(Note.data_created.desc()).all()
    return templates.TemplateResponse('todo/index.html', {"request": request, "app_name": app_name, "notes" : notes})

@router.post("/add")
async def add(title : str = Form(...), text : str = Form(...),  db_session : Session = Depends(get_db_session)):
    new_note = Note(title=title, text=text)
    db_session.add(new_note)
    db_session.commit()

    url = router.url_path_for('home')
    return RedirectResponse(url=url, status_code=303)

@router.get('/update/{note_id}')
async def update(note_id : int, db_session : Session = Depends(get_db_session)):
    note = db_session.query(Note).filter(Note.id == note_id).first()
    if note.is_complete == False:
        note.is_complete = True
    db_session.commit()

    url = router.url_path_for('home')
    return RedirectResponse(url=url, status_code=302)

@router.get('/delete/{note_id}')
async def delete(note_id : int, db_session : Session = Depends(get_db_session)):
    note = db_session.query(Note).filter(Note.id == note_id).first()
    db_session.delete(note)
    db_session.commit()

    url = router.url_path_for('home')
    return RedirectResponse(url=url, status_code=302)