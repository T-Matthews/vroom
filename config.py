import os

basedir=os.path.abspath(os.path.dirname(__name__))
class Config:
    FLASK_APP=os.environ.get('FLASK_APP')
    FLASK_DEBUG=os.environ.get('FLASK_DEBUG')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    GAS_KEY=os.environ.get('GAS_KEY')
    EIA_KEY=os.environ.get('EIA_KEY')

