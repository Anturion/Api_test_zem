from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from connection_database.database_connection import Base, engine_mysql
from src.routes.index import index_routes
from src.routes.user_session import user_routes

Base.metadata.create_all(bind=engine_mysql)

description = """
User portfolio

## Index

Render an introductory landing page.

## Users Data

You will be able to:

* **Update users** user/update.
* **Read users** user/data.
"""
contact={
        "name": "Alejandro Campillo Barrios",
        "url": "https://github.com/Anturion",
        "email": "alucardcampillo@gmail.com",
    }

tags_metadata = [
    {
        "name": "Index",
        "description": "Get an introductory HtmlResponse with Jinja2 templates",
    },
    {
        "name": "User Data",
        "description": "Manage user: get and updated info user from the database and their last 5 tweets"
    },
]

app = FastAPI(title='Zemoga API Test', 
              description=description, 
              contact=contact,
              openapi_tags=tags_metadata)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(index_routes)
app.include_router(user_routes)


