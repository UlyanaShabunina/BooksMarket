from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
##app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://olguksvapksbhz:1e7c4caef29027dac8f921c52ef5532578fd3e5ca59fcec96efaf13a64e579cb@ec2-35-170-146-54.compute-1.amazonaws.com:5432/dc8vodal6jeto0'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'xf3g82g27f9cdv443ui480nw'
login = LoginManager(app)
login.login_view = 'login'
app.config['SECRET_KEY'] = 'xf3g82g27f9cdv443ui480nw'
MAX_CONTENT_LENGTH = 1024 * 1024
generate_password_hash = generate_password_hash
check_password_hash = check_password_hash


