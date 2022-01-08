import os
from dotenv import load_dotenv

load_dotenv()

#Twitter settings

BEAREAR_TWITTER_TOKEN = os.environ.get('BEAREAR_TWITTER_TOKEN')

#Database settings

USERNAME_DB = os.environ.get('USERNAME_DB')
PASSWORD = os.environ.get('PASSWORD')
HOST = os.environ.get('HOST')
DB_NAME = os.environ.get('DB_NAME')
PORT = os.environ.get('PORT')
ID_USER = int(os.environ.get('ID_USER', '45678'))
