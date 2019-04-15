from flask import Flask

# https://flask-migrate.readthedocs.io/en/latest/
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager  # pip install Flask-Script

from flask_sqlalchemy import SQLAlchemy  # this is the new way to do it which works!
from config import Configuration # import our configuration data

app = Flask(__name__)
app.config.from_object(Configuration) # use values from our Configuration object.
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
