#Statement for enabling development environment
DEBUG = True
import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))
BASE_DIR= os.path.abspath(os.path.dirname(__file__))

# Application thrads. common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other
THREADS_PER_PAGE=2
#Enable protection agains cross-site request forgery (CSRF)
CSRF_ENABLED=True
#Use a secure, unique and absolutely secret key for a signing the data
CSRF_SESSION_KEY = "secret"
#Secret key for signing cookies
SECRET_KEY="secret"

SCHEDULER_VIEWS_ENABLED = True

#Configuration for uploader files
UPLOAD_FOLDER='data/'
MAX_CONTENT_LENGTH= 5 * 1024 * 1024
PER_PAGE=100
