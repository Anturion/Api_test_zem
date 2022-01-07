import re
from datetime import datetime
from typing import List

from pydantic import BaseModel, Field, validator, EmailStr

ALPHANUMERIC = r'^[a-zA-ZñÑ\s]+$'
PHONE_FORMAT = r'^\+[\d]{1,13}$'

class NewUser(BaseModel):
    
    id : int = Field(...)
    title : str = Field(...)
    image : str = Field(...)
    name : str = Field(...)
    email : str = Field(...)
    phone : str = Field(...)
    twitter_user : str = Field(...)
    text_description : str = Field(...)
    
    class Config:
        
        fields = {
            'names': {'max_length': 64, 'regex': ALPHANUMERIC},
            'phone': {'max_length': 13, 'regex': PHONE_FORMAT},
        }
    
class GetUser(NewUser):
    
    
    id: int
    
    class Config:
        
        orm_mode=True