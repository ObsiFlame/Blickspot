from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import string
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'ad7ceffecbaabd63274ed5a47d031c10'
app.permanent_session_lifetime = timedelta(hours=1)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from blickspot import routes