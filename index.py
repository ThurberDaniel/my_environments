from flask import Flask, render_template, flash, redirect, request, session, logging, url_for

from flask_sqlalchemy import SQLAlchemy

from forms import LoginForm, RegisterForm

app = Flask(__name__)
print(app)

app.config['SECRET_KEY'] = '!9m@S-dTsfsfwwwhyIlW[pHQbN^'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/auth'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):

    __tablename__ = 'usertable'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(15), unique=True)

    username = db.Column(db.String(15), unique=True)

    email = db.Column(db.String(50), unique=True)

    password = db.Column(db.String(256), unique=True)
    password = paswrd
