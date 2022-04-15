from flask import Flask

app = Flask(__name__)

from app import routes  # __init__ 与 routes 相互 import，这一行放在最后而不是行首可以保证 routes 能成功 import app.app
