from flask import Flask
try:
    from flask.ext.sqlalchemy import SQLAlchemy
except:
    from flask_sqlalchemy import SQLAlchemy  # this is the new way to do it which works!
from config import Configuration # import our configuration data

app = Flask(__name__)
app.config.from_object(Configuration) # use values from our Configuration object.
db = SQLAlchemy(app)
