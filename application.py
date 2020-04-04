import os

from config import config
from app import create_app

application = create_app(os.environ.get('FLASK_ENV', 'development'))
