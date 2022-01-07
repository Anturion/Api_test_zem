import os
from dotenv import load_dotenv

load_dotenv()

#Twitter settings

BEAREAR_TWITTER_TOKEN = os.environ.get('BEAREAR_TWITTER_TOKEN')

#Database settings

USERNAME_DB = os.environ.get('USERNAME_DB', 'zemoga_test_db')
PASSWORD = os.environ.get('PASSWORD', 'Zem0ga.101')
HOST = os.environ.get('HOST', 'zemoga-test-db.crhpedy9xxto.us-east-1.rds.amazonaws.com')
DB_NAME = os.environ.get('DB_NAME', 'zemoga_test_db')
PORT = os.environ.get('PORT', '3306')
ID_USER = int(os.environ.get('ID_USER', '45678'))
