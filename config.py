######## KONFIGURACJA #############

import os

ORIGINS = ["*"]
SECRET_KEY = "ad39defhkasdf0avfdsiav90AOD0DFs1" # to powinno być tajne :)

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
    os.path.join(basedir, 'database/sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False

