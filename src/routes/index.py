from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from pathlib import Path
from fastapi.templating import Jinja2Templates

index_routes = APIRouter(tags=['Index'])

templates = Jinja2Templates(directory="templates")

@index_routes.get('/', response_class=HTMLResponse)
def index(request: Request):
    context = {
        'request': request,
    }
    
    return templates.TemplateResponse('index.html',  context=context)

