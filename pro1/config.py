import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'Ok,_thi'   


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):

    TYPE_BASE = 'postgresql'
    USER = 'postgres'
    PASS = 'admin'
    HOST = 'localhost'
    PORT = '5432'
    DB = 'flask_db'

    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'{TYPE_BASE}://{USER}:{PASS}@{HOST}:{PORT}/{DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    TESTING = True
