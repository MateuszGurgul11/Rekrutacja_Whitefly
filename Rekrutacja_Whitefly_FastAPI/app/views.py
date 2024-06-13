from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from app.database import database
from app.models import entries
from sqlalchemy import insert, delete
from app.tasks import add_entry_async  

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    query = entries.select()
    results = await database.fetch_all(query)
    return templates.TemplateResponse("index.html", {"request": request, "entries": results})

@router.get("/add", response_class=HTMLResponse)
async def add_entry_form(request: Request):
    return templates.TemplateResponse("add_message.html", {"request": request})

@router.post("/add", response_class=HTMLResponse)
async def add_entry(request: Request, title: str = Form(...), content: str = Form(...)):
    query = insert(entries).values(title=title, content=content)
    await database.execute(query)
    return RedirectResponse(url="/", status_code=303)

@router.get("/add_async", response_class=HTMLResponse)
async def add_entry_async_form(request: Request):
    return templates.TemplateResponse("async_add_message.html", {"request": request})

@router.post("/add_async", response_class=HTMLResponse)
async def add_entry_async_view(request: Request, title: str = Form(...), content: str = Form(...)):
    add_entry_async.delay(title, content)
    return RedirectResponse(url="/", status_code=303)

@router.get("/delete/{entry_id}", response_class=HTMLResponse)
async def delete_entry(request: Request, entry_id: int):
    query = delete(entries).where(entries.c.id == entry_id)
    await database.execute(query)
    return RedirectResponse(url="/", status_code=303)