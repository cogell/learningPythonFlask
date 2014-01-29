import os
from flask import Flask

# create instance of Flask class
app = Flask(__name__)

# set up app config
APP_ROOT = os.path.dirname( os.path.abspath(__file__) )
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import views