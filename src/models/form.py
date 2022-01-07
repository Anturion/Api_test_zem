from fastapi import Form, File, UploadFile
from pydantic import BaseModel

class UserForm(BaseModel):
    
    title: str
    name: str
    email: str
    phone: str
    twitter_user: str
    description: str
    image: UploadFile
    
    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        description: str = Form(...),
        name: str = Form(...),
        email: str =  Form(...),
        phone: str =  Form(...),
        twitter_user: str =  Form(...),
        image: UploadFile = File(...)
    ):
        return cls(
            title = title,
            description = description,
            image = image,
            name = name,
            email = email,
            phone = phone,
            twitter_user = twitter_user
        )