from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from connection_database.database_connection import SessionLocal
from src.models.form import UserForm
from src.utils.images import get_images_path, save_image
from src.utils.tweeter_connection import get_user_tweets
from src.services.user import updated_or_create_user, get_user_by_id
from src.models.user import NewUser
from src import settings

user_routes = APIRouter(prefix='/user', tags=['User Data'])

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user_routes.get('/data', response_class=HTMLResponse)
def user_data(request: Request, db: Session = Depends(get_db)):
    
    if get_user_by_id(db):
    
        get_user = get_user_by_id(db)
        user = {
            'title': get_user.title,
            'name': get_user.name,
            'email': get_user.email,
            'phone': get_user.phone,
            'twitter_user': get_user.twitter_user,
            'description': get_user.text_description,
            'image_path': get_user.image
        }
        tweets = get_user_tweets(get_user.twitter_user)
    else: 
        user={}
        tweets = []
    context = {
        'request': request,
        'user': user,
        'tweets': tweets
    }
    
    return templates.TemplateResponse('user_data.html',  context=context)


@user_routes.get('/update', response_class=HTMLResponse)
def user_update(request: Request):
    
    context = {
        'request': request,
        'result': 'Cambio'
    }
    
    return templates.TemplateResponse('user_update.html',  context=context)


@user_routes.post('/update', response_class=HTMLResponse)
async def user_update(
    request: Request, 
    form_data: UserForm = Depends(UserForm.as_form), 
    db: Session = Depends(get_db)
    ):
    user_data = {
        'id': settings.ID_USER,
        'title': form_data.title,
        'image': f"{request.url_for('static', path='images/')}{form_data.image.filename}",
        'name': form_data.name,
        'email': form_data.email,
        'phone': f'+{int(form_data.phone)}',
        'twitter_user': form_data.twitter_user,
        'text_description': form_data.description
    }
    user = NewUser(**user_data)
    
    save_image(form_data.image.filename, form_data.image.file) 

    user = updated_or_create_user(db=db, user=user)
    context = {
        'request': request,
    }
    
    
    
    return RedirectResponse("data", status_code=303)