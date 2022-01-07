from sqlalchemy.orm import Session
from src import settings
from src.models.user import NewUser
from connection_database.database_table import User

def updated_or_create_user(db: Session, user: NewUser):
    
    db_user = User(
            
            id = settings.ID_USER,
            title=user.title,
            name = user.name,
            email = user.email,
            phone = user.phone,
            twitter_user = user.twitter_user, 
            text_description=user.text_description, 
            image=user.image,
            
        )
    
    if db.query(User).filter(User.id == settings.ID_USER).first():
        
        db.query(User).filter(User.id==settings.ID_USER).update(
            {
                'title': db_user.title,
                'name': db_user.name,
                'email': db_user.email,
                'phone': db_user.phone,
                'twitter_user': db_user.twitter_user,
                'text_description': db_user.text_description,
                'image': db_user.image
             }
        )
        db.commit()
        
    else:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
        

def get_user_by_id(db: Session):
    
    return db.query(User).filter(User.id == settings.ID_USER).first()