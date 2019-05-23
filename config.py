import os

_basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    UPLOAD_FOLDER = "files"
    ALLOWED_EXTENSIONS = set(['pdf', 'jpg', 'png'])

class ProductionConfig(Config):
    # TODO: generate SECRET_KEY with python -c "import os; print(str(os.urandom(16)))"
    SECRET_KEY = 'key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRO_DATABASE_URL') or \
        'sqlite:///' + os.path.join(_basedir, 'DATABASE.db3')
    # TODO: set a custom email and password"
    ADMIN = {"name": "admin",
             "surname": "",
             "category": "administrator",
             "email": "admin",
             "password": ""}

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'devkey'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(_basedir, 'DATABASE.db3')
    ADMIN = {"name": "admin",
             "surname": "",
             "institute": "",
             "category": "administrator",
             "email": "admin",
             "password": "admin"}

class TestingConfig(Config):
    TESTING = True
    SECRET_KEY = 'testkey'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(_basedir, 'DATABASE.db3')
    ADMIN = {"name": "admin",
             "surname": "",
             "institute": "",
             "category": "administrator",
             "email": "admin",
             "password": "admin"}

# custom configuration
config = DevelopmentConfig

host = '0.0.0.0'
port = 80
