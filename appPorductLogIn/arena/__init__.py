from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager 
app=Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
app.config['SECRET_KEY']='3b93a296b661e4e3c8d5315a'
db=SQLAlchemy(app)

bcrypt=Bcrypt(app)


login_manager=LoginManager(app)
login_manager.login_view="login_page"
login_manager.login_message_category="info"

from arena import routes


