"""SQLAlchemy models for Twitoff"""

#import
from flask_sqlalchemy import SQLAlchemy

#create a database
DB = SQLAlchemy()

#Twitter users that we pull and analyse
class User(DB.Model):
    id  = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

#Tweets
class Tweet(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.Unicode(300))
    #the below 2 rows are going to allow us to connect user.id to tweets
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets'), lazy=True)
