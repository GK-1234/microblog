from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_login import AnonymousUserMixin

#app = Flask(__name__)
#
class MyCustomAnonymousUser(AnonymousUserMixin):
    def __init__(self):
        self.roles = []

#flask_app = Flask(...)  # some flask app being initialized
app = Flask(__name__)

login = LoginManager(app)
login.login_view = 'login'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#@login_manager.user_loander
#def load_user(id):
#    return User.query.filter_by(user_id=id).first()


from app import routes, models
