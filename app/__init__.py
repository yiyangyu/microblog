from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models  # __init__ 与 routes 相互 import，这一行放在最后而不是行首可以保证 routes 能成功 import app.app
