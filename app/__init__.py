from flask import Flask
import os
from config import Config


app = Flask(__name__)
app.config['SECRET_KEY']=os.environ.get('SECRET_KEY')
app.config.from_object(Config)	


from . import routes
