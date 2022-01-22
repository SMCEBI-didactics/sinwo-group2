import os
import config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__,
            instance_relative_config=True,
            static_folder="static",
            static_url_path="")

app.config.from_object("config")

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# routing
from WebApp import views
# struktura bazy 
from WebApp import models 


