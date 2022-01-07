# Zemoga test API

## Introduction


Web APP development made for the backend with integrated FastAPI together with Jinja2 to present the frontend. In this portfolio you will be able to see and update the information of a single consumer

### General features
- The page has an introductory landing page, an endpoint that shows user information obtained from a remote MySQL database and another endpoint to update user information through a form

- All form fields are required to perform the post method

### Twitter API
- The tweepy library was used for the integration of the Twitter API. An attempt was made to obtain user tweets using Version 2 of the Twitter API, however when the user was consulted with the credentials given by the company, no data was returned, therefore the endpoints of version 1 were used, from which it is performed. a query to obtain the user's id through his username on twitter and later obtain the 5 most recent tweets

- The twitter user is saved in the database, this allows that at the same time that his data is consulted, the last 5 tweets published can be acquired

### MySQL 
- The connection and management of the database was done with the SQLAlchemy library where the connection string for the database is created

### Environment
- You can configure the .env to connect to other MySQL databases, the only required field is the Twitter Token Barear, if you do not configure the other fields, by default the fields given will be used for the connection to the database, you can also configure another ID_USER to create a new record in the database and update it through the application.

## Runing the project
To run the project you only need to create a virtual environment with the library of your choice, for this case venv was used
~~~
python -m venv <name of environment>  
~~~
The next thing is to activate the environment, please visit this page for more [information](https://docs.python.org/es/3/library/venv.html)

The following will be to install the project dependencies, for this type in your terminal:
~~~
pip install -r requirements.txt 
~~~
Make sure you have properly configured the .env and finally run:
~~~
uvicorn main:app
~~~

Now you can see the documantation swagger on http://127.0.0.1:8000/docs

## Docker
A dockerfile is added with all the necessary requirements to run the project, you only need to build the image and run the container.

### Time used
The time invested in this test was approximately 12 hours