from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, session, jsonify, make_response
app = Flask(__name__)
app.config['SECRET_KEY'] = '1515dd15dd3d5d1a51b5af515ca'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

class NewsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(1000), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    user = db.relationship('UserModel', backref=db.backref('NewsModel', lazy=True))
    def __repr__(self):
        return '<NewsModel {} {} {}>'.format(self.id, self.title, self.content)