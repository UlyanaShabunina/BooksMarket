from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
##app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bjlqshdcuyfxkv:c3f0e52679fa020795211c805b3c3a3cd246027bdb5b2c3e64ad0db6b1956536@ec2-52-200-5-135.compute-1.amazonaws.com:5432/dfa2gjaos48d7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'xf3g82g27f9cdv443ui480nw'
login = LoginManager(app)
login.login_view = 'login'
app.config['SECRET_KEY'] = 'xf3g82g27f9cdv443ui480nw'
MAX_CONTENT_LENGTH = 1024 * 1024
generate_password_hash = generate_password_hash
check_password_hash = check_password_hash


