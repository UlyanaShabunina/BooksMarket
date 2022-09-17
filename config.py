from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
##app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lovuuyrjjhgauv:8825b561c89f8e5e35068abf94df9428749ed9842577b9b76b21896516748e6a@ec2-34-200-205-45.compute-1.amazonaws.com:5432/d179n024ck62s9'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'xf3g82g27f9cdv443ui480nw'
login = LoginManager(app)
login.login_view = 'login'
app.config['SECRET_KEY'] = 'xf3g82g27f9cdv443ui480nw'
MAX_CONTENT_LENGTH = 1024 * 1024
generate_password_hash = generate_password_hash
check_password_hash = check_password_hash


